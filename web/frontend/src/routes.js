import Vue from "vue";
import Router from "vue-router";
import main from "./views/content/main";
import login from "./views/login";
import signUp from "./views/signUp";
import myInformation from "./views/myInformation";
import leave from "./views/leave";
import result from "./views/content/Result";
import search from "./views/content/search";
import detail from "./views/content/detail";
import NotFound from "./views/NotFound";
// import store from "./vuex/store";

Vue.use(Router);

const router = new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "main",
      component: main,
    },

    {
      path: "/login",
      name: "login",
      component: login,
    },

    {
      path: "/signUp",
      name: "signUp",
      component: signUp,
    },

    {
      path: "/myInformation",
      name: "myInformation",
      component: myInformation,
    },

    {
      path: "/leave",
      name: "leave",
      component: leave,
    },

    {
      path: "/result",
      name: "result",
      component: result,
    },

    {
      path: "/search",
      name: "search",
      component: search,
    },

    {
      path: "/detail",
      name: "detail",
      component: detail,
    },

    {
      path: "/MyPage",
      name: "Mypage",
      component: () => import("@/views/content/MyPage.vue"),
    },

    {
      path: "*",
      redirect: "/404",
    },
    {
      path: "/404",
      name: "NotFound",
      component: NotFound,
    },
  ],
});


export default router;
