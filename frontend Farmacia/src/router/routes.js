const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: "control-ventas",
        name: "control-ventas",
        component: () => import("../pages/modulo_ventas/paginaVentasPage.vue"),
      },
      {
        path: "historial-ventas-dia",
        name: "historial-ventas-dia",
        component: () =>
          import("../pages/modulo_ventas/historialVentasDiaPage.vue"),
      },

      {
        path: "panel-administrativo-ingreso-medicamento",
        name: "panel-administrativo-ingreso-medicamento",
        component: () =>
          import("../pages/modulo_Administrativo/ingresoMedicamentoPage.vue"),
      },

      {
        path: "panel-administrativo-consulta-medicamentos",
        name: "panel-administrativo-consulta-medicamentos",
        component: () =>
          import("../pages/modulo_Administrativo/invetarioMedicamentoPage.vue"),
      },
    ],
  },
  {
    name: "login",
    path: "/login",
    component: () => import("pages/modulo_usuario/loginPage.vue"),
  },
  {
    name: "registro",
    path: "/registro",
    component: () => import("pages/modulo_usuario/registroUsuarioPage.vue"),
  },

  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
