<template>
  <div class="content">
  <div class="nav">
    <span class="Return" @click="Return"></span>
    <h2>评价成功</h2>
  </div>
  <div class="success_title">
    <p>评价已完成,感谢你的评价</p>
    <p>我们会保护你的隐私,评价内容老师不可见</p>
  </div>
  </div>
    
</template>
<style type="text/css" lang="less" scoped>
 .content {
    width: 10rem;
    margin: 0 auto;
 }
 .content .nav {
    background: #007AFF;
    height: .933333rem;
    position: relative;
    box-sizing: border-box;
  }
 .content .nav .Return {
  background: url('../../assets/返回.png') no-repeat center;
  width: .213333rem;
  height: .346667rem;
  background-size: .213333rem .346667rem;
  position: absolute;
  left: .4rem;
  top: .3rem;
}
.content .nav h2 {
  width: 2.666667rem;
  position: absolute;
  left: 50%;
  margin-left: -.666667rem;
  color: #fff;
  top:50%;
  margin-top: -.28rem;
}
.content .success_title {
   position: relative;
   width: 100%;
   background: #E35555;
}
.content .success_title p {
  line-height: .6rem;
  text-align: center;
  margin-top: .066667rem;
  color:#fff;
  font-size: .4rem;
}
</style>
<script>
// 引入吐司
import { Toast, Button } from 'mint-ui';
export default {
  name: "Success",
  methods: {
    Return() {
      this.$router.push('/evaluate');
    }
  },

  created() {
    var username = JSON.parse(localStorage.getItem('username'));
    var className = JSON.parse(localStorage.getItem('classname'));
    if (username && className) {

    } else {
      // 先注册 上线在开启
      this.$router.push('/Invitation');
    }
  }
}

</script>
