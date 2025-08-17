from shapes_geometry.utils import validate_positive_numbers,PI

def volume(radius,height):
    validate_positive_numbers(radius=radius,height=height)
    return PI*radius*height

def diameter(height,Volume):
    validate_positive_numbers(height=height,volume=volume)
    return 2*((Volume/(PI*height))**0.5)

def surface_area(radius,height):
    validate_positive_numbers(radius=radius,height=height)
    return (2*PI*radius*height)+(2*PI*(radius**2))

def base_area(radius):
    validate_positive_numbers(radius=radius)
    return PI*(radius**2)

def lateral_surface(radius,height):
    validate_positive_numbers(radius=radius,height=height)
    return 2*PI*radius*height

def find_radius(height,ls):
    validate_positive_numbers(height=height,ls=ls)
    return ls/(2*PI*height)

def find_height(radius,ls):
    validate_positive_numbers(radius=radius,ls=ls)
    return ls/(2*PI*radius)