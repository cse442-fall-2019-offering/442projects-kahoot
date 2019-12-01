<template>
<div class = "content container">

  <p><b>Scheduling rules</b> <br/>
  Each team can play only one game a week <br/>
  For number of teams i, minimum number of events per week should be i+(i/2), (i/2) being rounded down <br/>
  For odd number of teams, i, minimum weeks needed for valid scheduling is i <br/>
  For even number of teams, i, minimum weeks needed for valid scheduling is (i-1)  
  </p>
</div>
</template>

<script>
import Row from './../components/Create/Row.vue';

export default {
  name: 'Help',
  components: {
    Row
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