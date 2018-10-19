<template>
  <div class="LoginPage">

    <div class="content">
      <div class="username">
        <label>姓名:</label>
        <input type="" name="" placeholder="请输入你的真实姓名" v-model='username'>
      </div>
      <div class="classData">
        <label>班级:</label>
        <select v-model="ClassData" @change="onchange">
          <option v-for="item in ClassName" v-bind:value="item.text"> {{item.text}}
          </option>
        </select>
      </div>
      <div class="submit">
        <mt-button type="primary" size="small" @click="submit">提交</mt-button>
      </div>
    </div>
  </div>
</template>
<style type="text/css" lang="less" scoped>
.px2px(@name, @px) {
    @{name}: round(@px / 2) * 1px;
    [data-dpr="2"] & {
      @{name}: @px * 1px;
    }
    // for mx3
    [data-dpr="2.5"] & {
      @{name}: round(@px * 2.5 / 2) * 1px;
    }
    // for 小米note
    [data-dpr="2.75"] & {
      @{name}: round(@px * 2.75 / 2) * 1px;
    }
    [data-dpr="3"] & {
      @{name}: round(@px / 2 * 3) * 1px
    }
    // for 三星note4
    [data-dpr="4"] & {
      @{name}: @px * 2px;
    }
  }
  .LoginPage {
    width: 10rem;
    .px2px(font-size, 20px);
    background: #777777;
  }
  .LoginPage .content {
    width: 20rem;
    height: 20rem;
    background: #c0c0c0;
    position: fixed;
    top: 50%;
    left: 50%;
    margin-top: -10rem;
    margin-left: -10rem;

  }
  .LoginPage .content .submit {

  }
  .LoginPage .content .submit .submitData {

  }

</style>
<script>
// 引入吐司
import { Toast, Button } from 'mint-ui';
// 引入接口
import { quickLogin, smsCode } from '../../api/api'
export default {
  name: "login",
  components: {

  },
  data() {
    return {
      username: '',
      ClassData: '',
      ClassName: [
        { text: '请选择你所在的班级', value: '0' },
        { text: '1年级', value: '1' },
        { text: '2年级', value: '2' },
        { text: '3年级', value: '3' }
      ]
    }
  },
  mounted() {
    document.title = "智量酷公众号";
  },
  methods: {
    onchange() {
      console.log(11);
    },
    submit() {
      var self = this;
      if (!self.username) {
        Toast('请输入姓名');
      } else if (!self.ClassData) {
        Toast('请输入班级');
      } else {
        Toast('发送axios');
      }
    }
  },
  created() {
    this.ClassData = this.ClassName[0].text;

    // 发送ajax请求后台班级数据
    // var self = this;
    // smsCode({
    //   // 携带的数据
    //   phone: self.loginForm.mobile,
    // }).then((response) => {
    //   switch (response.status) {
    //     case 201:
    //       self.sendCodeSucNotify();
    //       break;
    //     case 400:
    //       self.sendCodeErrorNotify();
    //       break;
    //     default:
    //       self.sendCodeErrorNotify();
    //   }
    // })
  }
}

</script>
