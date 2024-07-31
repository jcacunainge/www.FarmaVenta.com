import RouterTab from "vue-router-tab";
import { boot } from "quasar/wrappers";
import "vue-router-tab/dist/lib/vue-router-tab.css";

export default boot(({ app }) => {
  app.use(RouterTab);
});
