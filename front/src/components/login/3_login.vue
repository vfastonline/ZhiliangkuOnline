<template>
	<div>
		<div class="content" v-if="heding">
			<h2 class="titles">密码重置</h2>
			<input type="" name="" placeholder="请输入你的手机号" class="inp">
			<p>手机号码有误,重新输入</p>
			<div>
				<input type="" name="" placeholder="请输入验证码">
				<img src="" class="imgs">
				<p>验证码错误,请重新输入</p>
			</div>
			<div>
				<input type="" name="" placeholder="请输入短信验证码">
				<button>发送验证码</button>
			</div>
			<button @click="show">下一步</button>
		</div>
		<!-- 密码重置组件 -->
		<Reset v-if="rese"></Reset>
	</div>
</template>
<style type="text/css" lang="scss" scoped>
.content {
	width: 600px;
	border: 1px solid #eee;
	margin: 0 auto;
	background: #eee;
}

.content .titles {
	margin: 0 auto;
	width: 300px;
	height: 40px;
	background: #68dfd6;
	line-height: 40px;
	color: #fff;
	font-size: 20px;
}

.imgs {
	width: 50px;
	height: 20px;
	border: 1px solid blue;
	position: relative;
	top: 5px;
}

</style>
<script type="text/javascript">
// 引入密码重置组件
import Reset from "@/components/login/2_login"

export default {
	data() {
		return {
			msg: {
				none: true,
				tow: true,
			},
			heding: true,
			rese: false
		}
	},
	methods: {
		show() {
			this.heding = false;
			this.rese = true;
		}
	},
	components: {
		Reset
	}

}

</script>
</script>
