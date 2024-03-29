from flask import Flask
import requests
import math

app = Flask(__name__)

@app.route('/all/<int:page>')
def hello_world(page):

    ko = (page*1000)-1000

    request2 = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=1%3D1&outFields=*&outSR=4326&resultOffset='+str(ko)+'&f=json')

    return request2.json()


@app.route('/code/<string:school_code>/<int:page>')
def retCode(school_code, page):

    
    ko = (page*1000)-1000
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=%20(SCHOOL_CODE%20%3D%20'+school_code+')%20&outFields=*&outSR=4326&resultOffset='+str(ko)+'&f=json')
    bo = request.json()
    return bo
    


@app.route('/name/<string:school_name>/<int:page>')
def retName(school_name, page):

    ko = (page*1000)-1000
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=SCHOOL_NAME%20%3D%20%27'+school_name+'%27&outFields=*&outSR=4326&resultOffset='+str(ko)+'&f=json')
    bo = request.json()
    return bo
    

@app.route('/subject/<string:subject>/<int:page>')
def retSubject(subject, page):
    ko = (page*1000)-1000
    request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=SUBJECT%20%3D%20%27'+subject+'%27&outFields=*&outSR=4326&resultOffset='+str(ko)+'&f=json')
    bo = request.json()
    return bo

@app.route('/health')
def retHealth():
    return 'Web Service is Working'
