import { useQuasar } from "quasar";
export const useNotify = () => {
  const $q = useQuasar();

  const messageSuccess = (msg) => {
    $q.notify({
      type: "positive",
      message:
        msg === "add"
          ? "Registro ingresado"
          : msg === "edit"
          ? "Registro actualizado"
          : msg || "Proceso terminado",
      icon: "thumb_up",
    });
  };

  const messageWarning = (msg) => {
    $q.notify({
      type: "negative",
      message: msg || "Failed !",
    });
  };

  const messageInfo = (msg) => {
    $q.notify({
      type: "info",
      message: msg,
    });
  };

  return {
    messageSuccess,
    messageWarning,
    messageInfo,
  };
};
