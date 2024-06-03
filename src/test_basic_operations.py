import pytest
from basic_operations import BasicOperations


def test_add():
    assert BasicOperations.add(1, 2) == 3
    assert BasicOperations.add(-1, -2) == -3


def test_subtract():
    assert BasicOperations.subtract(2, 1) == 1
    assert BasicOperations.subtract(-2, -1) == -1


def test_multiply():
    assert BasicOperations.multiply(2, 3) == 6
    assert BasicOperations.multiply(-2, -3) == 6


def test_divide():
    assert BasicOperations.divide(6, 3) == 2
    with pytest.raises(ValueError):
        BasicOperations.divide(1, 0)
