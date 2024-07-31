import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    isAuthenticated: localStorage.getItem("isAuthenticated") === "true",
    user: JSON.parse(localStorage.getItem("user")) || null,
  }),
  actions: {
    login(user) {
      this.isAuthenticated = true;
      this.user = user;
      localStorage.setItem("isAuthenticated", "true");
      localStorage.setItem("user", JSON.stringify(user));
    },
    logout() {
      this.isAuthenticated = false;
      this.user = null;
      localStorage.removeItem("isAuthenticated");
      localStorage.removeItem("user");
    },
    initialize() {
      const storedUser = localStorage.getItem("user");
      if (storedUser) {
        this.user = JSON.parse(storedUser);
        this.isAuthenticated = true;
      }
    },
  },
});
