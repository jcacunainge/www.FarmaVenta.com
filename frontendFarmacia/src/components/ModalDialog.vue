<template>
  <q-dialog v-model="model" persistent>
    <q-card :style="{ width: width, 'max-width': maxWidth }">
      <q-card-section class="row items-center no-wrap">
        <div class="text-light-blue-10 text-h6">{{ title }}</div>
        <q-space />
        <q-btn icon="close" flat round dense @click="onClose" />
      </q-card-section>
      <q-separator />
      <q-form
        ref="form"
        method="post"
        @submit.prevent="onSave"
        @reset="onClose"

      >
        <q-card-section>
          <div class="row q-col-gutter-sm q-col-gutter-y-md q-pa-sm">
            <slot name="body"></slot>
          </div>
        </q-card-section>
        <q-card-actions class="row justify-end">
          <q-btn
            dense
            label="Cerrar"
            type="reset"
            color="red-7"
            style="width: 90px"
          />
          <q-btn
            dense
            label="Guardar"
            type="submit"
            color="blue-10"
            :loading="btnSaveLoading"
            style="width: 90px"
          />
        </q-card-actions>
      </q-form>
    </q-card>
  </q-dialog>
</template>

<script setup>
import { defineProps, computed } from "vue";
const props = defineProps({
  title: {
    type: String,
    default: "",
  },
  width: {
    type: String,
    default: "700px",
  },
  maxWidth: {
    type: String,
    default: "80vw",
  },
  modelValue: {
    type: Boolean,
    required: true,
  },
  btnSaveLoading: {
    type: Boolean,
    default: false,
  },
  onSave: {
    type: Function,
    required: true,
  },
  onClose: {
    type: Function,
    required: true,
  },
});

const model = computed({
  get() {
    return props.modelValue;
  },
  set(newValue) {
    emit("update:modelValue", newValue);
  },
});
</script>
