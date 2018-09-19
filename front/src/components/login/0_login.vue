<template>
	<div>
		<div class="content" v-if="shows">
			<div class="login">
				<span :class="[log]" @click="button_noe">密码登录</span>
				<span :class="[masge]" @click="button_tow">短信登录</span>
			</div>
			<!-- 密码登录 -->
			<div v-if="show">
				<div class="inputs">
					<div class="tops">
						<input type="tel" maxlength="11" placeholder="请输入你的手机号码">
						<p v-show="msg.none">手机号错误,请重新输入</p>
					</div>
					<div class="boots">
						<input type="" placeholder="请输入密码">
						<p v-show="msg.tow">密码错误,请重新输入</p>
					</div>
				</div>
				<div>
					<div>
						<input type="checkbox" name="">
						<span>7天自动登录</span>
					</div>
					<span>忘记密码</span>
				</div>
				<div class="entry">
					<button>登录</button>
				</div>
			</div>
			<!-- 短信登录 -->
			<div v-if="diply">
				<div class="inputs">
					<div class="tops">
						<input type="tel" maxlength="11" placeholder="请输入你的手机号码">
						<p v-show="msg.none">手机号错误,请重新输入</p>
					</div>
					<div class="boots">
						<input type="" placeholder="请输入密码">
						<button>发送验证码</button>
						<p v-show="msg.tow">验证码错误,请重新输入</p>
					</div>
				</div>
				<div>
					<span>忘记密码</span>
				</div>
				<div class="entry">
					<button @click="bth">登录</button>
				</div>
			</div>
			<Nav class="foot"></Nav>
		</div>
		<!-- 绑定手机号码 -->
		<Binding v-if="Bind"></Binding>	
	</div>
</template>
<style type="text/css" lang="less" scoped>
.content {
	width: 600px;
	border: 1px solid #bbbbbb;
	margin: 0 auto;
	padding-top: 20px;
	background: #EEE;
}

.content .login {
	width: 400px;
	height: 40px;
	font-size: 20px;
	color: #ffffff;
	margin: 0 auto;
}

.content .login span {
	float: left;
	width: 50%;
	background: #68dfd6;
}

.content .login .log_password {
	background: #68dfd6;
}

.content .login .masge_password {
	background: #bbbbbb;
}

.content .foot {
	margin: 0 auto;
	background: #eee;
}

</style>
<script type="text/javascript">
// 引入底部组件
import Nav from "@/components/register/2_register"
// 引入绑定手机组件
import Binding from "@/components/login/1_login"
export default {
	data() {
		return {
			msg: {
				none: true,
				tow: true,
			},
			show: true,
			log: 'log_password',
			masge: 'masge_password',
			diply: false,
			shows: true,
			Bind: false
		}
	},
	methods: {
		button_noe() {
			this.show = true;
			this.diply = false;
			this.log = 'log_password';
			this.masge = 'masge_password';
		},
		button_tow() {
			this.show = false;
			this.log = 'masge_password';
			this.masge = 'log_password';
			this.diply = true;
		},
		bth() {
            // 这个地方要做判断
			this.Bind = true;
			this.shows = false;
		}
	},
	components: {
		Nav: Nav,
		Binding: Binding
	}

}

</script>
</script>
