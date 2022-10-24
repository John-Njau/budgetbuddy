import Vue from "vue";
import Buefy from "buefy";
import axios from "axios";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import "buefy/dist/buefy.css";
import "bulma/css/bulma.css";

Vue.config.productionTip = false;
Vue.use(Buefy);

axios.defaults.baseURL = "http://localhost:8000";

new Vue({
  router,
  store,
  axios,
  render: (h) => h(App),
}).$mount("#app");
