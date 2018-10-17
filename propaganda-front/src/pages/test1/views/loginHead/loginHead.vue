<template>
  <div>
    <el-button type="text" @click="showLoginDialog" v-if="!username">
      <span>登录</span>
    </el-button>
    <div v-if="username">
      <span class="username">欢迎您 , {{username}}&nbsp;&nbsp;</span>
      <el-button @click="loginOut" type="text" class="username">退出</el-button>
      <hr>
    </div>
    <login></login>
  </div>
</template>
<script>
import login from '../login/login.vue'
import cookie from '../../static/js/cookie';

export default {
  name: "loginHead",
  components: {
    login: login
  },
  computed: {
    username: function() {
      var name = this.$store.state.userInfo.name;
      var reg = /^(\d{3})\d{4}(\d{4})$/;
      if (name) {
        return name.replace(reg, "$1****$2")
      }
      return "";
    }
  },
  created() {},
  data() {
    return {}
  },
  methods: {
    showLoginDialog() {
      this.$store.dispatch('setLoginDialogStatus', true);
    },
    loginOut() {
      cookie.delCookie('token');
      cookie.delCookie('name');
      this.$store.dispatch('setInfo');
    },
  }
}

</script>
<style scoped>
.username {
  font-size: 16px;
}

</style>
