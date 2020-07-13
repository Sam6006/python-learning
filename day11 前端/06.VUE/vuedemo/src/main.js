// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import settings from "./settings";
import router from "./routes/index";
import axios from 'axios'; /*导入axios包*/
import store from "./store";

Vue.config.productionTip = false;
Vue.prototype.$settings = settings;
Vue.prototype.$axios = axios;  /*把axios挂载到vue中*/


//注册elementUi
import ElementUI from 'element-ui';
import 'element-ui/lib/index';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
});
