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
export default{
    name: 'Login',
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
