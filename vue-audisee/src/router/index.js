import Vue from "vue";
import VueRouter from "vue-router";
import SearchView from "@/views/SearchView";
import HomeView from "@/views/HomeView";
import LoginView from "@/views/LoginView";
import MembersView from "@/views/MembersView";
import PlaylistView from "@/views/PlaylistView";
import ProfileView from "@/views/ProfileView";
import RecommendView from "@/views/RecommendView";
import SignupView from "@/views/SignupView";

Vue.use(VueRouter);

const routes = [
  {
    path: "/search",
    name: "SearchView",
    component: SearchView,
  },
  {
    path: "/home",
    name: "HomeView",
    component: HomeView,
  },
  {
    path: "/login",
    name: "LoginView",
    component: LoginView,
  },
  {
    path: "/members",
    name: "MembersView",
    component: MembersView,
  },
  {
    path: "/playlist",
    name: "PlaylistView",
    component: PlaylistView,
  },
  {
    path: "/profile",
    name: "ProfileView",
    component: ProfileView,
  },
  {
    path: "/recommend",
    name: "RecommendView",
    component: RecommendView,
  },
  {
    path: "/signup",
    name: "SignupView",
    component: SignupView,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
