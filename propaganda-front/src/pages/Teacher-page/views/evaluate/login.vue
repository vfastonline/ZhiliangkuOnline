<template>
  <div class="LoginPage">
    <mt-header fixed title="登录"></mt-header>
    <br>
    <br>
    <mt-field label="用户名" placeholder="请输入用户名" v-model="username" type="text"></mt-field>
    <br>
    <mt-field label="密码" placeholder="请输入密码" v-model="password" type="password"></mt-field>
    <mt-button type="primary" @click="submits">登录</mt-button>
  </div>
</template>
<style type="text/css" lang="less" scoped>
</style>

<script type="text/javascript">
// 引入吐司
import { Toast, Button, Field, Header } from 'mint-ui';
import cookie from '../../statics/js/cookie.js';
// 引入接口
import { login } from '../../api/api';
export default {
  name: "login",
  components: {

  },
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    submits() {
      var that = this;
      login({
          username: that.username,
          password: that.password,

        }).then((response) => {
          if (!response.status == 200) {
            Toast('登录失败');
          } else {
            cookie.setCookie('token', response.data.token, 7);
            that.$store.dispatch('setInfo');
            that.$router.push('/Invitation');
          }
        })
        .catch(function(error) {
          Toast('请求错误,请稍后再试');
        })
    },
  }
}

</script>
