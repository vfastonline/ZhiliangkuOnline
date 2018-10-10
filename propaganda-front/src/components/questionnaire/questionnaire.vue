<template>
  <div class="content">
    <user_info></user_info>
    <eq_iq></eq_iq>
  </div>
</template>
<style src="./questionnaire.css"></style>
<script>
  import user_info from './user_info.vue'
  import eq_iq from './eq_iq.vue'

  export default {
    data() {
      return {}
    },
    methods: {},
    components: {
      user_info: user_info,
      eq_iq: eq_iq
    }
  }
</script>
