<template>
	<div class="content">
		<p class="register">注册</p>
		<div class="entry">
			<input type="" placeholder="请输入6-16位数字或字母,区分大小写,无空格" class="inputs">
			<p v-show="msg.none">对不起,你输入的密码不符合标准,请重新输入</p>
			<div class="boot">
				<input type="" placeholder="请再次输入密码" class="verification">
			</div>
			<p v-show="msg.tow" class="err">对不起,密码不统一,请重新输入</p>
		</div>
		<h2>下一步</h2>
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
	width: 400px;
	height: 35px;
}

.content .entry .boot {
	margin-top: 10px;
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

</style>
<script type="text/javascript">
// 引入底部组件
export default {
	data() {
		return {
			msg: {
				none: true,
				tow: true,

			}
		}
	}

}

</script>
</script>
