<template>
    <div class="card shadow-sm p-2 m-2 text-center" style="width: 400px; display: inline-block;">
      <h3>{{ name }}</h3>
      <div class="d-flex justify-content-around">
          <router-link class="btn btn-primary w-100 m-1" :to="{name: 'calendar', params: {id: encodeURI(id)}}">
            <button class="btn btn-primary">View</button>    
          </router-link>
  
        <button class="w-100 m-1 btn btn-info">Mail</button>
        <button v-on:click="deleteC" class="w-100 m-1 btn btn-danger">Delete</button>
      </div>
    </div>    
</template>

<script>
export default {
  props: ["name", "id"],
  methods: {
    deleteC: function (event) {
      console.log("Delete");
      this.$google.deleteCalendar(this.id).then(_ => {
        this.$router.go();
      });
    }
  }
}
</script>

