import Vue from "vue";
import App from "./App.vue";
import store from "./store";
import router from "./router";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

/* import the fontawesome core */
import { library } from "@fortawesome/fontawesome-svg-core";

/* import font awesome icon component */
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

/* import specific icons */
import { faUserSecret } from "@fortawesome/free-solid-svg-icons";

/* add icons to the library */
library.add(faUserSecret);

/* add font awesome icon component */
Vue.component("font-awesome-icon", FontAwesomeIcon);

Vue.config.productionTip = false;

/* eslint-disable no-new */

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

new Vue({
  store,
  router,
  render: (h) => h(App),
}).$mount("#app");
