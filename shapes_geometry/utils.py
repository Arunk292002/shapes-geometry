from shapes_geometry.exceptions import InvalidDimensionError

PI=3.141592653589793

def validate_positive_numbers(**kwargs):
    """
    Validate that all provided keyword arguments are numeric (int/float) and > 0.

    Example:
        validate_positive_numbers(radius=5, height=10)
    """
    for name, value in kwargs.items():
        if not isinstance(value, (int, float)):
            raise InvalidDimensionError(f"{name.capitalize()} must be a numeric value (int or float).")
        if value <= 0:
            raise InvalidDimensionError(f"{name.capitalize()} must be greater than zero.")
