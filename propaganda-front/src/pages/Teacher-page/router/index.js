import Vue from 'vue'
import Router from 'vue-router'
import Invitation from '../views/evaluate/Classinvitation.vue'
import evaluate from '../views/evaluate/evaluate.vue'
import explain from '../views/evaluate/explain.vue'
import login from '../views/evaluate/login.vue'
Vue.use(Router);

var router = new Router({
  routes: [
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/Invitation',
      name: 'Invitation',
      component: Invitation
    },
    {
      path: '/evaluate',
      name: 'evaluate',
      component: evaluate
    },
    {
      path: '/explain',
      name: 'explain',
      component: explain
    },
    {
      path: '/',
      redirect: '/Invitation'
    }
  ]
});


export default router;
