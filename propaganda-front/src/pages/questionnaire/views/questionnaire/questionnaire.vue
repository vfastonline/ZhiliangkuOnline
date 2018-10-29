<template>
  <div>
    <el-tabs v-model="activeName">
      <el-tab-pane label="职场素质" name="second" @click="btnsss">
        <div v-for="(item,index) in eq_results" :key="index" @click="showlLoginDialog">
          <el-col :span="24" class="card">
            <el-card shadow="hover">
              <p>{{item.title}}</p>
              <el-radio-group v-model="eq_radio[index]">
                <el-radio :label="key.value" v-for="(key,index) in item.option" :key="index">{{key.option}}</el-radio>
              </el-radio-group>
            </el-card>
          </el-col>
        </div>
        <el-button type="primary" @click="handOver('eq')">交卷</el-button>
      </el-tab-pane>
      <el-tab-pane label="逻辑能力">
        <div v-for="(item,index) in iq_results" :key="index" class="cards" @click="showlLoginDialog">
          <el-col :span="24">
            <el-card shadow="hover" class="el">
              <p>{{item.title}}</p>
              <input type="text" name="" v-if="item.title.indexOf('38')!=-1" placeholder="请输入你的答案" v-model="answer">
              <p><img :src="item.image"></p>
              <el-radio-group v-model="iq_radio[index]">
                <el-radio :label="key.value + key.titleno" v-for="(key, index) in item.option" :key="index">
                  <p>{{key.option}}</p>
                </el-radio>
              </el-radio-group>
            </el-card>
          </el-col>
        </div>
        <!-- 提交的弹框 -->
        <el-button type="primary" @click="handOver('iq')">交卷</el-button>
      </el-tab-pane>
    </el-tabs>
    <el-dialog title="选择老师帮你解析答案" :visible.sync="teacherDialog">
      <el-form :model="teacher_form">
        <el-form-item label="老师" :label-width="formLabelWidth">
          <el-select v-model="teacher_form.users" placeholder="请选择老师" value="">
            <el-option v-for="(teacher, index) in teachers" :key="index" v-bind:value="teacher.email">
              {{teacher.name}}
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="teacherDialog = false">取消</el-button>
        <el-button type="primary" @click="submitTestPaper">确定</el-button>
      </div>
    </el-dialog>
    <login></login>
  </div>
</template>
<style>
.el-card {
  margin-top: 10px;
}

</style>
<script>
import login from '../login/login.vue'
import arrs from './questionnaire'
import { getConsultation, getEq, getIq, submitEq, submitIq } from '../../api/api'


export default {
  name: "questionnaire",
  components: {
    login: login
  },
  data() {
    return {
      submitType: "",
      src: '',
      formLabelWidth: '120px',
      teacherDialog: false,
      activeName: 'second',
      eq_results: [],
      iq_results: [],
      eq_radio: [],
      iq_radio: [],
      answer: '',
      eqFraction: '',
      iqLogic: '',
      phone: "",
      teachers: [],
      teacher_form: {
        users: ''
      }
    }
  },
  methods: {
    btnsss(){
      console.log(11);
    },
    showlLoginDialog() {
      var is_login = this.$store.getters.userInfo.token;
      if (!is_login) {
        this.$store.dispatch('setLoginDialogStatus', true);
      }
    },

    notAnswerNotify() {
      this.$notify.error({
        title: '请注意',
        message: '请先做题.'

      });
    },

    warningNotify() {
      this.$notify({
        title: '警告',
        message: '请稍后再试',
        type: 'warning'
      });
    },
    AnswerOkNotify() {
      this.$notify({
        title: '成功',
        message: '恭喜,答题成功,稍后通知答题结果',
        type: 'success'
      });
    },
    notSelectTeacherNotify() {
      this.$notify.error({
        title: '失败',
        message: '请选择咨询老师.'

      });
    },

    getConsultant() {
      var self = this;
      getConsultation().then((response) => {
        switch (response.status) {
          case 200:
            self.teachers = response.data.results;
            break;
          case 400:
            self.sendCodeErrorNotify();
            break;
          default:
            self.sendCodeErrorNotify();
        }
      });
    },

    handOver(types) {
      this.submitType = types;
      var is_login = this.$store.getters.userInfo.token;
      if (!is_login) {
        this.$store.dispatch('setLoginDialogStatus', true);
        return
      }
      if (types == "eq" && !this.eqFraction || types == "iq" && !this.iqLogic) {
        this.notAnswerNotify();
        return
      }

      this.teacherDialog = true;
      this.getConsultant();
    },

    submitTestPaper() {
      if (this.submitType == 'eq') {
        this.submitEq();
      } else if (this.submitType == 'iq') {
        this.submitIq();
      }
    },

    // 提交职场素质数据
    submitEq() {
      if (this.eqFraction) {
        var arr = this.eqFraction.map(function(item) {
          return +item;
        })
      }
      if (arr) {
        var result = arr.reduce(function(result, value, index) {
          return result + value;
        });
      }
      var self = this;
      if (!self.teacher_form.users) {
        self.notSelectTeacherNotify();
      } else {

        submitEq({
          category: 'eq',
          value: result,
          consultant_email: self.teacher_form.users

        }).then((response) => {
          switch (response.status) {
            case 201:
              self.AnswerOkNotify();
              self.teacherDialog = false;          
              break;
            default:
              self.warningNotify();
          }
        })
      }
    },
    submitIq() {
      var self = this;
      var arr = self.iqLogic;
      var arr1 = arrs.arrMap(arr, 0, 11);
      var arr2 = arrs.arrMap(arr, 10, 21);
      var arr3 = arrs.arrMap(arr, 20, 31);
      var arr4 = arrs.arrMap(arr, 30, 41);
      var arr5 = arrs.arrMap(arr, 40, 51);
      var arr6 = arrs.arrMap(arr, 50, 61);

      var arry1 = arrs.arrMap2(arr1);
      var arry2 = arrs.arrMap2(arr2);
      var arry3 = arrs.arrMap2(arr3);
      var arry4 = arrs.arrMap2(arr4);
      var arry5 = arrs.arrMap2(arr5);
      var arry6 = arrs.arrMap2(arr6);

      var arrys1 = arrs.arrsLice(arry1);
      var arrys2 = arrs.arrsLice(arry2);
      var arrys3 = arrs.arrsLice(arry3);
      var arrys4 = arrs.arrsLice(arry4);
      var arrys5 = arrs.arrsLice(arry5);
      var arrys6 = arrs.arrsLice(arry6);

      var a1 = {};
      for (var i = 0; i < arrys1.length; i++) {
        var str1 = arrys1[i].split(':');
        a1[str1[0]] = str1[1]
      }
      var b1 = JSON.stringify(a1);
      var a2 = {};
      for (var i = 0; i < arrys2.length; i++) {
        var str2 = arrys2[i].split(':');
        a2[str2[0]] = str2[1]
      }
      var b2 = JSON.stringify(a2);
      var a3 = {};
      for (var i = 0; i < arrys3.length; i++) {
        var str3 = arrys3[i].split(':');
        a3[str3[0]] = str3[1]
      }
      var b3 = JSON.stringify(a3);
      var a4 = {};
      for (var i = 0; i < arrys4.length; i++) {
        var str4 = arrys4[i].split(':');
        a4[str4[0]] = str4[1]
      }
      a4.TI38 = this.answer;
      var b4 = JSON.stringify(a4);
      var a5 = {};
      for (var i = 0; i < arrys5.length; i++) {
        var str5 = arrys5[i].split(':');
        a5[str5[0]] = str5[1]
      }
      var b5 = JSON.stringify(a5);
      var a6 = {};
      for (var i = 0; i < arrys6.length; i++) {
        var str6 = arrys6[i].split(':');
        a6[str6[0]] = str6[1]
      }
      var b6 = JSON.stringify(a6);
      var str = localStorage.getItem('token');
      var token = 'Bearer ' + str;
      if (!self.teacher_form.users) {
        self.notSelectTeacherNotify();
      } else {
        submitIq({
          category: 'iq',
          option_1: b1,
          option_2: b2,
          option_3: b3,
          option_4: b4,
          option_5: b5,
          option_6: b6,
          consultant_email: self.teacher_form.users
        }).then((response) => {
          switch (response.status) {
            case 201:
              self.AnswerOkNotify();
              self.teacherDialog = false;
              break;
            default:
              self.warningNotify();
          }
        })
      }

    },
  },

  // 监听数据变化
  watch: {
    'eq_radio': function(val) {
      this.eqFraction = val;
    },
    'iq_radio': function(val) {
      this.iqLogic = val;
    }
  },

  created() {
    var self = this;
    getEq().then((response) => {
      self.eq_results = response.data.results
    });

    getIq().then((response) => {
      self.iq_results = response.data.results
    });
  }
}

</script>
