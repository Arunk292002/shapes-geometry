from shapes_geometry.utils import validate_positive_numbers

def volume(a):
    validate_positive_numbers(a=a)
    return a**3

def suraface_area(a):
    validate_positive_numbers(a=a)
    return 6*(a**2)

def space_diagonal(a):
    validate_positive_numbers(a=a)
    return (3**0.5)*a

def find_edge(space_diagonal):
    validate_positive_numbers(space_diagonal=space_diagonal)
    return (3**0.5)*(space_diagonal/3)