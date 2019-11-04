
SERVER := ${user}@cheshire.cse.buffalo.edu
SSHSOCKET :=~/.ssh/$(SERVER)
WEB_ROOT := /web/CSE442-542/2019-Fall/cse-442h/

deploy:

	ssh -M -f -N -o ControlPath=$(SSHSOCKET) $(SERVER)
		
	npm --prefix frontend run build
	
	ssh -o ControlPath=$(SSHSOCKET) $(SERVER) "rm $(WEB_ROOT)frontend -r && mkdir $(WEB_ROOT)frontend"   
	ssh -o Controlpath=$(SSHSOCKET) $(SERVER) "rm $(WEB_ROOT)backend -r && mkdir $(WEB_ROOT)backend"

	scp -o ControlPath=$(SSHSOCKET) -r frontend/dist/* $(SERVER):$(WEB_ROOT)frontend 

	scp -o ControlPath=$(SSHSOCKET) -r backend/* $(SERVER):$(WEB_ROOT)backend

	ssh -o Controlpath=$(SSHSOCKET) $(SERVER) "pip3 install -t $(WEB_ROOT)backend -r $(WEB_ROOT)backend/requirements.txt"
	ssh -o Controlpath=$(SSHSOCKET) $(SERVER) "chmod +x $(WEB_ROOT)backend/app.cgi"

	ssh -S $(SSHSOCKET) -O exit $(SERVER)
