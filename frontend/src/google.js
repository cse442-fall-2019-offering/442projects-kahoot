import store from './store';
import router from './router';
import key from './api'

class Google {

  constructor() {
    this.loaded = new Promise(resolve => {
      gapi.load('client:auth2', _ => {
        gapi.client.init({
          apiKey: key,
          clientId: '220236547468-49pis7nd758b0rg1rrldmn38jjtl74f7.apps.googleusercontent.com',
          discoveryDocs: ['https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest'],
          scope: 'profile https://www.googleapis.com/auth/calendar',
        }).then(_ => {
          this.loginStateChange(gapi.auth2.getAuthInstance().isSignedIn.get())
          resolve();
        }, function(error) {
          alert("Google API error");
        });
      });
    });
  } 

  loginStateChange(isLoggedIn) {
    if (isLoggedIn) {
      const email = gapi.auth2.getAuthInstance().currentUser.Ab.w3.U3;
      store.commit('login', email);
    } else {
      store.commit('logout');
      if (router.currentRoute.path != '/') router.push('/');
    }
  }

  login() {
    gapi.auth2.getAuthInstance().signIn(/*{prompt: 'consent'}*/).then(user => {
      this.loginStateChange(gapi.auth2.getAuthInstance().isSignedIn.get());
      router.push('create');
    });
  }

  logout() {
    gapi.auth2.getAuthInstance().signOut();
    store.commit('logout');
    router.push('/');
  }

  // Get all calendars associated with this app 
  getCalendars(callback) {
    return new Promise(resolve => {
      this.loaded.then(_ => {
        gapi.client.calendar.calendarList.list().then(response => {
          const calendars = response.result.items.filter(v => {
            return v.summary.includes('iScheduler');
          });
          resolve (calendars);
        })
      })
    });
  }

  deleteCalendar(id) {}

  createCalendar(name, events) {
    return new Promise(resolve => {
      this.loaded.then(_ => {
        gapi.client.calendar.calendars.insert({
          resource: {
            summary: `iScheduler: ${name}`
          }
        }).then(r => {
          const id = r.result.id;
          this.createEvents(id, events).then(c => {
            console.log("Done");
            resolve(r.result);
          });
        });
      });
    });
  }

  createEvents(id, events) {
    return Promise.all(events.map(e => {
      return this.createEvent(id, e)
    }));
  }

  createEvent(id, event) {
    return new Promise(resolve => {
      this.loaded.then(_ => {
        gapi.client.calendar.events.insert({
          calendarId: id,
          resource: {
            summary: event.summary,
            description: event.description,
            start: {
              dateTime: event.datetime_obj_start,
              timeZone: "EST",
            },
            end: {
              dateTime: event.datetime_obj_end,
              timeZone: "EST",
            }
          }
        }).then(r => {
          resolve(r);
        })
      });
    });
  }

} 

export default Google;