<template>
  <div>
    
    <div class="sidenav">
      <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">
      Options
    </button>

      <a href="#" v-on:click="addTeam"><span class="oi oi-plus"></span>Team</a>
      <a href="#"><span class="oi oi-plus"></span>Coach</a>
      <a href="#"><span class="oi oi-plus"></span>Event</a>
      <a href="#"><span class="oi oi-plus"></span>Player</a>
    </div>

    <div class="content">
      <table class="table">
        <thead>
          <tr>
            <th>Teams</th>
            <th>Coaches</th>
            <th>Events</th>
            <th>Players</th>
          </tr>
        </thead>
        <tbody>
          <Row v-for="item in rows" v-bind:key="item.team" v-bind:team="item.team"></Row>
        </tbody>
      </table>
    </div>

<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Schedule Options</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <div class="container">
          <div class="form-group row">
            <label for="">Schedule Name</label>
            <input type="text" placeholder="Schedule 1" class="form-control">
          </div>
          </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Submit</button>
      </div>
    </div>
  </div>
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
      rows: [{team:'Team 1'}]
    } 
  },
  methods: {
    addTeam: function() {
      this.rows.push({ team: 'Team ' + (this.rows.length + 1) });
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