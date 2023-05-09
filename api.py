from fastapi import FastAPI
import requests

app = FastAPI()
request = requests.get('https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Education_WebMercator/MapServer/23/query?where=1%3D1&outFields=*&outSR=4326&f=json')


@app.get('/')
async def root():
    return request.json()

