<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <Tweet msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>

axios = require('axios')
// @ is an alias to /src
import Tweet from '@/components/Tweet.vue'

export default {
  name: 'User',
  components: {
    Tweeet
  }
}
</script>
