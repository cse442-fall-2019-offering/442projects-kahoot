#!/util/bin/python
from wsgiref.handlers import CGIHandler
from router import app

CGIHandler().run(app)
