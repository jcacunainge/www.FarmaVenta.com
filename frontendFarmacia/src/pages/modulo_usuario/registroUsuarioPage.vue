<template>
  <q-page class="flex flex-center">
    <div class="row justify-center items-center">
      <img class="imgFondo col-md-5" src="../../../public/fondo.jpg" alt="">
      <div class="col-md-7 column">
        <div class="text-h6 text-center q-mt-xs">
          FarmaVenta <br>"Ventas rápidas, salud al instante"
        </div>

        <div class="text-center" style="margin: 3rem auto;">
          <div class="row q-gutter-md justify-center">
            <q-input color="blue-12" v-model="formItem.nombre_usuario" label="Nombre Usuario:" outlined type="text"
              class="col-xs-12 col-sm-8 col-md-8">
              <template v-slot:prepend>
                <q-icon name="las la-user" />
              </template>
            </q-input>

            <q-input color="blue-12" v-model="formItem.codigo_usuario" label="Codigo Usuario:" outlined type="text"
              class="col-xs-12 col-sm-8 col-md-8">
              <template v-slot:prepend>
                <q-icon name="las la-address-card" />
              </template>
            </q-input>

            <q-input color="blue-12" v-model="formItem.nombre_negocio" label="Nombre Negocio:" outlined type="text"
              class="col-xs-12 col-sm-8 col-md-8">
              <template v-slot:prepend>
                <q-icon name="las la-home" />
              </template>
            </q-input>

            <q-input color="blue-12" v-model="formItem.dirrecion_negocio" label="Dirreción Negocio:" outlined
              type="text" class="col-xs-12 col-sm-8 col-md-8">
              <template v-slot:prepend>
                <q-icon name="las la-map-marker" />
              </template>
            </q-input>

            <q-input color="blue-12" v-model="formItem.telefono_negocio" label="Telefono Negocio:" outlined type="text"
              class="col-xs-12 col-sm-8 col-md-8">
              <template v-slot:prepend>
                <q-icon name="las la-phone-alt" />
              </template>
            </q-input>

            <q-input color="blue-12" v-model="formItem.correo" label="Correo:" outlined type="email"
              class="col-xs-12 col-sm-8 col-md-8">
              <template v-slot:prepend>
                <q-icon name="email" />
              </template>
            </q-input>

            <q-input v-model="formItem.contraseña" label="Contraseña" outlined :type="isPwd ? 'password' : 'text'"
              color="blue-12" class="col-xs-12 col-sm-8 col-md-8">
              <template v-slot:prepend>
                <q-icon name="las la-lock" />
              </template>
              <template v-slot:append>
                <q-icon :name="isPwd ? 'visibility_off' : 'visibility'" class=" cursor-pointer"
                  @click="isPwd = !isPwd" />
              </template>
            </q-input>

          </div>
          <div class="q-gutter-md q-mt-md">
            <q-btn type="submit" @click="reegistrarUsuario" label="Iniciar Sesión" color="primary" style="width: 180px;"
              flat />
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { useQuasar } from "quasar";
import { ref, onMounted, computed, watch, nextTick } from "vue";
import { api } from "boot/axios";
import { useRules, useNotify } from "src/composables/";
import { useRouter } from 'vue-router'
/* Variables iniciales */
const $q = useQuasar();
const { messageWarning } = useNotify();
const { required } = useRules();

const rules = ref({ required: (value) => required(value) });
const isPwd = ref(true)


const formItem = ref({
  nombre_usuario: "",
  codigo_usuario: "",
  nombre_negocio: "",
  dirrecion_negocio: "",
  telefono_negocio: "",
  contraseña: "",
  correo: ""
});


const router = useRouter()
const reegistrarUsuario = async () => {
  const registrarUsuario = JSON.stringify(formItem.value);
  try {
    console.log(registrarUsuario);
    await api.post("usuario/register", registrarUsuario);
    router.push({ name: 'login' })
  } catch (error) {
    console.log(error)
    messageWarning(error?.response?.data?.message);
  }
};
</script>

<style scoped>
.imgFondo {
  height: 100vh;

}

.flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
