import Vue from "vue";
import VueRouter from "vue-router";
import SearchView from "@/views/SearchView";

Vue.use(VueRouter);

const routes = [
  {
    path: "/search",
    name: "SearchView",
    component: SearchView,
  },

  // {
  //   path: '/',
  //   name: 'home',
  //   component: HomeView
  // },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
