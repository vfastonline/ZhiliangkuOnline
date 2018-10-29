<template>
  <div class="LoginPage">
    <span class="icon" @click="event"></span>
    <h3>智量酷</h3>
    <div class="content">
      <div class="username">
        <label>姓名:</label>
        <input type="text" placeholder="请输入你的真实姓名" v-model='username' class="User_input">
      </div>
      <div class="classData">
        <label>班级:</label>
        <select v-model="classData" class="Dropdown">
          <option v-for="item in ClassName" :value="item._id"> {{item.name}}
          </option>
        </select>
      </div>
      <div class="submit">
        <mt-button type="primary" size="small" @click="submit" class="btns">提交</mt-button>
      </div>
    </div>
  </div>
</template>
<style lang="less" scoped>
  @import '../css/Classinvitation.less';
  
</style>
<script>
import axios from 'axios';
// 引入吐司
import { Toast, Button } from 'mint-ui';
// 引入接口
import { userClass, sendClass } from '../../api/api'
export default {
  name: "login",
  components: {

  },
  data() {
    return {
      username: '',
      classData: '',
      classDats: '',
      user_id: '',
      ClassName: [{ text: '请选择你所在的班级', value: '0' }]

    }
  },
  watch: {
    'classData': function(val) {
      this.classDatas = val;
    }
  },
  mounted() {
    document.title = "智量酷公众号";
  },
  methods: {
    submit() {
      var self = this;
      if (!self.username) {
        Toast('请输入姓名');
      } else if (!self.classDatas || self.classDatas === this.ClassName[0].text) {
        Toast('请输入班级');
      } else {
        // 把学员信息发送给后台;
        self.submits();
      }
    },
    // 提交数据
    submits() {
      var self = this;
      var user_id = JSON.parse(localStorage.getItem('user_id'));
      self.$http.patch(`/api/set_user_class/${user_id}/`, {
        name: self.username,
       team_id: self.classDatas
      }).then((response) => {
          if (response.status == 200) {
            // 存储数据
            localStorage.setItem('username', JSON.stringify(self.username));
            localStorage.setItem('classname', JSON.stringify(self.classDatas));
            // 跳转路径
            this.$router.push('/evaluate');
          } else {
             Toast('提交失败');
          }
        })
        .catch((error) => {
            Toast('请求错误,请稍后再试');
        })
    },
    event() {
      var username = JSON.parse(localStorage.getItem('username'));
      var className = JSON.parse(localStorage.getItem('classname'));
      if (username && className) {
        // 先注册 上线在开启
        this.$router.push('/evaluate');
      } else {
        Toast('请输入班级与姓名');
      }
    }
  },
  created() {
    // 添加提示数据;
    let obj = {
      name: '请选择你所在的班级',
      value: '0'
    };
    // 默认提示用户的数据;
    this.classData = this.ClassName[0].name;
    // this缓存备份;
    var self = this;
    sendClass().then((response) => {
        if (response.status == 200) {
          self.ClassName = response.data.results
          self.ClassName.unshift(obj);
          // 存储用户的id
          self.user_id = response.data.results[1].user_id[0]._id
          localStorage.setItem('user_id',JSON.stringify(self.user_id));
        } else {
          Toast('数据请求失败');
        }

      })
      .catch((error) => {
        Toast('请求错误,请稍后再试');
      })
  }
}

</script>
