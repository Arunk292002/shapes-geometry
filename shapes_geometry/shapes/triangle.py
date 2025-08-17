from shapes_geometry.utils import validate_positive_numbers

def area(base,height):
    validate_positive_numbers(base=base,height=height)
    return (height*base)/2

def perimeter(side1,side2,base):
    validate_positive_numbers(side1=side1,side2=side2,base=base)
    return side1+base+side2

def find_height(base,Area):
    validate_positive_numbers(base=base,area=Area)
    return 2*(Area/base)
