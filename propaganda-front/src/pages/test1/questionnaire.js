// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import './styles/common.scss'
import router from './router'
import store from './store/store';
//全局加载resource拦截器
import './axios/';
import Axios from 'axios';
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';

Vue.prototype.$http = Axios;


Vue.use(ElementUI);

Vue.config.productionTip = false;

//创建全局实例
new Vue({
  el: '#app',
  router,
  store,
  components: {App},
  template: '<App/>'
});

