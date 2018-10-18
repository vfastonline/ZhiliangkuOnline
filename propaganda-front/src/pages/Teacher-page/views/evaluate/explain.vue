<template>
  <div class="content">
    <div class="nav">
      <span><a :href="backUrl?backUrl:'javascript:window.history.go(-1);'">返回</a></span>
      <h3>评价说明</h3>
    </div>
    <div>
      <p>各位同学:</p>
      <p>此评价是对自己一次负责的评价</p>
      <p>此评价是一次学习状态的评价</p>
      <p>此评价是知识掌握程度的评价</p>
      <p>此评价是针对学习任务的评价</p>
      <p>此评价是针对教学工资质量的评价</p>
      <p>此评价是关乎各位以后的学习任务以及工作安排进行的评价,请勿胡乱评价,也不要掺杂私人感情,我们只针对工作和事件来进行评价</p>
    </div>
    <div>
      <h3>此次评价分为三个部分:</h3>
      <div>
        <h4>讲师评价</h4>
        <ul>
          <li><span>精神面貌:</span>老师是否有足够好的精神状态来给带领大家完成学习任务</li>
          <li><span>课堂气氛:</span>你所在的班级课堂气氛是否活跃,是否是大家共同学习</li>
          <li><span>知识引导:</span>当学员遇到问题后,老师有没有给出问题的各种解决思路</li>
        </ul>
      </div>
      <div>
        <h4>学员方向</h4>
        <ul>
          <li><span>理解程度:</span>请如实写出你对本次课程内容中知识的掌握程度(这很重要)</li>
          <li><span>操作程度:</span>请如实写出你对本次课程内容中的实验以及工单完成度(这很重要)</li>
        </ul>
      </div>
      <div>
        <h4>自我表现</h4>
        <ul>
          <li><span>自我表现:</span>你有任何想说的话,都可以写下来,我们会对你给出的反馈进行分析,并酌情调整</li>
        </ul>
      </div>
      <p>此次评价完成是匿名评价,你的老师并不知道谁吐槽了他/她,也不清楚谁给了他/她好评&差评.只需要各位同学如实评价即可</p>
    </div>
    <div>
      <mt-button type="primary" size="small" @click="submit">去评价</mt-button>
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

.content {
  width: 100%;
  .px2px(font-size, 20px);

}
.content .nav {
  width: 100%;
  background: #007AFF;
  border: 1px solid blue;
}

</style>
<script>
// 引入吐司
import { Toast, Button } from 'mint-ui';
// 引入接口
import { quickLogin, smsCode } from '../../api/api'
export default {
  name: "login",
  props: ['backUrl'],
  components: {

  },
  data() {
    return {

    }
  },
  mounted() {},
  methods: {
    submit() {

      this.$router.push({
        path: '/evaluate'
      });
    }
  },
  created() {

  }
}

</script>
