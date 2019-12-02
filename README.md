# Deploy to server

```console
$ make deploy user=yourusername
```

This builds the frontend and uploads frontend/dist/* to /web/CSE442-542/2019-Fall/cse-442h/frontend and backend/* to /web/CSE442-542/2019-Fall/cse-442h/backend. 

# Download API key from server

```console
$ make get_key user=yourusername
```

This downloads the Google Calendar API key from the server. 