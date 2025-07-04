pi=3.141592653589793
def area(radius):
    return(pi*(radius**2))/2
def perimter(diameter):
    if diameter/2==diameter:
        return (pi*(diameter))+diameter*2
    else:
        return (pi*(diameter*2))+diameter
