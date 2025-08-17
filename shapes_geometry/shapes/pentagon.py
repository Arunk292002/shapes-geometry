from shapes_geometry.utils import validate_positive_numbers

def area(a):
    validate_positive_numbers(a=a)
    return (0.25)*((5*(5+2*(5**0.5)))**0.5)*(a**2)

def perimeter(a):
    validate_positive_numbers(a=a)
    return 5*a

def find_diagonal(a):
    validate_positive_numbers(a=a)
    return ((1+(5**0.5))/2)*a