from .shapes import (
    circle,
    cube,
    cuboid,
    cone,
    cylinder,
    ellipsoid,
    parallelogram,
    polygon,
    rectangle,
    sphere,
    square,
    triangle,
    rhombus,
    trapezium,
    hexagon,
    octagon,
    decagon,
    semicircle,
    pentagon,
    torus,
    kite,
)

from .exceptions import (
    ShapesGeometryError,
    InvalidDimensionError,
    InvalidCoordinateError,
)

# Package version
__version__ = "0.1.4"

__all__ = [
    "circle",
    "cube",
    "cuboid",
    "cone",
    "cylinder",
    "parallelogram",
    "rectangle",
    "sphere",
    "square",
    "triangle",
    "rhombus",
    "trapezium",
    "hexagon",
    "octagon",
    "decagon",
    "semicircle",
    "pentagon",
    "kite",
    "torus",
    "ellipsoid",
    "polygon"
    # exceptions
    "ShapesGeometryError",
    "InvalidDimensionError",
    "InvalidCoordinateError",
]
