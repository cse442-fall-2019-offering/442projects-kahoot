<template>
  <div>
    
    <div class="sidenav">

      <a href="#"><span class="oi oi-plus"></span>Old</a>
    </div>
  </div>
</template>

<script>
import Row from './../components/Create/Row.vue';

export default {
  components: {
    Row
  },
  data () {
    return {
      rows: []
    } 
  },
  methods: {
    addTeam: function() {
      this.rows.push({ team: this.rows.length + 1 });
    }
  }
}
</script>

<style lang="scss">
.sidenav {
  height: 100%; 
  width: 160px;
  position: fixed; 
  z-index: 1; 
  top: 0; 
  left: 0;
  background-color: #121212; 
  overflow-x: hidden; 
  padding: 20px;
  padding-top: 80px;
  text-align: left;
}
.sidenav a {
  margin-top: 10px;
  font-size: 20px;
  color: #c9c9c9;
  display: block;
}
.sidenav a:hover {
  text-decoration: none;
  color: green;
}
.content {
  margin-left: 160px;
  padding-top: 55px;
}
</style>