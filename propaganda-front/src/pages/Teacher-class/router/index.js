import Vue from 'vue'
import Router from 'vue-router'
import login from '../views/class/login.vue'
import classList from '../views/class/class.vue'
import search from '../views/class/classPage.vue'
Vue.use(Router);

var router = new Router({
  routes: [
    {
      path:'/login',
      name:'login',
      component:login
    },
    {
      path: '/list',
      name: 'classList',
      component: classList
    },
    {
      path: '/search',
      name: 'search',
      component: search
    },
    {
      path: '/',
      redirect: '/list'
    }
  ]
});


export default router;
