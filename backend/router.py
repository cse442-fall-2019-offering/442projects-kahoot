from flask import Flask, jsonify, request
from flask_cors import CORS
import scheduler

app = Flask(__name__)
CORS(app)

@app.route("/schedule", methods=['POST'])
def schedule():
    data = request.json
<<<<<<< HEAD
    
    return data
=======
    return scheduler.main(data)
>>>>>>> 4e0c578... did some more stuff
