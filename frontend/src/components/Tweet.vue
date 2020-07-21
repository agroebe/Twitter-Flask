<template>
  <div class="container">
    <div class="card text-left">
      <div class="card-body">
        <h6 class="card-title"><strong>{{ displayName }}</strong> @{{ username }}</h6>
        <p class="card-text">{{ contents }}</p>
        <hr class="">
        <button type="button" class="btn btn-primary btn-sm mr-3" @click="logIt()">Favorite <span class="badge badge-light">9</span></button>
        <button type="button" class="btn btn-primary btn-sm" @click="logIt()">Retweet <span class="badge badge-light">9</span></button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Tweet',
  props: {
    displayName: String,
    username: String,
    contents: String
  },
  methods: {
    logIt() {
      console.log('yo')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
