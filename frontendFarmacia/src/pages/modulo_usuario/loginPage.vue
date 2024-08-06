<template>
  <q-page>
    <div class="row">
      <img class="imgFondo col-md-5" src="../../../public/fondo.jpg" alt="">
      <div class="col-md-7 column">
        <div class="text-h6 text-center q-mt-xl"> FarmaVenta <br>"Ventas rápidas, Salud al instante"</div>
        <div style="margin: 3rem auto;">
          <div class="row q-gutter-md">
            <q-input color="blue-12" v-model="correo" label="Correo" outlined type="email"
              class="col-xs-12 col-sm-12 col-md-11">
              <template v-slot:prepend>
                <q-icon name="email" />
              </template>
            </q-input>
            <q-input v-model="contraseña" label="Contraseña" outlined :type="isPwd ? 'password' : 'text'"
              color="blue-12" class=" col-xs-12 col-sm-12 col-md-11">
              <template v-slot:append>
                <q-icon :name="isPwd ? 'visibility_off' : 'visibility'" class="cursor-pointer"
                  @click="isPwd = !isPwd" />
              </template>
            </q-input>
          </div>
          <div class="q-gutter-md q-mt-md q-ml-xs">
            <q-btn @click="login" label="Iniciar Sesión" color="primary" style="width: 180px;" flat />
            <q-btn color="primary" style="width: 180px;" flat>
              <router-link :to="{ name: 'registro' }" style="text-decoration: none; color: inherit;">
                Registrar Usuario
              </router-link>
            </q-btn>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue';
import { api } from 'boot/axios';
import { useRouter } from 'vue-router';
import { useAuthStore } from 'src/stores/authStore';
import { useNotify } from 'src/composables/';

const authStore = useAuthStore();
const router = useRouter();
const { messageSuccess, messageWarning } = useNotify();

const correo = ref('');
const isPwd = ref(true);
const contraseña = ref('');

const login = async () => {
  try {
    const response = await api.post('usuario/login', {
      correo: correo.value,
      contraseña: contraseña.value,
    });
    if (response.data && response.data.mensaje === 'Inicio de sesión exitoso') {
      authStore.login(response.data.usuario);
      messageSuccess(response.data.mensaje);
      router.push({ name: 'control-ventas' });
    } else {
      messageWarning(response.data.mensaje || 'Error desconocido');
    }
  } catch (error) {
    messageWarning(error.response?.data?.detail);
  }
};

</script>

<style scoped>
.imgFondo {
  height: 100vh;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
