<template>
  <div class="home">
    <Tweet class="mt-3 mb-3" v-for="tweet in tweets" :key=tweet.id :displayName=tweet.displayName :username=tweet.username :contents=tweet.contents />
    <p>{{tweets}}</p>
  </div>
</template>

<script>
import Tweet from '@/components/Tweet.vue'

import axios from 'axios'

export default {
  name: 'Home',
  components: {
    Tweet
  },
  data() {
    return {
      tweets: null
    }
  },
  mounted() {
    axios.get('http://localhost:5000/api/users/').then(response => {
      // this.tweets = response.data
      this.tweets = [
        {
          username: "agroebe",
          displayName: "Andrew P. Groebe",
          contents: "This is my first tweet, so hello world! This is my first tweet, so hello world! This is my first tweet, so hello world! This is my first tweet, so hello world! This is my first tweet, so hello world! This is my first tweet, so hello world!"
        },
        {
          username: "agroebe",
          displayName: "Andrew P. Groebe",
          contents: "This is my first tweet, so hello world!"
        },
      ]
      console.log(response)
    })
  }
}
</script>
