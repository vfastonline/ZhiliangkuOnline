// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';
import './styles/common.scss'
import _ajaxSubmit from './utils/ajaxSubmit'
import _commmonWebConfig from './utils/config'

Vue.prototype.commmonWebConfig = _commmonWebConfig;
Vue.prototype.ajaxSubmit = _ajaxSubmit;
Vue.use(ElementUI);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
});

Vue.prototype.arrmap = function (arr, i, j) {


  return arr.map(function (value, index) {
    var result = value.slice(4, 6);
    if (result > i && result < j) {
      return value;
    }

  });

};


Vue.prototype.arrmap2 = function (arr) {


  return arr.map(function (value, index) {
    if (value) {
      return value.slice(2, 6) + ':' + value.slice(0, 2);
    }
  })

};


Vue.prototype.arrslice = function (arr) {


  var b = [];
  for (var i = 0; i < arr.length; i++) {
    if (typeof(arr[i]) != 'undefined') {
      b.push(arr[i]);
    }
  }


  return b;

};
