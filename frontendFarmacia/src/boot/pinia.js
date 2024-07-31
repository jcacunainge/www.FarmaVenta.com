import { boot } from "quasar/wrappers";
import { createPinia } from "pinia";
import { useAuthStore } from "src/stores/authStore";

// * Puedes usar esta función para inicializar el store
export default boot(({ app }) => {
  const pinia = createPinia();
  app.use(pinia);

  // Inicializar el store de autenticación
  const authStore = useAuthStore();
  authStore.initialize(); // Inicializa el store con la información almacenada
});
