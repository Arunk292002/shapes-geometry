from shapes_geometry.utils import validate_positive_numbers

def area(diagonal_1,diagonal_2):
    validate_positive_numbers(diagonal_1=diagonal_1,diagonal_2=diagonal_2)
    return 0.5*diagonal_1*diagonal_2

def perimeter(a,b):
    validate_positive_numbers(a=a,b=b)
    return 2*(a+b)