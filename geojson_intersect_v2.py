from flask import Flask, render_template
from shapely.geometry import Polygon
import geojson

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/intersect', methods = ['POST'])
def intersect():
    polygon1 = geojson.utils.generate_random("Polygon")
    polygon2 = geojson.utils.generate_random("Polygon")

    if polygon1.is_valid or polygon2.is_valid:
        try:
            p1_coordinates = list(geojson.utils.coords(polygon1))
            p2_coordinates = list(geojson.utils.coords(polygon2))

            p1_coordinates, p2_coordinates = Polygon(p1_coordinates), Polygon(p2_coordinates)

            if p1_coordinates.intersection(p2_coordinates):
                return {"intersect": "True"}
            return {"intersect": "False"}
        except ValueError:
            print("Polygon data format invalid")

app.run(debug=True)