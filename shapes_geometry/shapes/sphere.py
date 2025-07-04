pi=3.141592653589793
def volume(radius):
    return (4/3)*pi*(radius**2)
def radius(volume):
    return (3(volume/(4*pi)))**(1/3)
def diameter(radius):
    return 2*radius
def surface_area(radius):
    return 4*pi*(radius**2)