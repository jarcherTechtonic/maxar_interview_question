from flask import Flask, render_template, request
from shapely.geometry import Polygon
import geojson

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/intersect', methods = ['POST'])
def intersect():
    try:
        data = request.get_json()
        data = data.values()
        polygons = []
        for item in data:
            coordinates = item['geometry']['coordinates']
            polygons.append(list(geojson.coords(coordinates[0])))
        polygons = [Polygon(polygon) for polygon in polygons]
        for p in range(len(polygons)):
            if polygons[0].intersection(polygons[1]):
                return 'These polygons Intersect'
        else:
            return 'These polygons don\'t intersect'
    except:
        return 'Please enter valid geoJSON Object'


app.run(debug=True)