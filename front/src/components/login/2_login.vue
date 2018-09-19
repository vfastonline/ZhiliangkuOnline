<template>
	<div class="content">
		<h2 class="titles">密码重置</h2>
		<input type="" name="" placeholder="请输入新密码" class="inp">
		<p>对不起,你输入的密码不符合标准,请重新输入</p>
		<input type="" name="" placeholder="请你再次输入密码">
		<p>密码错误,请重新输入</p>
		<button>提交</button>
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

</style>
<script type="text/javascript">
export default {
	data() {
		return {
			msg: {
				none: true,
				tow: true,
			}
		}
	},
	methods: {

	},
	components: {

	}

}

</script>
</script>
