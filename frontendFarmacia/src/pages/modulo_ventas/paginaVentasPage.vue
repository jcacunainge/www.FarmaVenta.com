<template>
  <q-page padding>
    <div class="row items-center q-gutter-sm q-mb-md">
      <q-breadcrumbs>
        <q-breadcrumbs-el label="Ventas" />
        <q-breadcrumbs-el label="Pagina de Ventas de Medicamentos" />
      </q-breadcrumbs>
    </div>

    <div>
      <div class="q-mb-sm flex justify-end">
        <div class="text-blue-10 text-subtitle1">{{ fechaHoy }}</div>
      </div>
      <div style="max-width: 100vw">
        <q-card flat>
          <div class="q-mb-md">
            <fieldset class="row q-gutter-sm">
              <legend class="text-blue-10">Información Básica Vendedor</legend>
              <q-input v-model="formItemVendedor.codigo_usuario" dense outlined filled type="text" disable readonly
                label="Nombre del Vendedor:" class="col-xs-12 col-sm-12 col-md-2" hide-bottom-space />
              <q-input v-model="formItemVendedor.codigo_usuario" dense outlined filled type="text" disable readonly
                label="Codigo Vendedor:" class="col-xs-12 col-sm-12 col-md-2" hide-bottom-space />
              <q-input v-model="formItemVendedor.nombre_negocio" dense outlined filled type="text" disable readonly
                label="Nombre Negocio:" class="col-xs-12 col-sm-12 col-md-2" hide-bottom-space />
              <q-input v-model="formItemVendedor.dirrecion_negocio" dense outlined filled type="text" disable readonly
                label="Dirreción Negocio:" class="col-xs-12 col-sm-12 col-md-2" hide-bottom-space />
              <q-input v-model="formItemVendedor.telefono_negocio" dense outlined filled type="text" disable
                readonlylabel="Telefono:" class="col-xs-12 col-sm-12 col-md-2" hide-bottom-space />
            </fieldset>
          </div>
          <div class="q-mb-md">
            <fieldset class="row q-gutter-sm">
              <legend class="text-blue-10">Información Básica Comprador</legend>
              <q-input v-model="formItemCliente.documento_cliente" dense outlined filled type="text"
                label="Número Documento" class="col-xs-12 col-sm-12 col-md-2" hide-bottom-space
                @blur="fetchClienteData" />
              <q-input v-model="formItemCliente.nombre_cliente" dense outlined filled type="text"
                label="Nombre del cliente" class="col-xs-12 col-sm-12 col-md-2" hide-bottom-space />
              <q-input v-model="formItemCliente.telefono_cliente" dense outlined filled type="text" label="Teléfono"
                class="col-xs-12 col-sm-12 col-md-2" hide-bottom-space />
              <q-input v-model="formItemCliente.correo_cliente" dense outlined filled type="text" label="Correo"
                class="col-xs-12 col-sm-12 col-md-2" hide-bottom-space />
              <q-btn @click="guardarCliente" color="green" text-color="white" dense class="q-pa-sm"
                label="Guardar Cliente" style="width: 150px" />
            </fieldset>
          </div>
        </q-card>
      </div>
    </div>

    <div>
      <q-table :rows="productos" :columns="columnas" row-key="codigo" flat separator="cell" class="headerTable" dense>
        <template v-slot:body-cell="props">
          <q-td :props="props">
            <!-- Condición para la columna nombre_medicamento -->
            <template v-if="props.col.field === 'nombre_medicamento'">
              <q-select v-model="props.row[props.col.field]" use-input hide-dropdown-icon :options="optionesProductos"
                @filter="filterFn" @update:model-value="actualizarCampos(props)"
                @keydown.enter="manejarTeclaEnter(props)" @keydown.tab="moverALaSiguienteFila(props)" clearable />
            </template>
            <!-- Condición para las columnas no editables -->
            <template v-else-if="!esEditable(props.col.field)">
              {{ props.row[props.col.field] }}
            </template>
            <!-- Condición para las columnas editables -->
            <template v-else>
              <q-input v-model="props.row[props.col.field]" @keydown.enter="manejarTeclaEnter(props)"
                @keydown.tab="moverALaSiguienteFila(props)" @update:model-value="actualizarTotal(props.row)" />
            </template>
          </q-td>
        </template>

        <template #top>
          <div class="col-grow flex row justify-between">
            <div class="q-gutter-md">
              <q-checkbox label="Ver Solo Stock" v-model="verStock" />
              <q-btn color="white" text-color="black" dense class="q-ml-sm q-pa-sm" label="Ventas Detalladas"
                style="width: 180px" />
            </div>
            <div>
              <q-btn text-color="white" dense class="bg-blue-10 q-ml-sm q-pa-sm" label="Realizar Venta"
                style="width: 180px" @click="guardarVenta" />
            </div>
          </div>
        </template>
        <template #bottom>
          <q-btn color="green" text-color="white" dense class="q-pa-sm" label="Cotizar" style="width: 100px" />
        </template>
      </q-table>
    </div>
    <div class="text-center">
      <div dense class="text-h5 text-blue-10 text-weight-bold">
        Total de Ventas $ {{ totalVentas }}
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { useQuasar } from "quasar";
import { ref, onMounted, computed, watch, nextTick } from "vue";
import { api } from "boot/axios";
import { useRules, useNotify } from "src/composables/";
import { date } from "quasar";
import { useAuthStore } from "src/stores/authStore";
const authStore = useAuthStore();
const user = computed(() => authStore.user);

/* Variables iniciales */
const { messageWarning, messageSuccess } = useNotify();
const { required } = useRules();

const verStock = ref(true);

const timeStamp = Date.now();
const fechaHoy = date.formatDate(timeStamp, "YYYY-MM-DD");

const formItemCliente = ref({
  nombre_cliente: "",
  documento_cliente: "",
  telefono_cliente: "",
  correo_cliente: "",
});

const formItemVendedor = ref({
  nombre_usuario: user.value.nombre_usuario,
  codigo_usuario: user.value.codigo_usuario,
  nombre_negocio: user.value.nombre_negocio,
  dirrecion_negocio: user.value.dirrecion_negocio,
  telefono_negocio: user.value.telefono_negocio,
});

onMounted(async () => {
  await initialize();
});
const initialize = async () => {
  await obtenerMedicamentos();
};

/*Trae los registros de la tabla*/
const datosProductos = ref([]);
const obtenerMedicamentos = async () => {
  await api
    .get("medicamentos/")
    .then(({ data }) => {
      datosProductos.value = data;
    })
    .catch((error) => {
      messageWarning(error?.response?.data?.message);
    });
};

// Limpiar datos en una fila específica
const limpiarFila = (fila) => {
  fila.codigo = "";
  fila.nombre_medicamento = "";
  fila.fabricante = "";
  fila.fecha_vencimiento = "";
  fila.cantidad = "";
  fila.lote = "";
  fila.stock = "";
  fila.precio = "";
  fila.total = "";
  fila.descuento = "";
  actualizarTotal(fila);
};

// Actualizar campos cuando se selecciona el medicamento
const actualizarCampos = (props) => {
  const valorBusqueda = props.row.nombre_medicamento;

  // Si el campo nombre_medicamento está vacío, limpia la fila y elimina la fila si es necesario
  if (!valorBusqueda) {
    limpiarFila(props.row);
    eliminarFilaSiPrimeraVacia();
    return;
  }

  const producto = datosProductos.value.find(
    (p) => p.nombre_medicamento.toLowerCase() === valorBusqueda.toLowerCase()
  );

  if (producto) {
    props.row.codigo = producto.codigo;
    props.row.fabricante = producto.fabricante;
    props.row.fecha_vencimiento = producto.fecha_vencimiento;
    props.row.lote = producto.lote;
    props.row.stock = producto.stock;
    props.row.precio = producto.precio;
    props.row.total = "";
    actualizarTotal(props.row);
    agregarNuevaFila();
  } else {
    limpiarFila(props.row);
  }
};

// Productos iniciales
const productos = ref([
  {
    codigo: "",
    nombre_medicamento: "",
    fabricante: "",
    fecha_vencimiento: "",
    cantidad: "",
    lote: "",
    stock: "",
    precio: "",
    total: "",
    descuento: "",
  },
]);

// Agregar una nueva fila
const agregarNuevaFila = () => {
  // Solo añade una nueva fila si no hay fila vacía
  if (
    productos.value.length === 0 ||
    productos.value[productos.value.length - 1].nombre_medicamento !== ""
  ) {
    productos.value.push({
      codigo: "",
      nombre_medicamento: "",
      fabricante: "",
      fecha_vencimiento: "",
      cantidad: "",
      lote: "",
      stock: "",
      precio: "",
      total: "",
      descuento: "",
    });
  }
};

// Función para eliminar la última fila si la primera fila está vacía
const eliminarFilaSiPrimeraVacia = () => {
  if (
    productos.value.length > 1 &&
    productos.value[0].nombre_medicamento === ""
  ) {
    productos.value.shift(); // Elimina la primera fila
  }
};

// Manejar la tecla Enter
const manejarTeclaEnter = (props) => {
  const valorBusqueda = props.row[props.col.field];

  // Si el campo nombre_medicamento está vacío, limpia la fila y elimina la fila si es necesario
  if (!valorBusqueda) {
    limpiarFila(props.row);
    eliminarFilaSiPrimeraVacia();
    return;
  }

  const producto = datosProductos.value.find(
    (p) =>
      p.codigo === valorBusqueda ||
      p.nombre_medicamento.toLowerCase() === valorBusqueda.toLowerCase()
  );

  if (producto) {
    props.row.nombre_medicamento = producto.nombre_medicamento;
    props.row.fabricante = producto.fabricante;
    props.row.fecha_vencimiento = producto.fecha_vencimiento;
    props.row.lote = producto.lote;
    props.row.stock = producto.stock;
    props.row.precio = producto.precio;
    actualizarTotal(props.row);
    agregarNuevaFila();
  } else {
    // Limpia la fila actual si no se encuentra el producto
    limpiarFila(props.row);
  }

  eliminarFilaSiPrimeraVacia(); // Elimina la primera fila si está vacía
};

// Actualizar el total de la fila
const actualizarTotal = (row) => {
  const cantidad = parseFloat(row.cantidad) || 0;
  const descuento = parseFloat(row.descuento) || 0;
  const precio = parseFloat(row.precio) || 0;
  row.total = cantidad * precio - descuento;
};

// Verificar si una columna es editable
const esEditable = (campo) => {
  const columnasNoEditables = [
    "fabricante",
    "fecha_vencimiento",
    "lote",
    "stock",
    "precio",
    "total",
  ];
  return !columnasNoEditables.includes(campo);
};

//Filtrado de Columna nombre_medicamento
const optionesProductos = ref(
  datosProductos.value.map((p) => p.nombre_medicamento)
);

const filterFn = (val, update, abort) => {
  if (val.length < 1) {
    abort();
    return;
  }
  update(() => {
    const needle = val.toLowerCase();
    optionesProductos.value = datosProductos.value
      .map((p) => p.nombre_medicamento)
      .filter(
        (nombre_medicamento) =>
          nombre_medicamento.toLowerCase().indexOf(needle) > -1
      );
  });
};

watch(productos, (newRows) => {}, { deep: true });

const totalVentas = computed(() => {
  return productos.value.reduce((sum, item) => sum + (item.total || 0), 0);
});

const fetchClienteData = async () => {
  try {
    const { data } = await api.get(
      `clientes/${formItemCliente.value.documento_cliente}`
    );
    console.log(data);
    if (data) {
      formItemCliente.value = {
        ...formItemCliente.value,
        nombre_cliente: data.nombre_cliente,
        telefono_cliente: data.telefono_cliente,
        correo_cliente: data.correo_cliente,
      };
    } else {
      formItemCliente.value = {
        ...formItemCliente.value,
        nombre_cliente: "",
        telefono_cliente: "",
        correo_cliente: "",
      };
    }
  } catch (error) {
    console.error("Error fetching client data:", error);
  }
};

watch(
  () => formItemCliente.value.documento_cliente,
  (newValue) => {
    if (newValue) {
      fetchClienteData();
    }
  }
);

const guardarCliente = async () => {
  const formData = JSON.stringify(formItemCliente.value);
  try {
    const response = await api.post("clientes/", formData);
    messageSuccess("Cliente guardado con éxito!");
  } catch (error) {
    messageWarning(
      "Error al guardar el cliente!"
    );
  }
};

const dataInfoVentta = computed(() => ({
  dataVendedor: formItemVendedor.value,
  dataCliente: formItemCliente.value,
  itemsVentas: productos.value,
}));

const guardarVenta = async (row) => {


  try {
    // Elimina filas vacías
    dataInfoVentta.value.itemsVentas = dataInfoVentta.value.itemsVentas.filter(
      (item) => item.nombre_medicamento.trim() !== ""
    );
    const response = await api.post("ventas/", dataInfoVentta.value);
    productos.value = [{}];

    formItemCliente.value = {
      nombre_cliente: "",
      documento_cliente: "",
      telefono_cliente: "",
      correo_cliente: "",
    };
    messageSuccess("Venta Realizada con éxito!");
  } catch (error) {
    console.error("Error saving sale:", error);
    messageWarning(
      "Error al realizar la venta!"
    );
  }
};

// Definición de columnas
const columnas = [
  {
    name: "nombre_medicamento",
    align: "left",
    label: "Medicamento",
    field: "nombre_medicamento",
    sortable: true,
  },
  {
    name: "cantidad",
    align: "right",
    label: "Cantidad",
    field: "cantidad",
    sortable: true,
  },
  {
    name: "descuento",
    align: "right",
    label: "Descuento",
    field: "descuento",
    sortable: true,
  },
  {
    name: "fabricante",
    align: "center",
    label: "Fabricante",
    field: "fabricante",
    sortable: true,
  },
  {
    name: "fecha_vencimiento",
    align: "center",
    label: "Fecha Vencimiento",
    field: "fecha_vencimiento",
    sortable: true,
  },

  {
    name: "lote",
    align: "center",
    label: "Lote",
    field: "lote",
    sortable: true,
  },
  {
    name: "stock",
    align: "right",
    label: "Stock",
    field: "stock",
    sortable: true,
  },
  {
    name: "precio",
    align: "right",
    label: "Precio",
    field: "precio",
    sortable: true,
  },
  {
    name: "total",
    align: "right",
    label: "Total",
    field: "total",
    sortable: true,
  },
];
</script>

<style scoped>
.q-table {
  width: 100%;
}

.q-td {
  padding: 0 !important;
}

.headerTable thead th {
  background-color: #154280;
  color: #fff;
}
</style>
