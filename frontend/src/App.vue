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
            <b-nav-item to="/">Login</b-nav-item> 
            <b-nav-item to="/schedules">Schedules</b-nav-item> 
            <b-nav-item to="/create">Create</b-nav-item> 
          </ul>
        </div>
      </nav>
      
    </div>
    <router-view/>
  </div>
</template>

<style lang="scss">
@import './../node_modules/open-iconic/font/css/open-iconic-bootstrap.css';

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
