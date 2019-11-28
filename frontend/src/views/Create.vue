
<template>
  <div>
    
    <div class="sidenav">
      <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">
      Options
    </button>

      <a href="#" data-toggle="modal" data-target="#exampleModal"><span class="oi oi-plus"></span>Team</a>
      <a href="#" data-toggle="modal" data-target="#optionModal"><span class="oi oi-plus"></span>Options</a>
      <a href="#"  data-toggle="modal" data-target="#eventModal"><span class="oi oi-plus"></span>Time-Slot</a>
      <a href="#"><span class="oi oi-plus"></span>Player</a>
    </div>

    <div class="content container">
      <div class = "row">
        <div class = "col-12">
          <table class="table">
            <thead>
              <tr>
                <th>Teams</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <Row v-for="item in rows" v-bind:key="item.team" v-bind:team="item.team"></Row>
              </tr>
            </tbody>
          </table>
        </div>
      <div class="conent container">
        <div class="col-12">
          <table class="table">
            <thead>
              <tr>
                <th>Time-Slot</th>
              </tr>
            </thead>
            <tbody>
              <tr >
                <EventOption v-for="opt in timeOptions" v-bind:key="opt.day" v-bind:day="opt.day" v-bind:timeOption="opt.timeOption" ></EventOption>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      </div>
   
      <button type="button" v-on:click="onSubmit" class="btn btn-primary posit">Submit Data</button>
    </div>

<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Enter Team</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <div class="container">
          <div class="form-group row">
            <label for="">Team Name</label>
            <input v-model="message" placeholder="Team 1" class="form-control">
          </div>
          </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button"  v-on:click="addTeam" data-dismiss="modal" class="btn btn-primary">Submit</button>
      </div>
    </div>
  </div>
</div>

<div class="modal fade" id="optionModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
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
            <label for="" >Number of Weeks</label>
                <input v-model="weeks" class="form-control" type="number" placeholder="0">
          </div>
          <div class="form-group row">
            <label for="" >Number of weekly practices </label>
                <input v-model="practices" class="form-control" type="number" placeholder="0">
          </div>
          <div class="form-group row">
            <label for="" >Start date</label>
                <input v-model="sdate" class="form-control" type="date" placeholder="2019-11-15">
          </div>
          </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button"  v-on:click="addOptions" data-dismiss="modal" class="btn btn-primary">Submit</button>
      </div>
    </div>
  </div>
</div>

<div class="modal fade" id="eventModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Event Scheduler</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <div class="container">
          <div class="form-group row">
            <label for="exampleS" id="spacing">Day</label>
            
              <select v-model="selected" >
                <option>Monday</option>
                <option >Tuesday</option>
                <option>Wednesday</option>
                <option >Thursday</option>
                <option >Friday</option>
                <option >Saturday</option>
                <option >Sunday</option>
              </select>
            
          </div>

    
        </div>
      
      <br>
        <div class="container">
          <div class="form-group row">
            <label for="exampleTime" id="spacing">Time</label>
            
              <select v-model="timeOption" >
                <option>09:00 AM</option>
                <option >10:00 AM</option>
                <option>11:00 AM</option>
                <option >12:00 PM</option>
                <option >01:00 PM</option>
                <option >02:00 PM</option>
                <option >03:00 PM</option>
                <option >04:00 PM</option>
                <option >05:00 PM</option>
              </select>
            
          </div>

        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" v-on:click="addEvent" class="btn btn-primary" data-dismiss="modal">Submit</button>
      </div>
    </div>
  </div>
</div>
      
  </div>
</template>

<script>
import Row from './../components/Create/Row.vue';
import EventOption from './../components/Create/EventOption.vue';
import ScheduleOptions from './../components/Create/ScheduleOptions.vue';
import axios from 'axios';

export default {
  components: {
    Row,
    EventOption,
    ScheduleOptions
    
    
  },
  data () {
    return {
      message:'',
      weeks: '',
      practices:'',
      sdate:'',
      rows: [{
        
      }],
      selected:'',
      timeOption:'',
      day:'',
      options:[{}],      
      timeOptions: [{
       
      }]
      
    } 
  },
  methods: {
    addTeam: function() {
      this.rows.push({ team: (this.message)  });
    },
    addEvent: function(){
     this.timeOptions.push({
       day:(this.selected),
       timeOption:(this.timeOption)
       }
       );
     
    },
    addOptions: function(){
      this.options.push({weeks: (this.weeks), practices:(this.practices), sdate: (this.sdate)});
    },
    onSubmit:function(){
      const payload={
        teaminfo : this.rows,
        timing : this.timeOptions,
        scheduleOptions: this.options
      }
      
      axios.post(process.env.VUE_APP_BACKEND + '/schedule', payload)
        .then(r => {
          console.log(r);
        })
        .catch(e => {
          console.log(e);
        });
    }
  }
}
</script>

<style lang="scss">
.sidenav {
  height: 100%; 
  width: 200px;
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
.posit{
  position: absolute;
  right: 5px;
  bottom: 20px;
  
}
#spacing{
  
  padding-right: 20px
}
</style>