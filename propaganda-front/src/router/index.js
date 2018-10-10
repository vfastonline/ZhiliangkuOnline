import Vue from 'vue'
import Router from 'vue-router'
import questionnaire from "../components/questionnaire/questionnaire.vue"


Vue.use(Router);


export default new Router({
  routes: [
    {
      path: '/questionnaire',
      name: 'questionnaire',
      component: questionnaire
    },
    {
      path: '/',
      redirect: '/questionnaire'
    }
  ]
})
