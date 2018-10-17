<template>
  <div>
    <div>
      <label>姓名</label>
      <input type="" name="" placeholder="请输入姓名" v-model='username'>
    </div>
    <div>
      <label>班级</label>
      <select v-model="ClassData" @change="onchange">
        <option v-for="item in ClassName" v-bind:value="item.value"> {{item.text}}
        </option>
      </select>
    </div>
    <div>
      <button @click="submit">提交</button>
    </div>
  </div>
</template>
<style>


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
      username: '',
      ClassData: '',
      ClassName: [
        { text: '1年级', value: '0' },
        { text: '2年级', value: '1' },
        { text: '3年级', value: '2' }
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
      if(!self.username){
        Toast('请输入姓名');
      }else if(!self.ClassData){
        Toast('请输入班级');
      } else {
        Toast('发送axios');
      }
    }
  },
  created() {
    
  }
}

</script>
