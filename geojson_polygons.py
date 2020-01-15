import geojson
from shapely.geometry import Polygon

# random case
polygon1 = geojson.utils.generate_random("Polygon")
polygon2 = geojson.utils.generate_random("Polygon")
# case where polygons are overlapping
polygon3 = {
  "type": "Feature",
  "properties": {},
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [-108.402099609375,38.77121637244273],
        [-105.66650390625,38.89958342598271],
        [-106.92993164062499,40.17047886718109],
        [-108.402099609375,38.77121637244273]
      ]
    ]
  }
}

polygon4 = {
  "type": "Feature",
  "properties": {},
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [-104.62280273437499,39.32579941789298],
        [-105.8203125,40.245991504199026],
        [-106.842041015625,39.20671884491848],
        [-104.62280273437499,39.32579941789298]
      ]
    ]
  }
}
#case where polygons aren't over lapping.
polygon5 = {
"type": "Feature",
  "properties": {},
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [-112.313232421875,39.50404070558415],
        [-110.18188476562499,39.62261494094297],
        [-111.37939453125,40.6306300839918],
        [-112.313232421875,39.50404070558415]
      ]
    ]
  }
}

def polygons_overlap(p1, p2):
    p1_coordinates = list(geojson.utils.coords(p1))
    p2_coordinates = list(geojson.utils.coords(p2))

    p1_coordinates, p2_coordinates = Polygon(p1_coordinates), Polygon(p2_coordinates)

    if p1_coordinates.intersection(p2_coordinates):
        return True
    return False

import flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/intersect', methods=['POST', 'GET'])
def intersect():
    if polygons_overlap(polygon1, polygon2):
        return {"intersect":"true"}
    else:
        return {"intersect":"false"}

app.run()

print(polygons_overlap(polygon1, polygon2))
print(polygons_overlap(polygon3, polygon4))
print(polygons_overlap(polygon2, polygon5))




