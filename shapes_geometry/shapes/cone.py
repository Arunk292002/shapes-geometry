pi=3.141592653589793
def volume(radius,height):
    return pi*(radius**2)*(height/3)
def radius(height,volume):
    return (3*(volume/(pi*height)))**0.5
def height(radius,volume):
    return 3*(volume/(pi*(radius**2)))
def surface_area(radius,height):
    return pi*radius*(radius+((height**2)+(radius**2))**0.5)
def base_area(radius):
    return pi*(radius**2)
def lateral_surface(radius,height):
    return pi*radius*((height**2)+(radius**2)**0.5)
def slant_height(radius,height):
    return ((radius**2)+(height**2))**0.5