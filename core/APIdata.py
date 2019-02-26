import requests
#!/usr/bin/python3
import json

from flask import Flask, render_template, request, jsonify


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/travels')
def travels():
    return render_template('travels.html')

@app.route('/drivers')
def drivers():
    r = requests.get('https://europe-west1-metropolis-fe-test.cloudfunctions.net/api/trips')
    data = r.json()
    print("-----------------------")
    print(data[0]['stops'])
    print("-----------------------")
    conductor = data[0]['driverName']
    print(data[0]['driverName'])
    drivers = []
    for x in range(0, 3):
        drivers.append({'name': data[x]['driverName']})
    return render_template('drivers.html', text=drivers)

if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=8080,
        debug=True
    )