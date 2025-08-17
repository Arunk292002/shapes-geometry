from shapes_geometry.utils import validate_positive_numbers,PI

def area (radius):
    validate_positive_numbers(radius=radius)
    return PI*radius**2
def diameter(radius):
    validate_positive_numbers(radius=radius)
    return 2*radius
def circumference(radius):
    validate_positive_numbers(radius=radius)
    return 2*PI*radius