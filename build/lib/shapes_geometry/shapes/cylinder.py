pi=3.141592653589793
def volume(radius,height):
    return pi*radius*height
def diameter(height,Volume):
    return 2*((Volume/(pi*height))**0.5)
def surface_area(radius,height):
    return (2*pi*radius*height)+(2*pi*(radius**2))
def base_area(radius):
    return pi*(radius**2)
def lateral_surface(radius,height):
    return 2*pi*radius*height
def find_radius(height,ls):
    return ls/(2*pi*height)
def find_height(radius,ls):
    return ls/(2*pi*radius)