from shapes_geometry.utils import validate_positive_numbers

def area (w,l):
    validate_positive_numbers(width=w,length=l)
    return w*l

def perimeter(w,l):
    validate_positive_numbers(width=w,length=l)
    return 2*(l+w)

def diagonal(w,l):
    validate_positive_numbers(width=w,length=l)
    return (w**2+l**2)**0.5

def find_length(w,P):
    validate_positive_numbers(width=w,perimeter=P)
    return (P/2)-w

def find_width(l,P):
    validate_positive_numbers(length=l,perimeter=P)
    return (P/2)-l
