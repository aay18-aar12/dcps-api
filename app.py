from flask import Flask
import requests
import math

request2 = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=SCHOOL_YEAR%20%3D%20%272015-16%27&outFields=*&outSR=4326&returnCountOnly=true&f=json')

countHolder = request2.json()

count = countHolder.get('count')

globCount = (math.trunc(count/1000))+1


app = Flask(__name__)

@app.route('/all')
def hello_world():
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
        
    for i in range(10):
        ko = str(i*1000)
        request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=SCHOOL_YEAR%20%3D%20%272015-16%27&outFields=*&outSR=4326&resultOffset='+ko+'&f=json')
        bo = request.json()
        filtered_data = dict(filter(my_filtering_function, bo.items()))

    return final_set
