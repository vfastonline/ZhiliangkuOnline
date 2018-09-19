<template>
	<div class="content">
		<h2 class="titles">绑定手机号</h2>
		<input type="" name="" placeholder="请输入你的手机号" class="inp">
		<p>手机号错误,请重新输入</p>
		<div class="msgs">
			<input type="" name="" placeholder="请输入短信验证码">
			<button class="btns">发送验证码</button>
		</div>
		<p>验证码错误,请重新输入</p>
		<button>确定</button>
	</div>
</template>
<style type="text/css" lang="scss" scoped>
  .content {
  	width:600px;
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
