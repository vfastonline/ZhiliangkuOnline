<template>
  <div class="content">
    <div class="title">
      <span class="return" @click="class_list"></span>
      <span class="Class_details">班级详情</span>
    </div>
    <div class="search">
      <div class="times">
        <span @click="openPicker" class="starts">&emsp;{{start}}{{birthday}}
        </span>
        <span class="tos">至</span>
        <span class="Ends" @click="Endtime">&emsp;{{ends}}{{Endtoday}}</span>
        <span class="searchs" @click="search_event">搜索</span>
      </div>
      <div class="datePicker">
        <mt-datetime-picker type="date" ref="picker" year-format="{value} 年" month-format="{value} 月" date-format="{value} 日" @confirm="handleConfirm" :startDate="startDate">
        </mt-datetime-picker>
      </div>
      <div class="datePicker">
        <mt-datetime-picker type="date" ref="pickers" year-format="{value} 年" month-format="{value} 月" date-format="{value} 日" @confirm="handleConfirms" :startDate="startDate">
        </mt-datetime-picker>
      </div>
    </div>
    <div id="myChart"></div>
    <!-- 选择区域-->
    <div class="Click_area">
      <ul class="list">
        <li class="spirit">
          <img src="../../assets/折线图标示-1.png">
          <span>精神面貌</span>
        </li>
        <li>
          <img src="../../assets/折线图标示-2.png">
          <span>课堂气氛</span>
        </li>
        <li>
          <img src="../../assets/折线图标示-3.png">
          <span>知识引导</span>
        </li>
        <li class="Understand">
          <img src="../../assets/折线图标示-4.png">
          <span>理解程度</span>
        </li>
        <li>
          <img src="../../assets/折线图标示-5.png">
          <span>操作成功</span>
        </li>
      </ul>
    </div>
    <!-- 吐槽区域 -->
    <div class="Tucao_area" v-for="(item,index) in Detailed" :key="index">
      <div class="hedaers">
        <!--  <img src="../../assets/头像-小.png"> -->
        <img :src="item.owner.icon">
        <p>{{item.owner.username}}</p>
      </div>
      <div class="texts">
        <h3 class="times">{{item.created_at}}</h3>
        <p class="Text_description">{{item.feedback}}</p>
      </div>
    </div>
  </div>
</template>
<style type="text/css" lang="less" scoped>
@import '../css/classPage.less';

</style>
<script>
// 引入吐司
import { DatetimePicker, Toast, Popup, Picker } from 'mint-ui'
import { quickLogin, smsCode } from '../../api/api'
export default {
  name: "search",
  components: {

  },
  data() {
    return {
      class_id: '',
      Today: '',
      Inverted: '',
      birthday: '', //开始时间
      Endtoday: '', //结束时间
      startDate: new Date('2018-01-01'),
      start: '开始时间:',
      ends: '结束时间:',
      // 吐槽数据
      Detailed: [],
      // x轴数据
      articles: [],
      // 平均值数据
      articless: [],
      articless1: [],
      articless2: [],
      articless3: [],
      articless4: [],
      articless5: [],
    }
  },
  methods: {
    search_event() {
      var self = this;
      self.class_id = JSON.parse(localStorage.getItem('class_id'));
      if (self.birthday > self.Endtoday) {
        Toast('抱歉你搜索的结束时间大于开始时间');
      } else if (!self.birthday && !self.Endtoday) {
        Toast('搜索时间不能为空');
      } else {
        // 开始搜索数据
        // self.$http.get('/api/user_score_item_avg/?', 
        self.$http.get('https://www.zhiliangku.com/user_score_item_avg/?', {
            params: {
              team: self.class_id,
              created_at_before: self.Endtoday,
              created_at_after: self.birthday
            }
          }).then((response) => {
            var X_arr = [];
            var Y_arr = [];
            if (response.data.length == 0) {
              Toast('抱歉.没有当前数据');
            } else if (response.status == 200) {
              for (var i = 0; i < response.data.length; i++) {
                X_arr.push(response.data[i]._id);
                for (var j = 0; j < response.data[i].avg_list.length; j++) {
                  self.articless.push(response.data[i].avg_list[j]);
                }
              }
              let obj = {};
              for (var i = 0; i < self.articless.length; i++) {
                if (!obj[self.articless[i]['name']]) {
                  obj[self.articless[i]['name']] = [];
                }
                obj[self.articless[i]['name']].push(self.articless[i]['avg']);
              }
              let arrResult = [];
              let j = 0;
              for (let k in obj) {
                arrResult[j++] = obj[k];
              }
              // 对时间进行排序
              let Time_arr = X_arr.sort((val1, val2) => {
                if (val1 > val2) return 1;
                else if (val1 < val2) return -1;
                else return 0;
              })
              self.articles = Time_arr;
              // 操作成功
              self.articless5 = arrResult[0];
              // 精神面貌
              self.articless1 = arrResult[1];
              // 课堂气氛
              self.articless2 = arrResult[2];
              // 理解程度
              self.articless3 = arrResult[3];
              // 知识引导
              self.articless4 = arrResult[4];
              // 把所有数据传入折线图中;
              self.drawLine(self.articles, self.articless1, self.articless2, self.articless3, self.articless4, self.articless5);
            } else {
              Toast('请求失败');
            }
          })
          .catch((error) => {
            Toast('请求失败,请稍后再试');
          })
      };
      // 取出后台吐槽数据
      self.$http.get('https://www.zhiliangku.com/user_score_feedback/?', {
          params: {
            team: self.class_id,
            created_at_before: self.Endtoday,
            created_at_after: self.birthday
          }
        }).then((response) => {
          if (response.status == 200) {
            self.Detailed = response.data.results;
          } else {
            Toast('请求失败');
          }
        })
        .catch((error) => {
          Toast('请求错误,请稍后再试');
        })
    },
    class_list() {
      this.$router.push('/list');
    },
    openPicker() {
      this.$refs.picker.open();
    },
    Endtime() {
      this.$refs.pickers.open();
    },
    handleConfirm(data, datas) {
      var d = new Date(data);
      var youWant = d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate();
      this.birthday = youWant;
      if (this.birthday) {
        this.start = '';
      } else {
        this.start = '开始时间';
      }
    },
    handleConfirms(data) {
      var d = new Date(data);
      var youWant = d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate();
      this.Endtoday = youWant;
      if (this.Endtoday) {
        this.ends = '';
      } else {
        this.ends = '结束时间';
      }
    },
    init() {
      const self = this;
      setTimeout(() => {
        window.onresize = function() {
          self.chart = self.echarts.init(document.getElementById('myChart'));
          self.chart.resize();
        }
      }, 20)
    },

    drawLine(datas, datas1, datas2, datas3, datas4, datas5) {
      // 基于准备好的dom，初始化echarts实例
      var myChart = this.echarts.init(document.getElementById('myChart'))
      // window.onresize = myChart.resize;
      // 绘制图表
      myChart.setOption({
        // 工具箱
        toolbox: {
          show: true,
          magicType: {
            type: ['line', 'bar']
          }
        },
        legend: {
          icon: 'rect',
          itemWidth: 12,
          itemHeight: 12,
          itemGap: 12,
          textStyle: {
            fontSize: 14,
            color: '#000'
          }
        },
        // 触发位置
        tooltip: {
          trigger: 'axis',
        },
        xAxis: {
          type: 'category',
          data: datas,
          axisLabel: {
            rotate: 50,
          },

        },
        yAxis: {},
        series: [{
            name: '精神面貌',
            type: 'line',
            animation: false,
            data: datas1,
            itemStyle: {
              normal: {
                color: '#f4b41e'
              }
            }
          },
          {
            name: '课堂气氛',
            type: 'line',
            data: datas2,
            itemStyle: {
              normal: {
                color: '#00a0ea'
              }
            }
          },
          {
            name: '知识引导',
            type: 'line',
            data: datas3,
            itemStyle: {
              normal: {
                color: '#8fc320'
              }
            }
          },
          {
            name: '理解程度',
            type: 'line',
            data: datas4,
            itemStyle: {
              normal: {
                color: '#950684'
              }
            }
          },
          {
            name: '操作成功',
            type: 'line',
            data: datas5,
            itemStyle: {
              normal: {
                color: '#e7004f'
              }
            }
          },

        ]
      });
    }
  },
  created() {
    var self = this;
    // 取出数据
    self.class_id = JSON.parse(localStorage.getItem('class_id'));
    self.Today = JSON.parse(localStorage.getItem('Today'));
    self.Inverted = JSON.parse(localStorage.getItem('Inverted'));
    // 取出后台可视化数据
    self.$http.get('https://www.zhiliangku.com/user_score_item_avg/?', {
        params: {
          team: self.class_id,
          created_at_before: self.Today,
          created_at_after: self.Inverted
        }
      }).then((response) => {
        var X_arr = [];
        var Y_arr = [];
        if (response.status == 200) {
          for (var i = 0; i < response.data.length; i++) {
            X_arr.push(response.data[i]._id);
            for (var j = 0; j < response.data[i].avg_list.length; j++) {
              self.articless.push(response.data[i].avg_list[j]);
            }
          }
          let obj = {};
          for (var i = 0; i < self.articless.length; i++) {
            if (!obj[self.articless[i]['name']]) {
              obj[self.articless[i]['name']] = [];
            }
            obj[self.articless[i]['name']].push(self.articless[i]['avg']);
          }
          let arrResult = [];
          let j = 0;
          for (let k in obj) {
            arrResult[j++] = obj[k];
          }
          // 对时间进行排序
          let Time_arr = X_arr.sort((val1, val2) => {
            if (val1 > val2) return 1;
            else if (val1 < val2) return -1;
            else return 0;
          })
          self.articles = Time_arr;
          // 操作成功
          self.articless5 = arrResult[0];
          // 精神面貌
          self.articless1 = arrResult[1];
          // 课堂气氛
          self.articless2 = arrResult[2];
          // 理解程度
          self.articless3 = arrResult[3];
          // 知识引导
          self.articless4 = arrResult[4];
          // 把所有数据传入折线图中;
          self.drawLine(self.articles, self.articless1, self.articless2, self.articless3, self.articless4, self.articless5);
        } else {
          Toast('请求失败');
        }
      })
      .catch((error) => {
        Toast('请求失败,请稍后再试');
      })

    // 取出后台吐槽数据
    self.$http.get('https://www.zhiliangku.com/user_score_feedback/?', {
        params: {
          team: self.class_id,
          created_at_before: self.Today,
          created_at_after: self.Inverted
        }
      })
      .then((response) => {
        if (response.status == 200) {
          self.Detailed = response.data.results;
        } else {
          Toast('请求失败');
        }
      })
      .catch((error) => {
        Toast('请求错误,请稍后再试');
      })
  },

  mounted() {
    // 渲染折线图
    this.drawLine();
    this.init();
  }
}

</script>
