class ShapesGeometryError(Exception):
    """Base exception for all errors in shapes-geometry package."""


class InvalidDimensionError(ShapesGeometryError):
    """Raised when a dimension is invalid (negative or zero) or the dimension is non-numeric."""


class InvalidCoordinateError(ShapesGeometryError):
    """Raised when coordinates are invalid or non-numeric."""

class CalculationError(ShapesGeometryError):
    """Raised when geometric calculations cannot be performed."""
