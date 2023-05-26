from flask import Flask
import requests

request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=1%3D1&outFields=*&outSR=4326&f=json')

app = Flask(__name__)

@app.route('/all')
def hello_world():
    return request.json()

@app.route('/school/{name}')
def retSchool(name: str):
    request = [x for x in request if x['SCHOOL_NAME'] == name]
    return request.json()
