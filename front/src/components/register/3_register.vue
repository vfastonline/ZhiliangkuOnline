<template>
	<div class="content">
		<p class="register">注册</p>
		<div class="entry">
			<input type="" placeholder="请输入班级邀请码" class="inputs">
			<p>说明:此邀请码作为分班依据,请务必认真填写</p>
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
				none: '',
				tow: ''

			}
		}
	}

}

</script>
</script>
