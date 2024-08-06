<template>
  <q-layout view="hHh lpR lFr">
    <q-header :elevated="!$q.dark.isActive" style="background: linear-gradient(to right, #154280, #154280, #0e9452)">
      <q-toolbar>

        <q-separator dark vertical inset />
        <!-- <div class="q-ml-sm">
          <img src="../assets/logo-gecelca-white.svg" style="height: 40px" />
        </div> -->

        <q-toolbar-title class="">{{ user.nombre_negocio }}
        </q-toolbar-title>

        <q-btn flat :icon="$q.fullscreen.isActive ? 'las la-compress' : 'las la-expand'"
          @click="$q.fullscreen.toggle()" />
        <!-- <q-btn flat round dense icon="las la-bell" class="q-mr-xs" @click="rightDrawerOpen = !rightDrawerOpen" /> -->
        <q-btn flat round dense icon="las la-user">
          <q-menu>
            <div class="row no-wrap q-pa-md">
              <div class="column">
                <div class="text-h6 q-mb-md">Perfil</div>

                <q-toggle v-model="darkMode" label="Modo Oscuro" color="green" checked-icon="las la-moon"
                  unchecked-icon="las la-sun" size="lg" />
              </div>

              <q-separator vertical inset class="q-mx-lg" />

              <div class="column items-center">
                <q-avatar size="70px">
                  <q-icon name="las la-user-circle" style="color: #ccc; font-size: 2em" />
                </q-avatar>
                <div class="text-subtitle2 text-center q-mt-md q-mb-xs">
                  {{ user.nombre_usuario }}
                </div>

                <q-btn v-close-popup color="primary" label="Logout" @click="logout()" push size="sm" />
              </div>
            </div>
          </q-menu>
        </q-btn>
      </q-toolbar>
    </q-header>

    <!-- Menu de opciones (Main) -->
    <q-drawer v-model="leftDrawerOpen" show-if-above :width="250" :breakpoint="400" style="border-right: 1px solid #ddd"
      :mini="!leftDrawerOpen || miniState" @click.capture="drawerClick">

      <q-scroll-area style="height: calc(90% - 100px); margin-top: 0px">
        <!-- menu -->
        <q-list padding class="q-mt-lg">
          <q-expansion-item label="Panel Administrativo" expand-icon="las la-angle-right" icon="las la-users"
            group="menu">
            <q-list>
              <q-item clickable v-ripple v-for="nav in menuAdministrativo" :key="nav.titulo" :to="nav.path">
                <q-item-section>{{ nav.titulo }}</q-item-section>
              </q-item></q-list>
          </q-expansion-item>
          <q-expansion-item label="Ventas" expand-icon="las la-angle-right" icon="las la-hand-holding-usd" group="menu">
            <q-list>
              <q-item clickable v-ripple v-for="nav in menuVentas" :key="nav.titulo" :to="nav.path">
                <q-item-section>{{ nav.titulo }}</q-item-section>
              </q-item></q-list>
          </q-expansion-item>
        </q-list>

        <!-- ./menu -->
      </q-scroll-area>
      <div class="q-mini-drawer-hide absolute" style="top: 10px; right: -8px">
        <q-btn dense round size="9px" unelevated color="indigo-10" icon="las la-angle-left" @click="miniState = true" />
      </div>
    </q-drawer>

    <q-drawer v-model="rightDrawerOpen" side="right" bordered>
      <!-- drawer content -->
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref, watch, onMounted, computed } from "vue";
import { useQuasar } from "quasar";
import { useRouter } from 'vue-router';
import { useNotify } from "src/composables/";
import { useAuthStore } from 'src/stores/authStore';

const router = useRouter();
const { messageSuccess } = useNotify();
const authStore = useAuthStore();

const user = computed(() => authStore.user);

const $q = useQuasar();
const leftDrawerOpen = ref(false);
const rightDrawerOpen = ref(false);
const darkMode = ref(false);
const miniState = ref(false);


const menuVentas = [
  {
    titulo: "Control de Ventas",
    path: "control-ventas",
  },
  {
    titulo: "Historial Ventas Dia",
    path: "historial-ventas-dia",
  },
];

const menuAdministrativo = [
  {
    titulo: "Ingreso Medicamentos",
    path: "panel-administrativo-ingreso-medicamento",
  },
  {
    titulo: "Consulta Inventario de Medicamentos",
    path: "panel-administrativo-consulta-medicamentos",
  },

];

watch(darkMode, (darkMode) => {
  $q.dark.set(darkMode);
  $q.localStorage.set("darkMode", darkMode);
});

/* Segun el tamaño del dipositivo se oculta el menu sidebar */
watch(
  (miniState) => $q.screen.name,
  (val) => {
    miniState.value = val === "xs" ? true : val === "sm" ? true : false;
  }
);

onMounted(() => {
  const darkModeIsActive = $q.localStorage.getItem("darkMode");
  if (darkModeIsActive) {
    darkMode.value = true;
  }
});

const drawerClick = (e) => {
  if (miniState.value) {
    miniState.value = false;
    e.stopPropagation();
  }
}

// const logout = () => {
//   localStorage.removeItem('isAuthenticated'); // Eliminar estado de autenticación
//   messageSuccess("Has cerrado sesión con éxito");
//   router.push({ name: 'login' }); // Redirigir a la página de inicio de sesión
// };

const logout = () => {
  authStore.logout();
  messageSuccess("¡Has cerrado sesión con éxito! 🍍");
  router.push({ name: 'login' });
};

</script>
<style>
.q-drawer-container:nth-child(1)>.q-drawer--left {
  margin-left: 0px !important;
  background: transparent;
}

.q-drawer-container:nth-child(2)>.q-drawer--left {
  margin-left: 0px !important;
  background: transparent;
}
</style>
