from shapes_geometry.utils import validate_positive_numbers

def area(a,b,height):
    validate_positive_numbers(a=a,b=b,height=height)
    return ((a+b)/2)*height

def perimeter(a,b,c,d):
    validate_positive_numbers(a=a,b=b,c=c,d=d)
    return a+b+c+d

def base_a(perimeter,b,c,d):
    validate_positive_numbers(perimeter=perimeter,b=b,c=c,d=d)
    return perimeter-b-c-d

def base_b(perimeter,a,c,d):
    validate_positive_numbers(perimeter=perimeter,a=a,c=c,d=d)
    return perimeter-a-c-d

def base_c(perimeter,a,b,d):
    validate_positive_numbers(perimeter=perimeter,a=a,b=b,d=d)
    return perimeter-a-b-d

def base_d(perimeter,a,b,c):
    validate_positive_numbers(perimeter=perimeter,a=a,b=b,c=c)
    return perimeter-a-b-c

def find_height(area,a,b):
    validate_positive_numbers(area=area,a=a,b=b)
    return 2*(area/(a+b))
 