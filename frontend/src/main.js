import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import "./../node_modules/bulma/css/bulma.css";

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  beforeCreate() {
    this.$store.dispatch("initializeToken");
    return;
  },
  render: h => h(App)
}).$mount("#app");
