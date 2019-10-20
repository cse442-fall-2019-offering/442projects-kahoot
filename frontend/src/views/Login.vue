<template>


    <div class="content mx-auto">
        <h2>{{title}}</h2>
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
            </div>
    </div>
</template>


<script>
import axios from 'axios';

export default{
    name: 'Login',
    mounted() {
        axios
            .get(process.env.VUE_APP_BACKEND + "/schedule")
            .then(res => {
                console.log(res);
            })
    },
    data(){
        return{
            title: 'Login'
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
