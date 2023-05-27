from flask import Flask
import requests

request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=1%3D1&outFields=*&outSR=4326&f=json')

app = Flask(__name__)

@app.route('/all')
def hello_world():
    return request.json()

@app.route('/code/{code}')
def retCode(code: int):
    final_set = {}
    bo = request.json()

    def my_filtering_function(pair):
        key, value = pair
        if key == 'features':
            for i in value:
                if i.get('attributes').get('SCHOOL_CODE') == code:
                    final_set.update({key: [final_set.get('features'), i]})
                
        else:
            return False
        

    filtered_data= dict(filter(my_filtering_function, bo.items()))

    return final_set
