from shapes_geometry.utils import validate_positive_numbers,PI

def volume(radius):
    validate_positive_numbers(radius=radius)
    return (4/3)*PI*(radius**2)

def radius(volume):
    validate_positive_numbers(volume=volume)
    return (3(volume/(4*PI)))**(1/3)

def diameter(radius):
    validate_positive_numbers(radius=radius)
    return 2*radius

def surface_area(radius):
    validate_positive_numbers(radius=radius)
    return 4*PI*(radius**2)