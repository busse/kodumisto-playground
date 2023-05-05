import re
from math import radians, degrees, sin, cos, pi

def is_valid_coordinate(coordinate):
    pattern = re.compile(r'^\s*(-?\d{1,2}(?:\.\d+)?),\s*(-?[1-9]?\d{1,2}(?:\.\d+)?|180(?:\.0+)?)\s*$')
    return bool(pattern.match(coordinate))

def opposite_coordinate(coordinate):
    lat, lon = map(float, coordinate.split(','))
    lat_rad, lon_rad = radians(lat), radians(lon)

    opposite_lat = -lat
    opposite_lon = lon + 180 if lon < 0 else lon - 180

    return opposite_lat, opposite_lon

# Test cases
test_coordinates = [
    "41.40338, 2.17403",
    "90.0, 180.0",
    "-90.0, -180.0",
    "0.0, 0.0",
    "100.0, 190.0",  # Invalid
    "abc, xyz"      # Invalid
]

for coordinate in test_coordinates:
    if is_valid_coordinate(coordinate):
        opposite_lat, opposite_lon = opposite_coordinate(coordinate)
        print(f"{coordinate}: Opposite Coordinate: ({opposite_lat}, {opposite_lon})")
    else:
        print(f"{coordinate}: Invalid coordinate")
