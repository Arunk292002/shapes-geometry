from shapes_geometry.utils import validate_positive_numbers

def area(p,q):
    validate_positive_numbers(p=p,q=q)
    return (p*q)/2

def perimeter(side):
    validate_positive_numbers(side=side)
    return 4*side

def diagonal_p(q,area):
    validate_positive_numbers(q=q,area=area)
    return 2*(area/q)

def diagonal_q(p,area):
    validate_positive_numbers(q=q,area=area)
    return 2*(area/p)

def find_side(p,q):
    validate_positive_numbers(p=p,q=q)
    return ((p**2)+(q**2)**0.5)/2