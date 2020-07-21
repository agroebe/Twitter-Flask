<template>
  <div id="app">
    <nav class="navbar navbar-light bg-light justify-content-between">
      <a class="navbar-brand">Twitter</a>
      <form class="form-inline d-flex justify-content-center md-form form-sm active-cyan-2 mt-6">
        <input class="form-control form-control-sm mr-3 w-80" type="text" placeholder="Search" aria-label="Search">
        <i class="fas fa-search" aria-hidden="true"></i>
        <button type="button" class="btn btn-default btn-md">Sign Up</button>
        <button type="button" class="btn btn-primary btn-md">Login</button>
      </form>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
