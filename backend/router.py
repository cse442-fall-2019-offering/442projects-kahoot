from flask import Flask, jsonify, request
from flask_cors import CORS
import scheduler
import auth, json

app = Flask(__name__)
CORS(app)

@app.route("/schedule", methods=['POST'])
def schedule():
    data = request.json
    print(type(data))
    print(data)
    return scheduler.get_week_array(data)


@app.route("/login", methods=['POST'])
def login():
    authCode = json.dumps(request.json["code"])
    return json.dumps(auth.login(authCode))