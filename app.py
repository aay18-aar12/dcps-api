from flask import Flask
import requests
import math




app = Flask(__name__)

@app.route('/all/<string:school_code>')
def hello_world(school_code):

    request2 = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=%20(SCHOOL_CODE%20%3D%20'+school_code+')%20&outFields=*&outSR=4326&returnCountOnly=true&f=json')

    countHolder = request2.json()

    count = countHolder.get('count')

    globCount = (math.trunc(count/1000))+1
    final_set = {}
    yo = []

    def my_filtering_function(pair):
        key, value = pair
        if key == 'features':
            for i in value:
                yo.append(i)
                final_set.update({key: yo})


                
        else:
            return False
        
    for i in range(globCount):
        ko = str(i*1000)
        request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=%20(SCHOOL_CODE%20%3D%20'+school_code+')%20&outFields=*&outSR=4326&resultOffset='+ko+'&f=json')
        bo = request.json()
        filtered_data = dict(filter(my_filtering_function, bo.items()))

    return final_set




@app.route('/subject/<string:school_code>/<string:subject>')
def retCode(school_code, subject):

    request2 = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=%20(SCHOOL_CODE%20%3D%20'+school_code+')%20&outFields=*&outSR=4326&returnCountOnly=true&f=json')

    countHolder = request2.json()

    count = countHolder.get('count')

    globCount = (math.trunc(count/1000))+1
    final_set = {}
    yo = []

    def my_filtering_function(pair):
        key, value = pair
        if key == 'features':
            for i in value:
                if i.get('attributes').get('SUBJECT') == subject:
                    yo.append(i)
                    final_set.update({key: yo})


                
        else:
            return False
        
    for i in range(globCount):
        ko = str(i*1000)
        request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=%20(SCHOOL_CODE%20%3D%20'+school_code+')%20&outFields=*&outSR=4326&resultOffset='+ko+'&f=json')
        bo = request.json()
        filtered_data = dict(filter(my_filtering_function, bo.items()))

    return final_set



@app.route('/name/<string:school_code>/<string:school_name>')
def retName(school_code, school_name):

    request2 = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=%20(SCHOOL_CODE%20%3D%20'+school_code+')%20&outFields=*&outSR=4326&returnCountOnly=true&f=json')

    countHolder = request2.json()

    count = countHolder.get('count')

    globCount = (math.trunc(count/1000))+1
    final_set = {}
    yo = []

    def my_filtering_function(pair):
        key, value = pair
        if key == 'features':
            for i in value:
                if i.get('attributes').get('SCHOOL_NAME') == school_name:
                    yo.append(i)
                    final_set.update({key: yo})


                
        else:
            return False
        
    for i in range(globCount):
        ko = str(i*1000)
        request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=%20(SCHOOL_CODE%20%3D%20'+school_code+')%20&outFields=*&outSR=4326&resultOffset='+ko+'&f=json')
        bo = request.json()
        filtered_data = dict(filter(my_filtering_function, bo.items()))

    return final_set



@app.route('/health')
def retHealth():
    return 'Web Service is Working'
