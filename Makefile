

deploy:
	npm --prefix frontend run build
	scp -r frontend/dist/* ${user}@cheshire.cse.buffalo.edu:/web/CSE442-542/2019-Fall/cse-442h/frontend
	scp -r backend ${user}@cheshire.cse.buffalo.edu:/web/CSE442-542/2019-Fall/cse-442h/backend

