from flask import Flask
import requests


request2 = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=1%3D1&outFields=*&outSR=4326&returnCountOnly=true&f=json')

countHolder = request2.json()

count = countHolder.get('count')




app = Flask(__name__)

@app.route('/all')
def hello_world():
    final_set = {}
    yo = []
    for i in range(190):
        ko = str(i*1000)
        request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=1%3D1&outFields=*&outSR=4326&resultOffset='+ko+'&f=json')
        bo = request.json()
        def my_filtering_function(pair):
            key, value = pair
            if key == 'features':
                for i in value:
                    yo.append(i)
                    final_set.update({key: yo})


                
            else:
                return False
        

    filtered_data = dict(filter(my_filtering_function, bo.items()))

    return final_set




