import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/components/HomePage.vue"; 
import RegisterPage from "@/components/RegisterPage.vue"; 
import LoginPage from "@/components/LoginPage.vue";

const routes = [
    { path: "/", component: HomePage }, 
    { path: "/register", component: RegisterPage },
    {path : '/login', component : LoginPage},
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
