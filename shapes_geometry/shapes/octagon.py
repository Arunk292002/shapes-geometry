from shapes_geometry.utils import validate_positive_numbers

def area(a):
    validate_positive_numbers(a=a)
    return 2*(1+(2**0.5))*(a**2)

def perimeter(a):
    validate_positive_numbers(a=a)
    return 8*a