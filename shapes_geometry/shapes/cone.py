from shapes_geometry.utils import validate_positive_numbers,PI

def volume(radius,height):
    validate_positive_numbers(radius=radius,height=height)
    return PI*(radius**2)*(height/3)

def radius(height,volume):
    validate_positive_numbers(height-height,volume=volume)
    return (3*(volume/(PI*height)))**0.5

def height(radius,volume):
    validate_positive_numbers(radius=radius,volume=volume)
    return 3*(volume/(PI*(radius**2)))

def surface_area(radius,height):
    validate_positive_numbers(radius=radius,height=height)
    return PI*radius*(radius+((height**2)+(radius**2))**0.5)

def base_area(radius):
    validate_positive_numbers(radius=radius)
    return PI*(radius**2)

def lateral_surface(radius,height):
    validate_positive_numbers(radius=radius,height=height)
    return PI*radius*((height**2)+(radius**2)**0.5)

def slant_height(radius,height):
    validate_positive_numbers(radius=radius,height=height)
    return ((radius**2)+(height**2))**0.5