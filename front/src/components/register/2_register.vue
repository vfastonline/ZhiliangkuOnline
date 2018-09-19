<template>
	<div class="cont">
		<p class="title">其他方式登录</p>
		<ul class="list">
			<li @click="weixin">微信</li>
			<li @click="weibo">微博</li>
			<li @click="qq">QQ</li>
		</ul>
	</div>
</template>
<style type="text/css" lang="less" scoped>
* {
	padding: 0;
	margin: 0;
	list-style: none;
}

.cont {
	width: 500px;
	height: 100px;
	background: pink;
}

.cont .list {
	position: relative;
	left: 100px;
	width: 500px;
	overflow: hidden;
}

.cont .list li {
	float: left;
	width: 50px;
	height: 50px;
	border: 1px solid #8e8e8e;
	text-align: center;
	line-height: 50px;
	border-radius: 100%;
	background: #8e8e8e;
	color: #FFF;
	margin-left: 40px;
}

.cont .title {
	position: relative;
	left: -200px;
	top: 35px;
}

</style>
<script type="text/javascript">
export default {
	data() {
		return {
			msg: {

			}
		}
	},
	methods: {
		weixin(){
			console.log(111);
		},
		weibo(){
			console.log(222);
		},
        qq(){
        	console.log(333);
        }
	}

}

</script>
</script>
