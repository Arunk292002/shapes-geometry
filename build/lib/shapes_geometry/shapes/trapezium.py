def area(a,b,height):
    return ((a+b)/2)*height
def perimeter(a,b,c,d):
    return a+b+c+d
def base_a(perimeter,b,c,d):
    return perimeter-b-c-d
def base_b(perimeter,a,c,d):
    return perimeter-a-c-d
def base_c(perimeter,a,b,d):
    return perimeter-a-b-d
def base_d(perimeter,a,b,c):
    return perimeter-a-b-c
def find_height(area,a,b):
    return 2*(area/(a+b))
 