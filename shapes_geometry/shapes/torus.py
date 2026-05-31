from shapes_geometry.utils import validate_positive_numbers, PI

def area(major_radius, minor_radius):
    validate_positive_numbers(major_radius=major_radius, minor_radius=minor_radius)
    return (2*PI*major_radius)*(2*PI*minor_radius)

def find_major_radius(minor_radius,volume):
    validate_positive_numbers(minor_radius=minor_radius, volume=volume)
    return (0.5)*volume*((1/(PI*minor_radius))**2)

def find_minor_radius(major_radius,volume):
    validate_positive_numbers(major_radius=major_radius, volume=volume)
    return ((volume/(2*major_radius))**0.5)/PI

def volume(major_radius, minor_radius):
    validate_positive_numbers(major_radius=major_radius, minor_radius=minor_radius)
    return (PI*(minor_radius**2))*(2*PI*major_radius)