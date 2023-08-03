from flask import Flask
import requests
import math

app = Flask(__name__)

@app.route('/all/<string:page>')
def hello_world(page):

    ko = (int(page)*1000)-1000

    request2 = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=1%3D1&outFields=*&outSR=4326&resultOffset='+ko+'&f=json')

    return request2.json()


@app.route('/code/<string:school_code>/<string:page>')
def retCode(school_code, page):

    
    ko = int(page)-1
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=%20(SCHOOL_CODE%20%3D%20'+school_code+')%20&outFields=*&outSR=4326&resultOffset='+ko+'&f=json')
    bo = request.json()
    return bo
    


@app.route('/name/<string:school_name>/<string:page>')
def retName(school_name, page):

    ko = page-1
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=%20(SCHOOL_NAME%20%3D%20'+school_name+')%20&outFields=*&outSR=4326&resultOffset='+ko+'&f=json')
    bo = request.json()
    return bo
    

@app.route('/subject/<string:subject>/<string:page>')
def retSubject(subject, page):
    ko = page-1
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=%20(SUBJECT%20%3D%20'+subject+')%20&outFields=*&outSR=4326&resultOffset='+ko+'&f=json')
    bo = request.json()
    return bo

@app.route('/health')
def retHealth():
    return 'Web Service is Working'
