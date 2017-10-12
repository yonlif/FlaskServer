from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/locations/<long>/<lat>')
def show_user_profile(long, lat):
    # show the user profile for that user
    print("got request for {} {}",long, lat)
    result = {}
    result['long'] = long
    result['lat'] = lat
    result['data'] = [{'long': 1, 'lat': 1}, {'long':2, 'lat':2}]

    return json.dumps(result)