import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
// 注册测试的路由
import Login from '@/components/register/0_register'
import Log from '@/components/register/1_register'
import Lo from '@/components/register/2_register'
import Los from '@/components/register/3_register'
// 登录测试的路由
import Plogin from '@/components/login/0_login'
import Plog   from '@/components/login/1_login'
import Plo  from '@/components/login/2_login'
import Plos  from '@/components/login/3_login'
// 首页头部测试的路由
import Header from '@/components/home/heder'

// 引入问卷调查
// import Header from '@/components/question'

Vue.use(Router)

export default new Router({
	routes: [{
			path: '/login',
			name: 'login',
			component: Login
		},
		{
			path: '/log',
			name: 'log',
			component: Log
		},
		{
			path: '/lo',
			name: 'lo',
			component: Lo
		},
		{
			path: '/los',
			name: 'los',
			component: Los
		},
		{
			path: '/plogin',
			name: 'plogin',
			component: Plogin
		},
		{
			path: '/Plog',
			name: 'Plog',
			component: Plog
		},
		{
			path: '/Plo',
			name: 'Plo',
			component: Plo
		},
		{
			path: '/Plos',
			name: 'Plos',
			component: Plos
		},
		{
			path: '/header',
			name: 'header',
			component: Header
		}

	]
})
