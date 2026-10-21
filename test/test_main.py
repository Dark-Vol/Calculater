
import math

import pytest

from main import (
    calculate_expression,
    format_result,
    round_multiply_divide_result,
    positive,
    positive_integer,
    root,
    triangle_area_sides,
    polygon_area,
    ap_term,
    ap_sum,
    gp_term,
    gp_sum,
)


# ==========================================
# 1. Арифметические операции
# ==========================================

@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("2 + 3", 5),
        ("10 - 4", 6),
        ("3 * 4", 12),
        ("12 / 3", 4),
        ("13 // 5", 2),
        ("13 % 5", 3),
        ("2 ** 3", 8),
        ("2 ** -2", 0.25),
        ("-5 + 2", -3),
        ("(2 + 3) * 4", 20),
        ("2 + 3 * 4", 14),
        ("--5", 5),
    ],
)
def test_arithmetic(expression, expected):
    assert calculate_expression(expression) == pytest.approx(expected)


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate_expression("10 / 0")


def test_floor_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate_expression("10 // 0")


def test_modulo_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate_expression("10 % 0")


# ==========================================
# 2. Константы
# ==========================================

def test_pi_constant():
    assert calculate_expression("pi") == pytest.approx(math.pi)


def test_e_constant():
    assert calculate_expression("e") == pytest.approx(math.e)


def test_tau_constant():
    assert calculate_expression("tau") == pytest.approx(math.tau)


# ==========================================
# 3. Корни и степени
# ==========================================

def test_square_root():
    assert calculate_expression("sqrt(144)") == pytest.approx(12)


def test_cube_root_positive():
    assert calculate_expression("cbrt(27)") == pytest.approx(3)


def test_cube_root_negative():
    assert calculate_expression("cbrt(-8)") == pytest.approx(-2)


def test_root():
    assert root(27, 3) == pytest.approx(3)


def test_even_root_of_negative_number():
    with pytest.raises(ValueError):
        root(-16, 2)


def test_odd_root_of_negative_number():
    assert root(-27, 3) == pytest.approx(-3)


def test_root_degree_zero():
    with pytest.raises(ValueError):
        root(25, 0)


def test_absolute_value():
    assert calculate_expression("abs(-15)") == 15


def test_factorial():
    assert calculate_expression("factorial(5)") == 120


# ==========================================
# 4. Логарифмы и экспоненты
# ==========================================

@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("ln(e)", 1),
        ("log10(100)", 2),
        ("log2(8)", 3),
        ("log(1000, 10)", 3),
        ("exp(0)", 1),
    ],
)
def test_logarithms_and_exponents(expression, expected):
    assert calculate_expression(expression) == pytest.approx(expected)


def test_logarithm_of_zero():
    with pytest.raises(ValueError):
        calculate_expression("ln(0)")


def test_logarithm_of_negative_number():
    with pytest.raises(ValueError):
        calculate_expression("log10(-5)")


# ==========================================
# 5. Тригонометрия
# ==========================================

def test_sin_radians():
    assert calculate_expression("sin(pi / 2)") == pytest.approx(1)


def test_cos_radians():
    assert calculate_expression("cos(0)") == pytest.approx(1)


def test_sin_degrees():
    assert calculate_expression("sind(90)") == pytest.approx(1)


def test_cos_degrees():
    assert calculate_expression("cosd(180)") == pytest.approx(-1)


def test_inverse_sine():
    assert calculate_expression("asin(1)") == pytest.approx(math.pi / 2)


# ==========================================
# 6. Округление и форматирование
# ==========================================

@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (2.4, 2),
        (2.5, 3),
        (2.51, 3),
        (3.9, 4),
        (-2.4, -2),
        (-2.5, -3),
        (-2.51, -3),
        (-3.9, -4),
        (0, 0),
    ],
)
def test_rounding(value, expected):
    assert round_multiply_divide_result(value) == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (5.0, "5"),
        (5.25, "5.25"),
        (0.000001, "1e-06"),
        (12, "12"),
        (-3.5, "-3.5"),
    ],
)
def test_format_result(value, expected):
    assert format_result(value) == expected


# ==========================================
# 7. Геометрия
# ==========================================

def test_circle_area():
    assert calculate_expression("circle_area(2)") == pytest.approx(
        math.pi * 4
    )


def test_circle_circumference():
    assert calculate_expression("circle_circumference(3)") == pytest.approx(
        2 * math.pi * 3
    )


def test_rectangle_area():
    assert calculate_expression("rectangle_area(4, 5)") == 20


def test_rectangle_perimeter():
    assert calculate_expression("rectangle_perimeter(4, 5)") == 18


def test_triangle_area():
    assert calculate_expression("triangle_area(10, 4)") == 20


def test_triangle_area_by_sides():
    assert triangle_area_sides(3, 4, 5) == pytest.approx(6)


def test_invalid_triangle():
    with pytest.raises(ValueError):
        triangle_area_sides(1, 2, 10)


def test_triangle_with_zero_side():
    with pytest.raises(ValueError):
        triangle_area_sides(0, 4, 5)


def test_polygon_area_square():
    assert polygon_area(4, 2) == pytest.approx(4)


def test_polygon_with_too_few_sides():
    with pytest.raises(ValueError):
        polygon_area(2, 5)


def test_polygon_with_zero_side():
    with pytest.raises(ValueError):
        polygon_area(5, 0)


# ==========================================
# 8. Объёмы и площади тел
# ==========================================

def test_cube_volume():
    assert calculate_expression("cube_volume(3)") == 27


def test_cube_area():
    assert calculate_expression("cube_area(3)") == 54


def test_cuboid_volume():
    assert calculate_expression("cuboid_volume(2, 3, 4)") == 24


def test_cuboid_area():
    assert calculate_expression("cuboid_area(2, 3, 4)") == 52


def test_sphere_volume():
    assert calculate_expression("sphere_volume(3)") == pytest.approx(
        36 * math.pi
    )


def test_sphere_area():
    assert calculate_expression("sphere_area(3)") == pytest.approx(
        36 * math.pi
    )


def test_cylinder_volume():
    assert calculate_expression("cylinder_volume(2, 5)") == pytest.approx(
        20 * math.pi
    )


def test_cone_volume():
    assert calculate_expression("cone_volume(3, 4)") == pytest.approx(
        12 * math.pi
    )


def test_pyramid_volume():
    assert calculate_expression("pyramid_volume(12, 6)") == 24


def test_negative_radius():
    with pytest.raises(ValueError):
        calculate_expression("circle_area(-2)")


# ==========================================
# 9. Арифметическая прогрессия
# ==========================================

def test_ap_term():
    assert ap_term(2, 3, 5) == 14


def test_ap_sum():
    assert ap_sum(2, 3, 5) == 40


def test_ap_first_term():
    assert ap_term(10, 2, 1) == 10


# ==========================================
# 10. Геометрическая прогрессия
# ==========================================

def test_gp_term():
    assert gp_term(2, 3, 4) == 54


def test_gp_sum():
    assert gp_sum(2, 3, 4) == 80


def test_gp_sum_ratio_one():
    assert gp_sum(5, 1, 4) == 20


def test_gp_first_term():
    assert gp_term(7, 2, 1) == 7


# ==========================================
# 11. Проверка аргументов
# ==========================================

def test_positive_valid_value():
    assert positive(5) == 5


@pytest.mark.parametrize("value", [0, -1, -5.5])
def test_positive_invalid_value(value):
    with pytest.raises(ValueError):
        positive(value)


def test_positive_integer_valid():
    assert positive_integer(5) == 5


def test_positive_integer_float():
    assert positive_integer(5.0) == 5


@pytest.mark.parametrize("value", [0, -1, 2.5])
def test_positive_integer_invalid(value):
    with pytest.raises(ValueError):
        positive_integer(value)


# ==========================================
# 12. Безопасность разбора выражений
# ==========================================

def test_unknown_function():
    with pytest.raises(ValueError):
        calculate_expression("unknown_function(5)")


def test_unknown_constant():
    with pytest.raises(ValueError):
        calculate_expression("unknown_constant")


def test_import_is_not_allowed():
    with pytest.raises((ValueError, TypeError, SyntaxError)):
        calculate_expression("__import__('os')")


def test_attribute_access_is_not_allowed():
    with pytest.raises((ValueError, TypeError, SyntaxError)):
        calculate_expression("math.sqrt(16)")


def test_named_arguments_are_not_allowed():
    with pytest.raises(ValueError):
        calculate_expression("log(x=100)")


def test_large_exponent_is_rejected():
    with pytest.raises(ValueError):
        calculate_expression("2 ** 10001")


def test_invalid_syntax():
    with pytest.raises(SyntaxError):
        calculate_expression("2 +")
