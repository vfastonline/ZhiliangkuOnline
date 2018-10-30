<template>
  <div class="content">
    <h3 class="title">班级列表</h3>
    <ul class="list">
      <li v-for='item in items' @click="toggle(item)" class="class_list">
        <span class="username" v-for="data in item.teachers ">{{data.name}}</span>
        <span class="class_table">{{item.name}}</span>
      </li>
    </ul>
  </div>
</template>
<style type="text/css" lang="less" scoped>
 @import '../css/class.less';

</style>
<script>
// 引入吐司
import { Toast, Button } from 'mint-ui';
// 引入接口
import { class_list, class_details } from '../../api/api'
export default {
  name: "class",
  components: {

  },
  data() {
    return {
      items: []

    }
  },
  methods: {
    toggle(item) {
      var self = this;
      var class_id = item._id;
      var Today = self.GetDateStr(0);
      var Inverted = self.GetDateStr(-6);
      // self.$http.get('/api/user_score_item_avg/?',
      self.$http.get('https://www.zhiliangku.com/user_score_item_avg/?', {
          params: {
            team: class_id,
            created_at_before: Today,
            created_at_after: Inverted
          }
        }).then((response) => {
          if (response.status == 200) {
            // 存储数据
            localStorage.setItem('class_id', JSON.stringify(class_id));
            localStorage.setItem('Today', JSON.stringify(Today));
            localStorage.setItem('Inverted', JSON.stringify(Inverted));
            self.$router.push('/search');
          } else {
            Toast('请求失败');
          }
        })
        .catch((error) => {
          if(error.detail =='您没有执行该操作的权限。') {
            Toast('抱歉你没有权限查看');
          }else {
            Toast('请求失败,请稍后再试');
          }
          
        })

    },
    // 时间封装函数
    GetDateStr(AddDayCount) {    
      var dd = new Date();   
      dd.setDate(dd.getDate() + AddDayCount);  
      var y = dd.getFullYear();    
      var m = (dd.getMonth() + 1) < 10 ? "0" + (dd.getMonth() + 1) : (dd.getMonth() + 1); //
        
      var d = dd.getDate() < 10 ? "0" + dd.getDate() : dd.getDate();  
      return y + "-" + m + "-" + d;  
    }
  },
  created() {
    var self = this;
    // 页面加载后发送数据给后台,请求数据;
    class_list().then((response) => {
        if (response.status == 200) {
          self.items = response.data.results;
        } else {
          Toast('请求失败');
        }
      })
      .catch((error) => {
        Toast('请求失败,请稍后再试');
      })
  }
}
</script>
