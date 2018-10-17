import Vue from 'vue'
import Router from 'vue-router'

import login from '../views/login/login.vue'

Vue.use(Router);

var router = new Router({
  routes: [
    {
      path: '/login',
      name: 'login',
      component: login
    }
  ]
});


export default router;
