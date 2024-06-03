import math

import pytest
from advanced_operations import AdvancedOperations


def test_cube_root():
    assert AdvancedOperations.cube_root(27) == pytest.approx(3)
    assert AdvancedOperations.cube_root(-27) == pytest.approx(-3)


def test_square():
    assert AdvancedOperations.square(2) == 4
    assert AdvancedOperations.square(-2) == 4


def test_cube():
    assert AdvancedOperations.cube(3) == 27
    assert AdvancedOperations.cube(-3) == -27


def test_sqrt():
    assert AdvancedOperations.sqrt(4) == 2
    with pytest.raises(ValueError):
        AdvancedOperations.sqrt(-4)


def test_ln():
    assert AdvancedOperations.ln(1) == 0
    assert AdvancedOperations.ln(math.e) == pytest.approx(1)


def test_log():
    assert AdvancedOperations.log(100, 10) == 2
    assert AdvancedOperations.log(27, 3) == 3
    with pytest.raises(ValueError):
        AdvancedOperations.log(100, 1)
    with pytest.raises(ValueError):
        AdvancedOperations.log(100, -1)


def test_log10():
    assert AdvancedOperations.log10(100) == 2


def test_reciprocal():
    assert AdvancedOperations.reciprocal(2) == 0.5
    with pytest.raises(ValueError):
        AdvancedOperations.reciprocal(0)


def test_abs():
    assert AdvancedOperations.abs(-5) == 5
    assert AdvancedOperations.abs(5) == 5


def test_factorial():
    assert AdvancedOperations.factorial(5) == 120
    with pytest.raises(ValueError):
        AdvancedOperations.factorial(-5)
    with pytest.raises(ValueError):
        AdvancedOperations.factorial(5.5)
