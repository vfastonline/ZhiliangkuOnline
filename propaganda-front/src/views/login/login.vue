<template>
  <el-dialog title="登录" :visible.sync='dialogFormVisible' center :before-close="hidenLoginDialog">

    <el-form :model="loginForm" status-icon :rules="loginRules" ref="loginForm" label-width="100px"
             class="demo-ruleForm">

      <el-form-item label="手机号" prop="mobile">
        <el-input type="tel" v-model.number="loginForm.mobile" :disabled="disabled"></el-input>
      </el-form-item>

      <el-form-item label="验证码" prop="code">
        <el-input type="text" v-model="loginForm.code"></el-input>
        <el-button type="primary" @click="checkMobile" :disabled="disabled">
          {{btnContent}}
        </el-button>
      </el-form-item>

    </el-form>

    <div slot="footer" class="dialog-footer">
      <el-button @click="hidenLoginDialog">取消</el-button>
      <el-button type="primary" @click="login">登录</el-button>
    </div>

  </el-dialog>
</template>

<script>
  import {quickLogin, smsCode} from '../../api/api'
  import cookie from '../../static/js/cookie';

  export default {
    name: "login",
    created() {
      // cookie.delCookie('token');
      // cookie.delCookie('name');
      // this.$store.dispatch('setInfo');
    },
    computed: {
      dialogFormVisible: function () {
        return this.$store.state.loginDialogOpen
      }
    },

    data() {
      var checkNum = (rule, value, callback) => {
        if (!value) {
          return callback(new Error('手机号必填'));
        }
        setTimeout(() => {
          if (!Number.isInteger(value)) {
            callback(new Error('请输入数字值'));
          } else {
            var myreg = /^[1][3,4,5,7,8,9][0-9]{9}$/;
            if (!myreg.test(value)) {
              callback(new Error('请输入正确的手机号码'));
            } else {
              callback();
            }

          }
        }, 1000);
      };

      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入短信验证码'));
        } else {
          callback();
        }
      };

      return {
        loginDialogOpen: false,
        number: 0,
        count_down_time: 0,
        disabled: false,
        btnContent: '获取验证码',
        loginRules: {
          code: [
            {validator: validatePass, trigger: 'blur'}
          ],
          mobile: [
            {validator: checkNum, trigger: 'blur'}
          ]
        },
        loginForm: {
          code: '',
          mobile: '',
        },
      }
    },
    methods: {
      hidenLoginDialog() {
        this.$refs["loginForm"].resetFields();
        this.$store.dispatch('setloginDialogStatus', false)
      },

      sendCodeErrorNotify() {
        this.$notify({
          title: '错误',
          message: '验证码发送失败,请输入正确的手机号码'
        });
      },

      sendCodeSucNotify() {
        this.$notify({
          title: '成功',
          message: '验证码发送成功',
          type: 'success'
        });
      },

      sendCode() {
        var self = this;
        smsCode({
          phone: self.loginForm.mobile,
        }).then((response) => {
          switch (response.status) {
            case 201:
              self.sendCodeSucNotify();
              break;
            case 400:
              self.sendCodeErrorNotify();
              break;
            default:
              self.sendCodeErrorNotify();
          }
        })
      },

      countDown() {
        if (this.count_down_time > 0) {
          this.count_down_time--;
          this.btnContent = '重新获取' + '(' + this.count_down_time + 's' + ')';
          setTimeout(this.countDown, 1000);
        } else {
          this.count_down_time = 60;
          this.btnContent = "获取验证码";
          this.disabled = false;
          this.loginForm.mobile = '';
        }
      },

      checkMobile() {
        var regMobile = /^[1][3,4,5,7,8,9][0-9]{9}$/;
        var self = this;
        if (self.loginForm.mobile && regMobile.test(self.loginForm.mobile)) {
          self.count_down_time = 60;
          self.disabled = true;
          self.countDown();
          self.sendCode();
        } else {
          self.sendCodeErrorNotify();
        }
      },

      loginSucNotify() {
        this.$notify({
          title: '成功',
          message: '登录成功,可以开始答题了.',
          type: 'success'
        });
      },

      login() {
        var that = this;
        that.$refs["loginForm"].validate((valid) => {
          if (valid) {
            quickLogin({
              mobile: this.loginForm.mobile,
              code: this.loginForm.code,
            }).then((response) => {
              cookie.setCookie('name', response.data.name, 7);
              cookie.setCookie('token', response.data.token, 7);
              that.$store.dispatch('setInfo');
              this.hidenLoginDialog()
            })
              .catch(function (error) {
                if ("non_field_errors" in error) {
                  // console.log(error.non_field_errors[0])
                  // that.error = error.non_field_errors[0];
                }
                if ("mobile" in error) {
                  // console.log(error.mobile[0])
                  // that.userNameError = error.mobile[0];
                }
                if ("code" in error) {
                  // console.log(error.code[0])
                  // that.parseWordError = error.code[0];
                }
              });
          }
        })
      },
    }
  }
</script>

<style scoped>

</style>
