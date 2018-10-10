<template>
  <div>
    <el-button type="text" v-model="isShow" @click="showlDialog" v-show="loginBtn">
      <span>登录</span>
    </el-button>

    <div v-show="username">
      <span class="username">欢迎您 , {{phone}}&nbsp;&nbsp;</span>
      <el-button @click="logout" type="text" class="username">注销</el-button>
      <hr>
    </div>

    <login :invitor="isShow" @changingType="showlDialog" v-on:listenLogin="showPhone"></login>
  </div>

</template>

<script>
  import login from './login.vue'

  export default {
    name: "user_info",
    components: {
      login: login
    },
    created() {
      var reg = /^(\d{3})\d{4}(\d{4})$/;
      this.phone = localStorage.getItem('name');
      if (this.phone) {
        this.phone = this.phone.replace(reg, "$1****$2");
        this.loginBtn = false;
        this.username = true
      }
    },
    data() {
      return {
        isShow: false,
        loginBtn: true,
        username: false,
        phone: "",
      }
    },
    methods: {
      showPhone(phone) {
        this.loginBtn = false;
        this.phone = phone;
        this.username = true
      },
      showlDialog(data) {
        if (data == 'false') {
          this.isShow = false;
        } else {
          this.isShow = true;
        }
      },
      logout() {
        localStorage.clear();
        this.phone = '';
        this.loginBtn = true;
        this.username = false;
      },
    }
  }
</script>

<style scoped>
  .username {
    font-size: 16px;
  }
</style>
