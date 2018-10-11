<template>
  <div>
    <el-button type="text" @click="showlLoginDialog" v-if="!userInfo.name">
      <span>登录</span>
    </el-button>

    <div v-if="userInfo.name">
      <span class="username">欢迎您 , {{userInfo.name}}&nbsp;&nbsp;</span>
      <el-button @click="loginOut" type="text" class="username">退出</el-button>
      <hr>
    </div>

    <login></login>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex';
  import login from '../login/login.vue'
  import cookie from '../../static/js/cookie';

  export default {
    name: "loginHead",
    components: {
      login: login
    },
    created() {
    },
    data() {
      return {}
    },

    computed: {
      ...mapGetters({
        userInfo: 'userInfo'
      })
    },
    methods: {
      showlLoginDialog() {
        this.$store.dispatch('setloginDialogOpen', true);
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
