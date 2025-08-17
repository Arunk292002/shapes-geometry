from shapes_geometry.utils import validate_positive_numbers

def area(a):
    validate_positive_numbers(a=a)
    return ((3*(3**0.5))/2)*(a**2)

def perimeter(a):
    validate_positive_numbers(a=a)
    return 6*a
