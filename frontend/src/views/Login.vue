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
        <button v-on:click="login" :hidden="authenticated" class="btn btn-primary">Sign in with Google</button>
        <span :hidden="!authenticated">Logged in as {{ email }}</span> <br>
        <button v-on:click="logout" :hidden="!authenticated" class="btn btn-warning">Log out</button>

    </div>
</template>


<script>
import axios from 'axios';

export default{
    name: 'Login',
    data() {
        return {
            authenticated: false,
            email: "",
        }
    },
    methods: {
        login: function() {
            this.$gAuth.signIn()
            .then(GoogleUser => {
                console.log('user', GoogleUser)
                this.email = GoogleUser.getBasicProfile().U3
                this.isSignIn = this.$gAuth.isAuthorized
                this.authenticated = true;
            })
            .catch(error  => {
            //on fail do something
            })
        },
        logout: function() {
            this.$gAuth.signOut()
            .then(() => {
                this.authenticated = false;
            
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
