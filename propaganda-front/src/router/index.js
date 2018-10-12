import Vue from 'vue'
import Router from 'vue-router'

import app from '../views/app/app.vue'; //公共部分
import footer from '../views/footer/footer.vue'
import loginHead from '../views/loginHead/loginHead.vue'
import questionnaire from '../views/questionnaire/questionnaire.vue'

Vue.use(Router);

var router = new Router({
  routes: [
    {
      path: '/app',
      component: app,
      children: [
        {
          path: 'questionnaire',
          name: 'questionnaire',
          components: {
            head: loginHead,
            content: questionnaire,
            footers: footer
          },
          meta: {
            title: '登录',
            need_log: false
          }
        },

      ]
    },
    {path: '/', redirect: '/app/questionnaire'}
  ]
});


export default router;
