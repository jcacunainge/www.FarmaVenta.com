<template>
  <q-page padding>
    <div class="row items-center q-gutter-sm q-mb-md">
      <q-breadcrumbs>
        <q-breadcrumbs-el label="Panel Administrativo" />
        <q-breadcrumbs-el label="Pagina de Consulta e Inventario Medicamentos" />
      </q-breadcrumbs>
    </div>
    <q-card>
      <q-card-section class="q-pa-none">
        <q-table :rows="filteredRows" :columns="columnsVisible" dense flat table-header-class="text-weight-bolds"
          no-data-label="No hay datos que mostrar!" class="headerTable" separator="cell" :rows-per-page-options="[100]"
          :hide-pagination="true">
          <template v-slot:top>
            <q-toolbar>
              <q-toolbar-title class="text-light-blue-10 text-h6 gt-xs">
                Consulta e Inventario
              </q-toolbar-title>
              <div class="col-grow flex row justify-end q-gutter-xs">
                <q-input v-model="filter" outlined dense label="Buscar" class="col-xs-12 col-sm-3 col-md-3">
                  <template v-slot:append>
                    <q-icon name="search" />
                  </template>
                </q-input>
                <q-select v-model="visibleColumns" multiple outlined dense options-dense
                  :display-value="$q.lang.table.columns" emit-value map-options :options="columns" option-value="name"
                  class="q-ml-sm col-xs-12 col-sm-3 col-md-3" />
              </div>
            </q-toolbar>
          </template>
        </q-table>
      </q-card-section>
    </q-card>
  </q-page>
</template>


<script setup>
import { ref, onMounted, watch, computed } from "vue";
import { api } from "boot/axios";
import { formatCurrency } from "src/helpers/formatPrecio";
const visibleColumns = ref([
  "codigo",
  "nombre_medicamento",
  "fabricante",
  "fecha_vencimiento",
  "cantidad",
  "lote",
  "stock",
  "precio"
]);

const pagination = ref({
  page: 1,
  rowsPerPage: 10,
});


onMounted(async () => {
  await initialize();
});

const initialize = async () => {
  await producto();
};


const rows = ref([]);
const producto = async () => {
  try {
    const { data } = await api.get("medicamentos/");
    console.log(data)
    rows.value = data
  } catch (error) {
    console.warn(error?.response?.data?.message);
  }
};



const columnsVisible = computed(() => {
  return columns.filter((col) => visibleColumns.value.includes(col.name));
});


const filter = ref("");
const filteredRows = computed(() => {
  const filterText = filter.value.toLowerCase();
  return rows.value.filter((row) => {
    return Object.values(row).some((value) =>
      String(value).toLowerCase().includes(filterText)
    );
  });
});




const columns = [
  {
    name: "codigo",
    align: "left",
    label: "Código",
    field: "codigo",
    sortable: true,
    style: "width: 140px",
  },
  {
    name: "nombre_medicamento",
    align: "left",
    label: "Nombre Medicamentos",
    field: "nombre_medicamento",
    sortable: true,
  },
  {
    name: "fabricante",
    align: "left",
    label: "Fabricante",
    field: "fabricante",
    sortable: true,
  },
  {
    name: "fecha_vencimiento",
    align: "left",
    label: "Fecha Vencimiento",
    field: "fecha_vencimiento",
    sortable: true,
  },

  {
    name: "lote",
    align: "left",
    label: "Lote",
    field: "lote",
    sortable: true,
  },
  {
    name: "stock",
    align: "left",
    label: "Stock",
    field: "stock",
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
    name: "precio",
    align: "right",
    label: "Precio",
    field: "precio",
    sortable: true,
    format: (val) => formatCurrency(val),
  },
];
</script>
