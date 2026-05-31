from shapes_geometry.utils import validate_positive_numbers,PI
from shapes_geometry.exceptions import CalculationError
import math

def sum_of_interior_angles(sides):
    validate_positive_numbers(sides=sides)
    return (sides-2)*180

def number_of_diagonals(sides):
    validate_positive_numbers(sides=sides)
    return (sides*(sides-3))/2

def area(sides,side_length):
    validate_positive_numbers(sides=sides,side_length=side_length)
    if sides <= 2:
        raise CalculationError("Area cannot be calculated for a polygon with fewer than 3 sides.")
    return (sides*(side_length**2))/(4*math.tan(PI/sides))

def perimeter(sides,side_length):
    validate_positive_numbers(sides=sides,side_length=side_length)
    return sides*side_length
