from shapes_geometry.utils import PI, validate_positive_numbers

def volume(radius,side):
    validate_positive_numbers(radius=radius,side=side)
    return PI*(radius**2)*((4/3)*radius+side)

def surface_area(radius,side):
    validate_positive_numbers(radius=radius,side=side)
    return 2*PI*radius((2*radius)+side)

def circumference(radius):
    validate_positive_numbers(radius=radius)
    return 2*PI*radius

def total_height(radius,side):
    validate_positive_numbers(radius=radius,side=side)
    return side+(2*radius)