
from main import calculate


def test_addition():
    assert calculate(1, "+", 2) == 3


def test_subtraction():
    assert calculate(5, "-", 2) == 3


def test_multiplication():
    assert calculate(3, "*", 4) == 12


def test_division():
    assert calculate(10, "/", 2) == 5


def test_power():
    assert calculate(2, "**", 3) == 8


def test_modulo():
    assert calculate(10, "%", 3) == 1
