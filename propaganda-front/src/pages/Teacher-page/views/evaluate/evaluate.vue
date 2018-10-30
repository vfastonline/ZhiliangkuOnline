<template>
  <div class="main">
    <div class="titles">
      <span class="Close" @click="CloseEvent"></span>
      <span class="typeface">欢迎来评价~</span>
      <span @click="Explain" class="Explain"></span>
    </div>
    <div class="title">
      <p class="imgs"><img src="../../assets/智量logo.png"></p>
      <p class="Hint">智量酷承诺保护你的隐私,评价内容讲师不可见</p>
    </div>
    <div class="General_evaluation">
      <div class="information">
        <div class="heders">
          <p class="head_img"><img :src="Teacher_picture"></p>
          <p class="classname">{{classTeacher}}</p>
        </div>
        <div class="single">
          <p class="Slogan">课堂气氛</p>
          <span class="starface" v-for="(item,index) in list" :key='index'>
          <span @click="star1(index)" class="face">
            <img :src="Stars_one>index?stara:starb"/>
          </span>
          </span>
        </div>
        <div class="single">
          <p class="Slogan">精神面貌</p>
          <span class="starface" v-for="(item,index) in list" :key='index'>
          <span @click="star2(index)">
            <img :src="Stars_two>index?stara:starb"/>
          </span>
          </span>
        </div>
        <div class="single">
          <p class="Slogan">知识引导</p>
          <span class="starface" v-for="(item,index) in list" :key='index'>
          <span @click="star3(index)">
            <img :src="Stars_three>index?stara:starb"/>
          </span>
          </span>
        </div>
      </div>
      <div class="information">
        <div class="heders">
          <p class="head_img"><img :src="classname_picture"></p>
          <p class="classname">{{classname}}</p>
        </div>
        <div class="single">
          <p class="Slogan">课堂程度</p>
          <span class="starface" v-for="(item,index) in list" :key='index'>
          <span @click="star4(index)">
            <img :src="Stars_four>index?stara:starb"/>
          </span>
          </span>
        </div>
        <div class="single">
          <p class="Slogan">操作成功</p>
          <span class="starface" v-for="(item,index) in list" :key='index'>
          <span @click="star5(index)">
            <img :src="Stars_five>index?stara:starb"/>
          </span>
          </span>
        </div>
      </div>
      <div class="Tucao_area">
        <textarea v-model="content" placeholder="你有什么要吐槽的?尽管说"></textarea>
      </div>
      <mt-button type="primary" class="submit" @click="submit" :disabled="isDisable">提交</mt-button>
    </div>
  </div>
</template>
<style type="text/css" lang="less" scoped>
@import '../css/evaluate.less';

</style>
<script type="text/javascript">
// 引入吐司
import { Toast } from 'mint-ui';
// 引入接口
import { information, submit_data, class_data } from '../../api/api'
export default {
  name: "login",
  data() {
    return {
      // 老师头像
      Teacher_picture:'',
      // 学生头像
      classname_picture:'',
      // 提交锁
      lock: '',
      // 老师id:
      Teacher_id: '',
      // 学生id:
      classname_id: '',
      isDisable: false,
      list: [0, 1, 2, 3, 4],
      // 上线之后把路径去掉
      stara: './static/imgs/表情点亮-5.png',
      starb: './static/imgs/表情-5.png',
      Stars_one: 0,
      Stars_two: 0,
      Stars_three: 0,
      Stars_four: 0,
      Stars_five: 0,
      Teacher_datas: [],
      classname_datas: [],
      score_records: [],
      score_Crecords: [],
      content: ''
    }
  },
  computed: {
    classTeacher: function() {
      return JSON.parse(localStorage.getItem('teacher'));
    },
    classname: function() {
      return JSON.parse(localStorage.getItem('username'));
    }
  },
  methods: {
    CloseEvent() {
      this.$router.push({
        path: '/Invitation'
      });
    },
    Explain() {
      this.$router.push({
        path: '/explain'
      });
    },
    star1(val) {
      this.Stars_one = val + 1;
    },
    star2(val) {
      this.Stars_two = val + 1;
    },
    star3(val) {
      this.Stars_three = val + 1;
    },
    star4(val) {
      this.Stars_four = val + 1;
    },
    star5(val) {
      this.Stars_five = val + 1;
    },
    // 老师数据
    Teacher_data() {
      let self = this;
      let spirit_obj = {
        score_item: self.score_records[0]._id,
        score: self.Stars_one
      };
      let Classroom_obj = {
        score_item: self.score_records[1]._id,
        score: self.Stars_two
      };
      let knowledge_obj = {
        score_item: self.score_records[2]._id,
        score: self.Stars_three
      };
      self.Teacher_datas = [spirit_obj, Classroom_obj, knowledge_obj];
      submit_data({
          user: self.Teacher_id,
          score_records: self.Teacher_datas,
          feedback: self.content

        }).then((response) => {
          // 请求成功把按钮变成灰色
          if (response.status == 201) {
            self.isDisable = true;
          } else {
            Toast('请求失败')
          }

        })
        .catch((error) => {
          // 请求失败,在把按钮打开
          Toast('请求错误,请稍后再试');
          self.isDisable = false;
        })

    },
    // 学生数据
    classname_data() {
      let self = this;
      let Understand_obj = {
        score_item: self.score_Crecords[0]._id,
        score: self.Stars_four
      };
      let operation_obj = {
        score_item: self.score_Crecords[1]._id,
        score: self.Stars_five
      }
      self.classname_datas = [Understand_obj, operation_obj];

      class_data({
          user: self.classname_id,
          score_records: self.classname_datas,
          // 上线代码回删除;
          feedback: self.content,
        }).then((response) => {
          // 请求成功把按钮变成灰色
          if (response.status == 201) {
            self.isDisable = true;
          } else {
            Toast('请求失败')
          }
        })
        .catch((error) => {
          // 请求失败,按钮可以在点击
          Toast('请求错误,请稍后再试');
          self.isDisable = false;
        })

    },
    submit() {
      var self = this;
      if (self.Stars_one == 0 || self.Stars_two == 0 || self.Stars_three == 0) {
        Toast('老师评分未评完');
      } else if (self.Stars_four == 0 || self.Stars_five == 0) {
        Toast('个人评分未评完');
      } else if (!self.content) {
        Toast('你没有吐槽');
      } else if (self.lock == true) {
        Toast({
          message: '亲你今天已评价',
          duration: 4000
        });
      } else {
        Toast({
          message: '评价成功',
          duration: 4000
        });
        // 提交老师数据
        self.Teacher_data();
        // 提交学生数据
        self.classname_data();
      }
    }
  },
  created() {
    var self = this;
    var username = JSON.parse(localStorage.getItem('username'));
    var className = JSON.parse(localStorage.getItem('classname'));
    if (username && className) {

    } else {
      // 先注册 上线在开启
      this.$router.push('/Invitation');
    }
    // 发送接口数据进行学生与老师赋值;
    information().then((response) => {
        if (response.status == 200) {
          for (var i = 0; i < response.data.results.length; i++) {
            // 本地存储数据状态;
            self.lock = response.data.results[i].is_history;
            localStorage.setItem('teacher', JSON.stringify(response.data.results[i].teacher.user_info.username));
            localStorage.setItem('classname', JSON.stringify(response.data.results[i].student.user_info.username));
            // 老师头像
            self.Teacher_picture = response.data.results[i].teacher.user_info.icon;
            // 学生头像
            self.classname_picture = response.data.results[i].student.user_info.icon;
            self.score_records = response.data.results[i].teacher.score_records;
            self.score_Crecords = response.data.results[i].student.score_records;
            self.Teacher_id = response.data.results[i].teacher.user_info._id;
            self.classname_id = response.data.results[i].student.user_info._id;
          }
        } else {
          Toast('请求失败');
        }
      })
      .catch((error) => {
        Toast('请求错误,请你稍后再试');
      })

  }
}

</script>
