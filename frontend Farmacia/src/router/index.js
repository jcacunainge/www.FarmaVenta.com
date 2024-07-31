import { createRouter, createWebHistory } from "vue-router";
import routes from "./routes";

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem("isAuthenticated") === "true";

  if (to.name !== "login" && to.name !== "registro" && !isAuthenticated) {
    next({ name: "login" });
  } else {
    next();
  }
});

export default router;
