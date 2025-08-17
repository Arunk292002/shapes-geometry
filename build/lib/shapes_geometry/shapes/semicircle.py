from shapes_geometry.utils import validate_positive_numbers,PI

def area(radius):
    validate_positive_numbers(radius=radius)
    return(PI*(radius**2))/2

def perimter(diameter):
    validate_positive_numbers(diameter=diameter)
    if diameter/2==diameter:
        return (PI*(diameter))+diameter*2
    else:
        return (PI*(diameter*2))+diameter
