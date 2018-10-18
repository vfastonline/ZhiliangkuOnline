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
        <div><img src=""></div>
        <p>某某老师</p>
        <p>大数据3班班主任兼讲师</p>
      </div>
      <div class="starXin" v-for="(item,index) in list" :key='index'>
        <div @click="star(index)">
          <!-- <img :src="xing>index?stara:starb" /> -->
          <!-- <p><img :src="'./imgs' + item.img"></p> -->
          <img src="./img/表情点亮-1.png">
        </div>
      </div>
    </div>
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
      list: [
        { id: 0, img: '表情点亮-1.png', imgs: '表情-1.png' },
        { id: 1, img: '表情点亮-2.png', imgs: '表情-2.png' },
        { id: 2, img: '表情点亮-3.png', imgs: '表情-3.png' },
        { id: 3, img: '表情点亮-4.png', imgs: '表情-4.png' },
        { id: 4, img: '表情点亮-5.png', imgs: '表情-5.png' },
      ],
      // list: [0, 1, 2, 3, 4,5],
      // stara: {

      // }
      // starb: {

      // }
      xing: 0
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
    star(val) {
      this.xing = val + 1
      console.log(this.xing);
    }
  },
  created() {

  }
}

</script>
