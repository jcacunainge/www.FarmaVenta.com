<template>
  <q-page>
    <div v-if="isAuthenticated">
      <h1>Bienvenido, {{ user.nombre_usuario }}</h1>
      <p>Correo: {{ user.correo }}</p>
      <p>Nombre del negocio: {{ user.nombre_negocio }}</p>
      <p>Dirección del negocio: {{ user.direccion_negocio }}</p>
      <p>Teléfono del negocio: {{ user.telefono_negocio }}</p>
      <!-- Contenido protegido -->
    </div>
    <div v-else>
      <p>No estás autenticado. Por favor, inicia sesión.</p>
      <q-btn @click="goToLogin" label="Iniciar Sesión" color="primary" />
    </div>
  </q-page>
</template>

<script setup>
import { computed } from 'vue';
import { useAuthStore } from 'src/stores/authStore';
import { useRouter } from 'vue-router';

const authStore = useAuthStore();
const router = useRouter();

const isAuthenticated = computed(() => authStore.isAuthenticated);
const user = computed(() => authStore.user);

const goToLogin = () => {
  router.push({ name: 'login' });
};
</script>
