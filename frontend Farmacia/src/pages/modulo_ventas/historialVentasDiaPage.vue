<template>
  <q-page padding>
    <div class="row items-center q-gutter-sm q-mb-md">
      <q-breadcrumbs>
        <q-breadcrumbs-el label="Ventas" />
        <q-breadcrumbs-el label="Pagina de Ventas de Medicamentos" />
      </q-breadcrumbs>
    </div>
    <div class="q-pa-md">
      <q-table
        flat
        bordered
        title="Historial de Ventas"
        :rows="filteredRows"
        :columns="columnsVisible"
        row-key="_id"
        class="headerTable"
        dense
      >
        <template v-slot:top>
          <q-toolbar>
            <q-toolbar-title class="text-light-blue-10 text-h6 gt-xs">
              Consulta e Inventario
            </q-toolbar-title>
            <div class="col-grow flex row justify-end q-gutter-xs">
              <q-input
                v-model="filter"
                outlined
                dense
                label="Buscar"
                class="col-xs-12 col-sm-3 col-md-3"
              >
                <template v-slot:append>
                  <q-icon name="search" />
                </template>
              </q-input>
              <q-select
                v-model="visibleColumns"
                multiple
                outlined
                dense
                options-dense
                :display-value="$q.lang.table.columns"
                emit-value
                map-options
                :options="columns"
                option-value="name"
                class="q-ml-sm col-xs-12 col-sm-3 col-md-3"
              />
            </div>
          </q-toolbar>
        </template>

        <template v-slot:header="props">
          <q-tr :props="props">
            <q-th auto-width />
            <q-th v-for="col in props.cols" :key="col.name" :props="props">
              {{ col.label }}
            </q-th>
          </q-tr>
        </template>

        <template v-slot:body="props">
          <q-tr :props="props">
            <q-td auto-width>
              <q-btn
                size="sm"
                color="accent"
                round
                dense
                @click="props.expand = !props.expand"
                :icon="props.expand ? 'remove' : 'add'"
              />
            </q-td>
            <q-td v-for="col in props.cols" :key="col.name" :props="props">
              {{ col.value }}
            </q-td>
          </q-tr>
          <q-tr v-show="props.expand" :props="props">
            <q-td colspan="100%">
              <q-table
                :rows="props.row.itemsVentas"
                :columns="itemColumns"
                flat
                dense
                row-key="codigo"
              >
                <template #body-cell-opciones="props">
                  <q-td :props="props">
                    <q-btn
                      dense
                      flat
                      round
                      color="primary"
                      icon="las la-ellipsis-v"
                    >
                      <q-menu transition-show="scale" transition-hide="scale">
                        <q-list dense>
                          <q-item
                            v-ripple
                            v-close-popup
                            clickable
                            @click="editItem(props.row)"
                          >
                            <q-item-section class="q-mx-sm"
                              >Editar</q-item-section
                            >
                          </q-item>
                          <q-item
                            v-ripple
                            v-close-popup
                            clickable
                            @click="
                              deleteItem(
                                props.row.notdtope,
                                props.row.notdtdoc,
                                props.row.notdnume,
                                props.row.notdcons
                              )
                            "
                          >
                            <q-item-section class="q-mx-sm"
                              >Eliminar</q-item-section
                            >
                          </q-item>
                        </q-list>
                      </q-menu>
                    </q-btn>
                  </q-td>
                </template>
              </q-table>
            </q-td>
          </q-tr>
        </template>
      </q-table>
    </div>
  </q-page>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { api } from "boot/axios";
import { date } from "quasar";

const formatFecha = (val) => {
  return date.formatDate(val, "YYYY-MM-DD");
};

const columns = [
  {
    name: "nombre_cliente",
    label: "Nombre Cliente",
    align: "left",
    field: (row) => row.dataCliente.nombre_cliente,
    sortable: true,
  },
  {
    name: "documento_cliente",
    label: "Documento Cliente",
    align: "left",
    field: (row) => row.dataCliente.documento_cliente,
    sortable: true,
  },
  {
    name: "nombre_usuario",
    label: "Nombre Vendedor",
    align: "left",
    field: (row) => row.dataVendedor.nombre_usuario,
    sortable: true,
  },
  {
    name: "fecha_venta",
    label: "Fecha Venta Medicamentos",
    align: "left",
    field: "fecha_venta",
    sortable: true,
    format: formatFecha,
  },
];

const itemColumns = [
  {
    name: "codigo",
    label: "Codigo Medicamento",
    align: "left",
    field: "codigo",
    sortable: true,
  },
  {
    name: "nombre_medicamento",
    label: "Medicamento",
    align: "left",
    field: "nombre_medicamento",
    sortable: true,
  },

  {
    name: "fabricante",
    label: "Fabricante",
    align: "left",
    field: "fabricante",
    sortable: true,
  },
  {
    name: "fecha_vencimiento",
    label: "Fecha Vencimiento",
    align: "left",
    field: "fecha_vencimiento",
    sortable: true,
  },

  {
    name: "cantidad",
    label: "Cantidad",
    align: "right",
    field: "cantidad",
    sortable: true,
  },
  {
    name: "precio",
    label: "Precio",
    align: "right",
    field: "precio",
    sortable: true,
  },
  {
    name: "total",
    label: "Total Compra",
    align: "right",
    field: "total",
    sortable: true,
  },
  {
    name: "opciones",
    label: "Opciones",
    align: "center",
    field: "opciones",
    sortable: true,
  },
];

const rows = ref([]);

onMounted(async () => {
  await traerDataVentas();
});

const traerDataVentas = async () => {
  try {
    const { data } = await api.get("ventas/");
    console.log(data);
    rows.value = data;
  } catch (error) {
    console.warn(error?.response?.data?.message);
  }
};

const visibleColumns = ref([
  "nombre_cliente",
  "documento_cliente",
  "nombre_usuario",
  "fecha_venta",
]);

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
</script>
