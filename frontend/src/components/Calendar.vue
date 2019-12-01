<template>
  <router-link :to="{name: 'calendar', params: {id: encodeURI(id)}}">
    <div class="card shadow-sm p-2 m-2 text-center" style="width: 400px; display: inline-block;">
      <h3>{{ name }}</h3>
    </div>    
  </router-link>
</template>

<script>
export default {
  props: ["name", "id"]
}
</script>

