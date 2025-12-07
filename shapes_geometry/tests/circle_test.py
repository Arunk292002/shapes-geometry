import pytest
from shapes_geometry.shapes import circle
from shapes_geometry.exceptions import InvalidDimensionError
import math

# ---- Valid Inputs ----

@pytest.mark.parametrize("radius, expected", [
    (1, math.pi),
    (2.5, math.pi * 2.5**2),
    (10, math.pi * 100),
])
def test_circle_area_valid(radius, expected):
    assert circle.area(radius) == pytest.approx(expected, rel=1e-5)

@pytest.mark.parametrize("radius, expected", [
    (1, 2),
    (2.5, 5),
    (10, 20),
])
def test_circle_diameter_valid(radius, expected):
    assert circle.diameter(radius) == expected

@pytest.mark.parametrize("radius, expected", [
    (1, 2 * math.pi),
    (2.5, 2 * math.pi * 2.5),
    (10, 2 * math.pi * 10),
])
def test_circle_circumference_valid(radius, expected):
    assert circle.circumference(radius) == pytest.approx(expected, rel=1e-5)

# ---- Edge Cases ----

def test_circle_small_radius():
    assert circle.area(0.0001) == pytest.approx(math.pi * (0.0001**2), rel=1e-6)

def test_circle_very_small_radius():
    assert circle.area(1e-10) == pytest.approx(math.pi * (1e-10**2), rel=1e-6)

def test_circle_large_radius():
    assert circle.area(1000000) == pytest.approx(math.pi * (1000000**2), rel=1e-5)

def test_circle_zero_radius():
    with pytest.raises(InvalidDimensionError):
        circle.area(0)

# ---- Invalid Inputs ----

@pytest.mark.parametrize("invalid_radius", [-1, -5.5, "abc", None, [5], {"radius": 5}])
def test_circle_area_invalid(invalid_radius):
    with pytest.raises(InvalidDimensionError):
        circle.area(invalid_radius)

@pytest.mark.parametrize("invalid_radius", [-1, "abc", None])
def test_circle_diameter_invalid(invalid_radius):
    with pytest.raises(InvalidDimensionError):
        circle.diameter(invalid_radius)

@pytest.mark.parametrize("invalid_radius", [-1, "abc", None])
def test_circle_circumference_invalid(invalid_radius):
    with pytest.raises(InvalidDimensionError):
        circle.circumference(invalid_radius)