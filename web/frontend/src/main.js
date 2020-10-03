import Vue from "vue";
import App from "./App.vue";
import Vuex from "vuex";
import store from "./vuex/store";
import router from "./routes";
import vuetify from "./plugins/vuetify";

Vue.use(Vuex);

new Vue({
  vuetify,
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
