import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/components/HomePage.vue";
import CreateNanny from "@/components/CreateNanny.vue";

const routes = [
  { path: "/", component: HomePage },
  { path: "/be-nanny", component: CreateNanny },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
