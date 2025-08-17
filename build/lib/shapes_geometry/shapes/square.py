from shapes_geometry.utils import validate_positive_numbers

def area(side):
    validate_positive_numbers(side=side)
    a= side**2
    return a

def perimeter(side):
    validate_positive_numbers(side=side)
    p=4*side
    return p

def diagonal(side):
    validate_positive_numbers(side=side)
    power=0.5
    d=(2**power)*side
    return d