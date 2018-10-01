import Vue from 'vue'
import Router from 'vue-router'
// IQ测试题
import login from '@/components/home/IQ_file'

Vue.use(Router)

export default new Router({
	routes: [
		// 注册与测试
		{
			path: '/questionnaire',
			name: 'questionnaire',
			component: login
		},
		// 重定向
		{
			path: '/',
			redirect: '/questionnaire'
		}
	]
})
