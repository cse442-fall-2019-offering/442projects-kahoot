<template>
  <div id="app">
    <div id="nav">
      <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
        <a class="navbar-brand" href="#">iScheduler</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav mr-auto">
            <b-nav-item :hidden="$store.getters.authenticated" to="/">Login</b-nav-item> 
            <b-nav-item :hidden="!$store.getters.authenticated"  to="/schedules">Schedules</b-nav-item> 
            <b-nav-item :hidden="!$store.getters.authenticated" to="/create">Create</b-nav-item> 
            <b-nav-item :hidden="!$store.getters.authenticated" to="/Help">Help</b-nav-item>
          </ul>
          <ul class="nav navbar-nav navbar-right">
            <li :hidden="!$store.getters.authenticated"><button  v-on:click="this.$google.logout" class="btn">
              <span :hidden="!$store.getters.authenticated"> Logout {{ $store.getters.email }} </span></button>
            </li>
          </ul>
        </div>
      </nav>
      
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="scss">
@import './../node_modules/open-iconic/font/css/open-iconic-bootstrap.css';
@import 'node_modules/bootstrap/scss/bootstrap';
@import 'node_modules/bootstrap-vue/src/index.scss';

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

.oi {
  margin: 0px 8px;
}
</style>
