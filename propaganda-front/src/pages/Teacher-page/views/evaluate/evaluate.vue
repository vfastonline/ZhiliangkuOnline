<template>
  <div class="main">
    <div class="nav">
      <p class="typeface">欢迎来评价</p>
      <p @click="Explain"><img src="../../assets/说明.png"></p>
    </div>
    <div class="title">
      <h2><img src="../../assets/智量logo.png"></h2>
      <p>智量酷承诺保护你的隐私,评价内容讲师不可见</p>
    </div>
    <div class="information">
      <div class="heders">
        <div><img :src="'../../../../static/imgs/'+className.Teacher"></div>
        <p>{{className.Tname}}</p>
        <p>{{className.Tclass}}</p>
      </div>
      <div class="single">
        <p>精神面貌</p>
        <span class="starXin" v-for="(item,index) in list" :key='index'>
          <span @click="star1(index)">
            <img :src="Stars_one>index?stara:starb"/>
          </span>
        </span>
      </div>
      <div class="single">
        <p>课堂气氛</p>
        <span class="starXin" v-for="(item,index) in list" :key='index'>
          <span @click="star2(index)">
            <img :src="Stars_two>index?stara:starb"/>
          </span>
        </span>
      </div>
      <div class="single">
        <p>知识引导</p>
        <span class="starXin" v-for="(item,index) in list" :key='index'>
          <span @click="star3(index)">
            <img :src="Stars_three>index?stara:starb"/>
          </span>
        </span>
      </div>
    </div>
    <div class="information">
      <div class="heders">
        <div><img :src="'../../../../static/imgs/'+className.Student"></div>
        <p>{{className.Sname}}</p>
        <p>{{className.Sclass}}</p>
      </div>
      <div class="single">
        <p>理解程度</p>
        <span class="starXin" v-for="(item,index) in list" :key='index'>
          <span @click="star4(index)">
            <img :src="Stars_four>index?stara:starb"/>
          </span>
        </span>
      </div>
      <div class="single">
        <p>操作程度</p>
        <span class="starXin" v-for="(item,index) in list" :key='index'>
          <span @click="star5(index)">
            <img :src="Stars_five>index?stara:starb"/>
          </span>
        </span>
      </div>
    </div>
    <!-- 吐槽区域 -->
    <div>
      
    </div>
    <button @click="submit">提交</button>
  </div>
</template>
<style type="text/css" lang="less" scoped>
  .px2px(@name, @px) {
    @{name}: round(@px / 2) * 1px;
    [data-dpr="2"] & {
      @{name}: @px * 1px;
    } // for mx3
    [data-dpr="2.5"] & {
      @{name}: round(@px * 2.5 / 2) * 1px;
    } // for 小米note
    [data-dpr="2.75"] & {
      @{name}: round(@px * 2.75 / 2) * 1px;
    }
    [data-dpr="3"] & {
      @{name}: round(@px / 2 * 3) * 1px
    } // for 三星note4
    [data-dpr="4"] & {
      @{name}: @px * 2px;
    }
  }

  .main {
    width: 100%;
  }

  .main .nav {
    background: #007aff;
    overflow: hidden;
  }

  .main .nav p {
    float: left;
    width: 50%;
    text-align: center;
  }

  .main .nav .typeface {
    font-size: 20px;
    color: #fff;
  }

</style>
<script>
// 引入吐司
import { Toast } from 'mint-ui';
// 引入接口
import { quickLogin, smsCode } from '../../api/api'
export default {
  name: "login",
  components: {

  },
  data() {
    return {
        list: [0, 1, 2, 3, 4],
        stara: '../../../../static/imgs/表情点亮-5.png',
        starb: '../../../../static/imgs/表情-5.png',
        Stars_one: 0,
        Stars_two: 0,
        Stars_three: 0,
        Stars_four: 0,
        Stars_five: 0,
        className: {
        Teacher: '头像-小.png',
        Student: '头像-小.png',
        Tname: '黄泽俊老师',
        Sname: '黄嘉城',
        Tclass: '大数据3班班主任兼讲师',
        Sclass: '大数据3班学员'
       }


    }
  },

  mounted() {

  },
  methods: {
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
   submit() {
      if (this.Stars_one==0 && this.Stars_two==0 && this.Stars_three==0) {
        Toast('老师你没有评分');
      } else if(this.Stars_four==0 && this.Stars_five==0){
         Toast('个人没有评分');
      } else {
        Toast('评价成功');
      }

    }
  },
  created() {

  }
}

</script>
