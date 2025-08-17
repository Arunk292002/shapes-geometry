from shapes_geometry.shapes import circle
from shapes_geometry.exceptions import InvalidDimensionError

try:
    print(circle.area(-2))
except InvalidDimensionError as e:
    print("Error:", e)   # short clean message for users
