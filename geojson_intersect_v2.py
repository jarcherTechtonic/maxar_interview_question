from flask import Flask, render_template, request
from shapely.geometry import Polygon
import geojson

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/intersect', methods = ['POST'])
def intersect():
    # polygon1 = geojson.utils.generate_random("Polygon")
    # polygon2 = geojson.utils.generate_random("Polygon")
    data = request.get_json()
    polygon1 = data['coord1'].split(',')
    polygon2 = data['coord2'].split(',')
    polygon1 = [int(coord) for coord in polygon1]
    polygon2 = [int(coord) for coord in polygon2]
    print(polygon1)
    try:
        p1_coordinates, p2_coordinates = polygon1, polygon2
        p1_coordinates, p2_coordinates = Polygon(p1_coordinates), Polygon(p2_coordinates)

        if p1_coordinates.intersection(p2_coordinates):
            return {"intersect": "True"}
        return {"intersect": "False"}
    except ValueError:
        print("Polygon data format invalid")

app.run(debug=True)