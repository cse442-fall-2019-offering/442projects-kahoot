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
            // this.$gAuth.signIn()
            // .then(GoogleUser => {
            //     console.log('user', GoogleUser)
            //     this.$store.commit('login', GoogleUser.getBasicProfile().U3);
            //     this.$router.push("create");
            //     // this.isSignIn = this.$gAuth.isAuthorized
            // })
            // .catch(error  => {
            // //on fail do something
            // })
            this.$gAuth.getAuthCode()
              .then(authCode => {
                  axios.post(process.env.VUE_APP_BACKEND + '/login', {code: authCode})
                    .then(r => {
                        this.$store.commit('login', r.data);
                        this.$router.push("create");
                    })
                    .catch(e => {

                    })
              })
              .catch(e => {

              });
        },
        logout: function() {
            this.$gAuth.signOut()
            .then(() => {
                this.$store.commit('logout');
            })
            .catch(error  => {
            
            })
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
