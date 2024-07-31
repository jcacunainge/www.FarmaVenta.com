<template>
  <q-page padding>
    <div class="row items-center q-gutter-sm q-mb-md">
      <q-breadcrumbs>
        <q-breadcrumbs-el label="Panel Administrativo" />
        <q-breadcrumbs-el label="Pagina de Ingreso de Medicamentos" />
      </q-breadcrumbs>
    </div>

    <div class="text-h5 q-mb-md text-blue-10 ">Ingreso de Medicamentos</div>
    <q-form @submit.prevent="agregarMedicamento" class="q-gutter-sm row">
      <q-select v-model="form.codigo" label="Nombre Medicamentos" :options="filteredProductos" option-label="label"
        option-value="value" use-input emit-value map-options outlined filled class="col-xs-12 col-sm-12 col-md-4"
        hide-bottom-space clearable @filter="filterProducto" />
      <q-input v-model="form.fabricante" label="Fabricante" outlined filled
        class="col-xs-12 col-sm-12 col-md-4"></q-input>

      <q-input v-model="form.fecha_vencimiento" label="Fecha de Vencimiento" outlined filled type="date"
        class="col-xs-12 col-sm-12 col-md-4"></q-input>
      <q-input v-model.number="form.cantidad" label="Cantidad" outlined filled type="number"
        class="col-xs-12 col-sm-12 col-md-4"></q-input>
      <q-input v-model="form.lote" label="Lote" outlined filled class="col-xs-12 col-sm-12 col-md-4"></q-input>
      <q-input v-model.number="form.stock" label="Stock" outlined filled type="number"
        class="col-xs-12 col-sm-12 col-md-4"></q-input>
      <q-input v-model.number="form.precio" label="Precio" outlined filled type="number"
        class="col-xs-12 col-sm-12 col-md-4"></q-input>
      <q-btn type="submit" label="Agregar Medicamento" color="primary" class="q-mt-md"></q-btn>
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

const medicamentos = ref([]);
const lvProductos = ref([]);

const form = ref({
  codigo: '',
  nombre_medicamento: '',
  fabricante: '',
  fecha_vencimiento: '',
  cantidad: 0,
  lote: '',
  stock: 0,
  precio: 0
});

const resetForm = () => {
  form.value = {
    codigo: null,
    nombre_medicamento: null,
    fabricante: null,
    fecha_vencimiento: null,
    cantidad: null,
    lote: null,
    stock: null,
    precio: null
  };
};

const agregarMedicamento = () => {
  medicamentos.value.push({ ...form.value });
  resetForm();
};

watch(
  medicamentos,
  (newMedicamentos) => {
    console.log("Datos actualizados:", newMedicamentos);
  },
  { deep: true }
);

const eliminarMedicamento = (index) => {
  medicamentos.value.splice(index, 1);
  console.log(medicamentos)
  resetForm();
};

watch(
  () => form.value.codigo,
  async (newCodigo) => {
    if (newCodigo === "") {
      resetForm();
    } else {
      await obtenerIdMedicamento();
    }
  },
  { immediate: true }
);


onMounted(async () => {
  await initialize();
});

const initialize = async () => {
  await producto();
};

// Sección productos
const filteredProductos = ref([]);
const producto = async () => {
  try {
    const { data } = await api.get("medicamentos/");
    lvProductos.value = data.map(({ codigo, nombre_medicamento }) => ({
      value: codigo,
      label: `${nombre_medicamento}`,
    }));
    filteredProductos.value = lvProductos.value;
  } catch (error) {
    console.warn(error?.response?.data?.message);
  }
};


// Función para filtrar los proveedores basándose en el input del usuario
const filterProducto = (val, update) => {
  if (val === "") {
    update(() => {
      filteredProductos.value = lvProductos.value;
    });
    return;
  }
  update(() => {
    const needle = val.toLowerCase();
    filteredProductos.value = lvProductos.value.filter((provider) =>
      provider.label.toLowerCase().includes(needle)
    );
  });
};


const obtenerIdMedicamento = async () => {
  const { codigo } = form.value;
  if (!codigo) {
    return;
  }
  try {
    const { data } = await api.get(`medicamentos/${form.value.codigo}`);
    if (data) {
      form.value.nombre_medicamento = data.nombre_medicamento;
      form.value.fabricante = data.fabricante;
      form.value.fecha_vencimiento = data.fecha_vencimiento;
      form.value.cantidad = data.cantidad;
      form.value.lote = data.lote;
      form.value.stock = data.stock;
      form.value.precio = data.precio;
    }
  } catch (error) {
    console.warn(error?.response?.data?.message);
  }
};
</script>
