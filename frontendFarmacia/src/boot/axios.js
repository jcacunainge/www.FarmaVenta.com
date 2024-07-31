import { boot } from "quasar/wrappers";
import axios from "axios";
import { useValidationError } from "src/composables/";
import { Loading, Notify } from "quasar";
// Be careful when using SSR for cross-request state pollution
// due to creating a Singleton instance here;
// If any client changes this (global) instance, it might be a
// good idea to move this instance creation inside of the
// "export default () => {}" function below (which runs individually
// for each client)
const axiosConfig = {
  baseURL: process.env.API_URL,
};
const api = axios.create(axiosConfig);
api.interceptors.request.use(
  async (config) => {
    config.headers = {
      //'Authorization': `Bearer ${token}`,
      "x-api-key": `WNeIcvhoxPJMEDcHhbVKS9OV3WfDh4V2`,
      Accept: "application/json",
      "Content-Type": "application/json",
    };
    Loading.show({
      delay: 500,
      message: "Espere por favor...",
    });
    return config;
  },
  (error) => {
    Promise.reject(error);
  }
);

api.interceptors.response.use(
  (response) => {
    Loading.hide();
    return response;
  },
  (error) => {
    if (!!useValidationError(error.code)) {
      Notify.create({
        type: "negative",
        message: useValidationError(error.code),
      });
    } else {
      Loading.hide();
    }

    return Promise.reject(error);
  }
);

export default boot(({ app }) => {
  // for use inside Vue files (Options API) through this.$axios and this.$api

  app.config.globalProperties.$axios = axios;
  // ^ ^ ^ this will allow you to use this.$axios (for Vue Options API form)
  //       so you won't necessarily have to import axios in each vue file

  app.config.globalProperties.$api = api;
  // ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
  //       so you can easily perform requests against your app's API
  app.provide("axios", app.config.globalProperties.$axios);
});

export { axios, api };
