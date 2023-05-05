import re
from math import radians, degrees, sin, cos, pi

def validate(val_in):
    pattern = re.compile(r'^\s*(-?\d{1,2}(?:\.\d+)?),\s*(-?[1-9]?\d{1,2}(?:\.\d+)?|180(?:\.0+)?)\s*$')
    return bool(pattern.match(val_in))

def calc_second_val(val_in):
    a, b = map(float, val_in.split(','))
    a_rad, b_rad = radians(a), radians(b)

    opposite_a = -a
    opposite_b = b + 180 if b < 0 else b - 180

    return opposite_a, opposite_b
