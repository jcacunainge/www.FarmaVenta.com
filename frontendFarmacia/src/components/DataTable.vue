<template>

  <q-table
    :v-model:pagination="pagination"
    :dense="dense"
    :rows="rows"
    :columns="columns"
    :visible-columns="visibleColumns"
    :filter="filter"
    :rows-per-page-options="[$q.screen.name === 'xl' ? 15 : 10]"
    class="headerTable"
    :separator="borderCell"
    flat
  >

    <template #top="item">
      <q-toolbar>
        <q-toolbar-title class="text-light-blue-10 text-h6 gt-xs">
          {{ title }}
        </q-toolbar-title>
        <div class="col-grow flex row justify-end q-gutter-xs">
          <q-input
            v-model="filter"
            borderless
            outlined
            dense
            solo
            debounce="300"
            color="primary"
            label="Buscar"
            class="col-xs-12 col-sm-3 col-md-3"
          >
            <template #append>
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
            options-cover
            style="min-width: 150px"
            class="q-ml-sm col-xs-12 col-sm-3 col-md-3"
          />
          <q-btn
            round
            dense
            :icon="item.inFullscreen ? 'fullscreen_exit' : 'fullscreen'"
            text-color="primary"
            class="q-ml-sm"
            size="14px"
            @click="item.toggleFullscreen"
          />
          <q-btn
            class="q-ml-sm"
            size="14px"
            color="white"
            text-color="primary"
            round
            dense
            icon="las la-redo-alt"
            @click="onInitialize"
          />
          <q-btn
            color="white"
            text-color="primary"
            round
            dense
            class="q-ml-sm"
            size="14px"
            icon="las la-plus"
            @click="onAddItem"
          />
        </div>
      </q-toolbar>
    </template>
    <template #header="item">
      <q-tr :props="item">
        <q-th v-for="col in item.cols" :key="col.name" :props="item">
          {{ col.label }}
        </q-th>
      </q-tr>
    </template>
    <template #body="item">
      <slot v-bind="item" name="columns"></slot>
    </template>
  </q-table>
</template>

<script setup>
import { ref, defineProps } from "vue";
import { useQuasar } from "quasar";
name: "DataTable";
const $q = useQuasar();
const loadingDt = ref(false);
const props = defineProps({
  title: {
    type: String,
    default: "",
  },
  borderCell: {
    type: String,
    default: "cell",
  },
  rows: {
    type: Object,
    default: () => {},
  },
  columns: {
    type: Object,
    default: () => {},
  },
  dense: {
    type: Boolean,
    required: true,
  },
  pagination: {
    type: Object,
    default: () => {},
  },
  onAddItem: {
    type: Function,
    default: () => {},
    required: false,
  },
  onInitialize: {
    type: Function,
    default: () => {},
    required: false,
  },
});

const filter = ref("");

const visibleColumns = ref(props.columns.map((x) => x.field));
</script>
