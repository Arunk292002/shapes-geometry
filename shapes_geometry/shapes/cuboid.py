from shapes_geometry.utils import validate_positive_numbers

def volume(length,width,height):
    validate_positive_numbers(length=length,width=width,height=height)
    return width*length*height

def surface_area(length,width,height):
    validate_positive_numbers(length=length,width=width,height=height)
    return 2*((width*length)+(length*height)+(height*width))

def space_diagonal(length,width,height):
    validate_positive_numbers(length=length,width=width,height=height)
    return ((width**2)+(length**2)+(height**2))**0.5

def find_length(space_diagonal,width,height):
    validate_positive_numbers(space_diagonal=space_diagonal,width=width,height=height)
    return ((space_diagonal**2)-(width**2)-(height**2))**0.5

def find_width(space_diagonal,length,height):
    validate_positive_numbers(space_diagonal=space_diagonal,length=length,height=height)
    return ((space_diagonal**2)-(length**2)-(height**2))**0.5

def find_height(space_diagonal,length,width):
    validate_positive_numbers(space_diagonal=space_diagonal,length=length,width=width)
    return ((space_diagonal**2)-(length**2)-(width**2))**0.5