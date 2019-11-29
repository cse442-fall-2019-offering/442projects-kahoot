<template>
    <div class="content mx-auto">
        <!-- <h2>{{title}}</h2>
            <div class="form-group">
            <label for="username">Username </label>
            <input type="text" />
        </div>
        <div class="form-group">
            <label htmlFor="password">Password </label>
            <input type="text"/>
        </div>
        <div class="form-group">
            <button class="btn  btn-success">Login</button>
        </div> -->
        <button v-on:click="login" :hidden="$store.getters.authenticated" class="btn btn-primary">Sign in with Google</button>
        <span :hidden="!$store.getters.authenticated">Logged in as {{ $store.getters.email }}</span> <br>
        <button v-on:click="logout" :hidden="!$store.getters.authenticated" class="btn btn-warning">Log out</button>

    </div>
</template>


<script>
import axios from 'axios';

export default{
  name: 'Login',
  methods: {
    login: function() {
      this.$google.login();
      // this.$gAuth.signIn()
      // .then(GoogleUser => {
      //     window.user = GoogleUser;
      //     console.log('user', GoogleUser)
      //     this.$store.commit('login', GoogleUser.getBasicProfile().U3);
      //     this.$router.push("create");
      //     this.$gAuth.signOut()
      //     // this.isSignIn = this.$gAuth.isAuthorized
      // })
      // .catch(error  => {
      // //on fail do something
      // })
    },
    logout: function() {
      // this.$gAuth.signOut()
      // .then(() => {
      //     this.$store.commit('logout');
      // })
      // .catch(error  => {

      // })
    }
  }
}
</script>

<style lang="scss">

.content {
  margin-top: 100px;
  padding-top: 105px;
}


</style>
