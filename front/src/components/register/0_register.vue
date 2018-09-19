<template>
	<div class="content">
		<p class="register">注册</p>
		<div class="entry">
			<input type="tel" maxlength="11" placeholder="请输入你的手机号码" class="inputs">
			<p v-show="msg.none">请输入正确的手机号码/你的手机号码已注册,请重新输入</p>
			<div class="boot">
				<input type="" placeholder="请输入短信验证码" class="verification">
				<button>发送验证码</button>
			</div>
			<p v-show="msg.tow" class="err">验证码错误,请重新输入</p>
			<div class="check">
				<input type="checkbox" name=""><span>同意智量酷注册协议</span>
			</div>
			<p v-show="msg.trow" class="erro">请同意注册协议</p>
		</div>
		<h2>下一步</h2>
		<!-- 注册组件 -->
		<Nav class="foot"></Nav>
	</div>
</template>
<style type="text/css" lang="less" scoped>
* {
	padding: 0;
	margin: 0;
}

.content {
	width: 600px;
	border: 1px solid #bbbbbb;
	margin: 0 auto;
	padding-top: 20px;
	background: #EEE;
}

.content .register {
	width: 400px;
	height: 45px;
	line-height: 40px;
	color: #FFF;
	background: #68dfd6;
	text-align: center;
	margin: 0 auto;
	margin-bottom: 10px;
	font-size: 20px;
	font-weight: bold;
}

.content .entry .inputs {
	width: 400px;
	height: 35px;
}

.content .entry p {
	color: red;
}

.content .entry .err {
	position: relative;
	left: -115px;
}

.content .entry .check {
	width: 405px;
	height: 40px;
	line-height: 40px;
	margin: auto;
	position: relative;
	left: -126px;
}

.content .entry .verification {
	width: 298px;
	height: 35px;
}

.content .entry .boot {
	margin-top: 10px;
}

.content .entry button {

	width: 100px;
	height: 38px;
	margin: 0;
	padding: 0;
	border: 1px solid transparent; //自定义边框
	outline: none;
	border: 1px solid #bbb;
	background: #fff;
}

.content h2 {
	width: 200px;
	height: 45px;
	line-height: 45px;
	background: #68dfd6;
	font-size: 20px;
	color: #FFFFFF;
	text-align: center;
	margin: 0 auto;
}
.content .foot {
	margin: 0 auto;
	background: #eee;
}

</style>
<script type="text/javascript">
// 引入底部组件
import Nav from "@/components/register/2_register"
export default {
	data() {
		return {
			msg: {
				none: false,
				tow: false,
				trow: false
			}
		}
	},
	components: {
		Nav: Nav
	}

}

</script>
</script>
