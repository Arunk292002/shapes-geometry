from shapes_geometry.utils import validate_positive_numbers

def area(base,height):
    validate_positive_numbers(base=base,height=height)
    return base*height

def perimeter(base,side):
    validate_positive_numbers(base=base,side=side)
    return 2*(side+base)

def find_base(side,Perimeter):
    validate_positive_numbers(side=side,perimeter=Perimeter)
    return (Perimeter/2)-side

def find_side(base,Perimeter):
    validate_positive_numbers(base=base,perimeter=Perimeter)
    return (Perimeter/2)-base
