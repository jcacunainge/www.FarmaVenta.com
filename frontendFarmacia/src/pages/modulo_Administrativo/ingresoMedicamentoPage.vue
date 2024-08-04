<template>
  <q-page padding>
    <div class="row items-center q-gutter-sm q-mb-md">
      <q-breadcrumbs>
        <q-breadcrumbs-el label="Panel Administrativo" />
        <q-breadcrumbs-el label="Página de Ingreso de Medicamentos" />
      </q-breadcrumbs>
    </div>

    <div class="text-h5 q-mb-md text-blue-10">Ingreso de Medicamentos</div>
    <q-form class="q-gutter-sm row">
      <div class="q-mb-md col-md-12">
        <fieldset class="row q-gutter-sm">
          <legend class="text-blue-10">Información Básica del Comprador</legend>
          <q-select v-model="formItemCliente.documento_cliente" label="Documentos Cliente" :options="filteredClientes"
            option-label="label" option-value="value" use-input emit-value map-options outlined filled
            class="col-xs-12 col-sm-12 col-md-3" dense hide-bottom-space clearable @filter="filterCliente" />
          <q-input v-model="formItemCliente.nombre_cliente" dense outlined filled type="text" label="Nombre del Cliente"
            class="col-xs-12 col-sm-12 col-md-3" hide-bottom-space />
          <q-input v-model="formItemCliente.telefono_cliente" dense outlined filled type="text" label="Teléfono"
            class="col-xs-12 col-sm-12 col-md-2" hide-bottom-space />
          <q-input v-model="formItemCliente.correo_cliente" dense outlined filled type="text" label="Correo"
            class="col-xs-12 col-sm-12 col-md-3" hide-bottom-space />
        </fieldset>
      </div>
    </q-form>

    <q-list bordered class="q-mt-md">
      <q-item v-for="(medicamento, index) in medicamentos" :key="medicamento.codigo" class="bg-red-1 q-mb-md">
        <q-item-section>
          <q-item-label>
            <span class="text-weight-bold">Código: </span>{{ medicamento.codigo }}
          </q-item-label>
          <q-item-label>
            <span class="text-weight-bold">Nombre Medicamento: </span>{{ medicamento.nombre_medicamento }}
          </q-item-label>
          <q-item-label>
            <span class="text-weight-bold">Fabricante: </span>{{ medicamento.fabricante }}
          </q-item-label>
          <q-item-label>
            <span class="text-weight-bold">Fecha Vencimiento: </span>{{ medicamento.fecha_vencimiento }}
          </q-item-label>
          <q-item-label>
            <span class="text-weight-bold">Cantidad: </span>{{ medicamento.cantidad }}
          </q-item-label>
          <q-item-label>
            <span class="text-weight-bold">Lote: </span>{{ medicamento.lote }}
          </q-item-label>
          <q-item-label>
            <span class="text-weight-bold">Stock: </span>{{ medicamento.stock }}
          </q-item-label>
          <q-item-label>
            <span class="text-weight-bold">Precio: </span>{{ medicamento.precio }}
          </q-item-label>
        </q-item-section>
        <q-item-section side>
          <q-btn icon="delete" color="red" @click="eliminarMedicamento(index)"></q-btn>
        </q-item-section>
      </q-item>
    </q-list>
  </q-page>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import { api } from "boot/axios";

const formItemCliente = ref({
  nombre_cliente: "",
  documento_cliente: "",
  telefono_cliente: "",
  correo_cliente: "",
});

watch(
  () => [formItemCliente.value.documento_cliente],
  async ([newDocumento]) => {
    formItemCliente.value.nombre_cliente = "";
    formItemCliente.value.telefono_cliente = "";
    formItemCliente.value.correo_cliente = "";
    if (newDocumento) {
      await obtenerCliente();
    }
  }
);

onMounted(async () => {
  await initialize();
});

const initialize = async () => {
  await cargarClientes();
};

const filteredClientes = ref([]);
const lvclientes = ref([]);

const cargarClientes = async () => {
  try {
    const { data } = await api.get("clientes/");
    lvclientes.value = data.map(({ documento_cliente }) => ({
      value: documento_cliente,
      label: documento_cliente,
    }));
    filteredClientes.value = lvclientes.value;
  } catch (error) {
    console.warn(error?.response?.data?.message);
  }
};

const filterCliente = (val, update) => {
  if (val === "") {
    update(() => {
      filteredClientes.value = lvclientes.value;
    });
    return;
  }
  update(() => {
    const needle = val.toLowerCase();
    filteredClientes.value = lvclientes.value.filter((cliente) =>
      cliente.label.toLowerCase().includes(needle)
    );
  });
};

const obtenerCliente = async () => {
  const { documento_cliente } = formItemCliente.value;
  try {
    const { data } = await api.get(`clientes/${documento_cliente}`);
    if (data) {
      formItemCliente.value.nombre_cliente = data.nombre_cliente;
      formItemCliente.value.correo_cliente = data.correo_cliente;
      formItemCliente.value.telefono_cliente = data.telefono_cliente;
    }
  } catch (error) {
    console.warn(error?.response?.data?.message);
  }
};
</script>

<!--
<template>
  <q-page padding>
    <div class="row items-center q-gutter-sm q-mb-md">
      <q-breadcrumbs>
        <q-breadcrumbs-el label="Ingreso" />
        <q-breadcrumbs-el label="Ingresar Medicamentos" />
      </q-breadcrumbs>
    </div>
    <DataTable :title="title" :rows="desserts" :columns="columns" :dense="true" :on-add-item="addItem"
      :on-initialize="initialize" :pagination="pagination" border-cell="horizontal">
      <template #columns="props">
        <q-tr class="text-uppercase" :props="props">
          <q-td>
            {{ props.row.codigo }}
          </q-td>
          <q-td>
            {{ props.row.nombre_medicamento }}
          </q-td>
          <q-td>
            {{ props.row.fabricante }}
          </q-td>
          <q-td>
            {{ props.row.fecha_vencimiento }}
          </q-td>
          <q-td>
            {{ props.row.cantidad }}
          </q-td>
          <q-td>
            {{ props.row.lote }}
          </q-td>
          <q-td>
            {{ props.row.stock }}
          </q-td>
          <q-td class="text-right">
            {{ formatCurrency(props.row.precio) }}
          </q-td>

          <q-td class="text-center">
            <q-btn dense flat round color="primary" icon="las la-ellipsis-v">
              <q-menu transition-show="scale" transition-hide="scale">
                <q-list dense>
                  <q-item v-ripple v-close-popup clickable @click="editItem(props.row)">
                    <q-item-section class="q-mx-sm">Editar</q-item-section>
                  </q-item>
                  <q-item v-ripple v-close-popup clickable @click="deleteItem(props.row.codigo)">
                    <q-item-section class="q-mx-sm">Eliminar</q-item-section>
                  </q-item>
                </q-list>
              </q-menu>
            </q-btn>
          </q-td>
        </q-tr>
      </template>
    </DataTable>

    <ModalDialog v-model="dialogForm" :title="formTitle" :on-save="save" :on-close="close">
      <template #body>
        <q-input v-model="formItem.codigo" label="Código" dense type="text" class="col-xs-12 col-sm-12 col-md-6 "
          maxlength="20" outlined />
        <q-input v-model="formItem.nombre_medicamento" label="Nombre del Medicamento" dense type="text"
          class="col-xs-12 col-sm-12 col-md-6 " maxlength="100" outlined />
        <q-input v-model="formItem.fabricante" label="Fabricante" dense type="text"
          class="col-xs-12 col-sm-12 col-md-6 " maxlength="50" outlined />
        <q-input v-model="formItem.fecha_vencimiento" label="Fecha de Vencimiento" dense type="date"
          class="col-xs-12 col-sm-12 col-md-6" outlined />
        <q-input v-model.number="formItem.cantidad" label="Cantidad" dense type="number"
          class="col-xs-12 col-sm-12 col-md-6" outlined />
        <q-input v-model="formItem.lote" label="Lote" dense type="text" class="col-xs-12 col-sm-12 col-md-6"
          maxlength="20" outlined />
        <q-input v-model.number="formItem.stock" label="Stock" dense type="number" class="col-xs-12 col-sm-12 col-md-6"
          outlined />
        <q-input v-model.number="formItem.precio" label="Precio" dense type="number" step="0.01"
          class="col-xs-12 col-sm-12 col-md-6" outlined />
      </template>
    </ModalDialog>

  </q-page>
</template>

<script setup>
import { useQuasar } from "quasar";
import { ref, onMounted, computed } from "vue";
import { api } from "boot/axios";
import { useRules, useNotify } from "src/composables/";
import DataTable from "src/components/DataTable.vue";
import ModalDialog from "src/components/ModalDialog.vue";
import { formatCurrency } from "src/helpers/formatPrecio";

/* Variables iniciales */
const $q = useQuasar();
const { messageWarning } = useNotify();
const { required } = useRules();

const rules = ref({ required: (value) => required(value) });

const editedIndex = ref(-1);
const dialogForm = ref(false);
const desserts = ref([]);
const title = ref("Ingresar Medicamentos");
const pagination = ref({
  page: 1,
  rowsPerPage: 10,
});

const formItem = ref({
  codigo: '',
  nombre_medicamento: '',
  fabricante: '',
  fecha_vencimiento: '',
  cantidad: 0,
  lote: '',
  stock: 0,
  precio: 0
});

const reset = () => {

const masCodigo = Math.max(
0,
...desserts.value.map((item) => item.codigo)
);

formItem.value = {
codigo: masCodigo,
nombre_medicamento: null,
fabricante: null,
fecha_vencimiento: null,
cantidad: 0,
lote: null,
stock: 0,
precio: 0
};
};

onMounted(async () => {
await initialize();
});

const formTitle = computed(() => {
return editedIndex.value === -1
? "Nuevo Ingresar Medicamentos"
: "Modificar Ingresar Medicamentos";
});

const initialize = async () => {
await fetchData();
adjusteCodigoMedicamento()
};

/*Trae los registros de la tabla*/
const fetchData = async () => {
await api
.get("medicamentos/")
.then(({ data }) => {
console.log(data)
desserts.value = data;
})
.catch((error) => {
messageWarning(error?.response?.data?.message);
});
};


const addItem = () => {
reset()
dialogForm.value = true;
};

const editItem = (item) => {
editedIndex.value = desserts.value.indexOf(item);
formItem.value = Object.assign({}, item);
dialogForm.value = true;
};

const close = () => {
dialogForm.value = false;
setTimeout(() => {
editedIndex.value = -1;
reset();
}, 300);
};

const save = async () => {
const formData = JSON.stringify(formItem.value);
if (editedIndex.value > -1) {
try {
await api.put(`medicamentos/${formItem.value.codigo}`, formData);
initialize();
close();
} catch (error) {
messageWarning("Error al actualizar");
} finally {
btnSaveLoading.value = false;
}
} else {
try {
await api.post("medicamentos/", formData);
messageSuccess("Medicamento Ingresado Corretamente");
initialize();
close();
} catch (error) {
messageWarning("Error al Ingresar Medicamento");
}
}
};

const deleteItem = (codigo) => {
try {
$q.dialog({
title: "Eliminar Información",
message: "¿Desea eliminar esta Información?",
cancel: true,
persistent: true,
}).onOk(async () => {
await api.delete(`medicamentos/${codigo}`);
messageSuccess("Items Medicamentos Eliminado")
adjusteCodigoMedicamento()
await initialize();
});
} catch (error) {
console.log(error);
messageWarning(error?.response?.data?.message);
}
};

const adjusteCodigoMedicamento = () => {
desserts.value.forEach((item, index) => {
item.notdcons = index + 1;
});
};
const columns = [
  {
    name: "codigo",
    field: "codigo",
    label: "Código Medicamento",
    align: "left",
    sortable: true,
  },
  {
    name: "nombre_medicamento",
    field: "nombre_medicamento",
    label: "Medicamento",
    align: "left",
    sortable: true,
  },
  {
    name: "fabricante",
    field: "fabricante",
    label: "Fabricante",
    align: "left",
    sortable: true,
  },
  {
    name: "fecha_vencimiento",
    field: "fecha_vencimiento",
    label: "Fecha Vencimiento",
    align: "left",
    sortable: true,
  },
  {
    name: "cantidad",
    field: "cantidad",
    label: "Cantidad",
    align: "left",
    sortable: true,
  },
  {
    name: "lote",
    field: "lote",
    label: "Lote",
    align: "left",
    sortable: true,
  },

  {
    name: "stock",
    field: "stock",
    label: "Stock",
    align: "left",
    sortable: true,
  },

  {
    name: "precio",
    field: "precio",
    label: "Precio",
    align: "right",
    sortable: true,
    format: (val) => formatCurrency(val),
  },

  {
    name: "opciones",
    field: "opciones",
    label: "Opciones",
    align: "center",
  },
];
</script> -->
