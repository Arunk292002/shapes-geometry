from shapes_geometry.utils import validate_positive_numbers

def area(a):
    validate_positive_numbers(a=a)
    return (5/2)*(a**2)*((5+2*(5**0.5)**0.5))
def perimeter(a):
    validate_positive_numbers(a=a)
    return 10*a