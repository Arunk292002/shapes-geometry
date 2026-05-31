from shapes_geometry.utils import validate_positive_numbers,PI

def surface_area(a,b,c):
    validate_positive_numbers(a=a,b=b,c=c)
    return (4*PI)*(((((a*b)**1.6)*((a*c)**1.6)((b*c)**1.6))/3)**0.625)

def find_a(volume,b,c):
    validate_positive_numbers(volume=volume,b=b,c=c)
    return 3*(volume/(4*PI*b*c))

def find_b(volume,a,c):
    validate_positive_numbers(volume=volume,a=a,c=c)
    return 3*(volume/(4*PI*a*c))

def find_c(volume,a,b):
    validate_positive_numbers(volume=volume,a=a,b=b)
    return 3*(volume/(4*PI*a*b))

def volume(a,b,c):
    validate_positive_numbers(a=a,b=b,c=c)
    return (4/3)*(PI*a*b*c)
