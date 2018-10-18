import Vue from 'vue'
import Router from 'vue-router'
import evaluate from '../views/evaluate/evaluate.vue'
import explain from '../views/evaluate/explain.vue'
Vue.use(Router);

var router = new Router({
  routes: [
    {
      path: '/evaluate',
      name: 'evaluate',
      component: evaluate
    },
    {
      path: '/explain',
      name: 'explain',
      component: explain
    }
  ]
});


export default router;
