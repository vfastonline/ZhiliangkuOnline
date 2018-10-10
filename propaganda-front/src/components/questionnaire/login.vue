<template>
  <el-dialog title="登录" :visible.sync="dialogFormVisible" center :before-close="hide">
    <el-form :model="loginForm" status-icon :rules="loginRules" ref="loginForm" label-width="100px">
      <el-form-item label="手机号" prop="mobile">
        <el-input v-model.number="loginForm.mobile" :disabled="disabled"></el-input>
      </el-form-item>
      <el-form-item label="验证码" prop="code">
        <el-input type="tel" v-model="loginForm.code" auto-complete="off"></el-input>
        <el-button type="primary" @click="check_code" :disabled="disabled">
          {{btnContent}}
        </el-button>
      </el-form-item>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button @click="hide(); resetForm('loginForm')">取消</el-button>
      <el-button type="primary" @click="login('loginForm')">登录</el-button>
    </div>
  </el-dialog>
</template>

<script>
  export default {
    name: "login",
    props: ['invitor'],
    watch: {
      invitor(cur) {//监听invitor值的变化
        if (cur == true) {//当父组件传递值为true是，则显示
          this.dialogFormVisible = true;
        } else {
          this.dialogFormVisible = false;
        }
      },
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
        number: 0,
        count_down_time: 0,
        disabled: false,
        dialogFormVisible: false,
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
      hide() {//弹层消失事件
        this.$emit('changingType', 'false');//调用父组件的自定义事件，并传值
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      send_code_error_notify() {
        this.$notify({
          title: '错误',
          message: '验证码发送失败,请输入正确的手机号码'
        });
      },

      send_code_ok_notify() {
        this.$notify({
          title: '成功',
          message: '验证码发送成功',
          type: 'success'
        });
      },

      send_code() {
        var self = this;
        self.ajaxSubmit.ajax({
          url: self.commmonWebConfig.zhiliangkuapi + self.ajaxSubmit.allUrl.message,
          type: "post",
          data: {
            phone: self.loginForm.mobile
          },
          async: false,
          dataType: 'json',
          success: function (data) {
            if (data.Status != 201) {
              self.send_code_ok_notify();
            } else {
              self.send_code_error_notify();
            }
          },
          error: function (data) {
            self.send_code_error_notify();
          }

        })
      },

      count_down() {
        if (this.count_down_time > 0) {
          this.count_down_time--;
          this.btnContent = '重新获取' + '(' + this.count_down_time + 's' + ')';
          setTimeout(this.count_down, 1000);
        } else {
          this.count_down_time = 60;
          this.btnContent = "获取验证码";
          this.disabled = false;
          this.loginForm.mobile = '';
        }
      },

      check_code() {
        var myreg = /^[1][3,4,5,7,8,9][0-9]{9}$/;
        var self = this;
        if (self.loginForm.mobile && myreg.test(self.loginForm.mobile)) {
          self.count_down_time = 60;
          self.disabled = true;
          self.count_down();
          self.send_code();
        } else {
          self.send_code_error_notify();
        }
      },

      login_ok_notify() {
        this.$notify({
          title: '成功',
          message: '登录成功,可以开始答题了.',
          type: 'success'
        });
      },

      login(formData) {
        this.$refs[formData].validate((valid) => {
          if (valid) {
            this.dialogFormVisible = false;
            this.loginBtn = false;
            this.username = true;
            this.login_ok_notify();

            var reg = /^(\d{3})\d{4}(\d{4})$/;
            var self = this;
            self.ajaxSubmit.ajax({
              url: self.commmonWebConfig.zhiliangkuapi + self.ajaxSubmit.allUrl.login,
              type: "post",
              data: {
                mobile: self.loginForm.mobile,
                code: self.loginForm.code,
              },
              async: false,
              dataType: 'json',
              success: function (data) {
                if (data.Status !== 201) {
                  self.token = data.token;
                  self.name = data.name;
                  localStorage.setItem('token', self.token);
                  localStorage.setItem('name', self.name);
                  self.phone = localStorage.getItem('name');
                  if (self.phone) {
                    self.phone = self.phone.replace(reg, "$1****$2");
                  }
                  self.$emit("listenLogin", self.phone)
                }
              },
              error: function (data) {
              }

            })
          } else {
            return false;
          }

        });

      },
    }
  }
</script>

<style scoped>

</style>
