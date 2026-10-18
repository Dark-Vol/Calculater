from imports import math
from imports import ast
from imports import operator
from imports import logging

logger = logging.getLogger("calculator")
logging.basicConfig(level=logging.INFO)

# Арифметические операции
BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


# ---------- Проверки аргументов ----------

def positive(value, name="value"):
    if value <= 0:
        raise ValueError(f"{name} должен быть больше нуля")
    return value


def positive_integer(value, name="n"):
    if not isinstance(value, (int, float)) or not value.is_integer() if isinstance(value, float) else False:
        raise ValueError(f"{name} должен быть целым числом")

    if value < 1:
        raise ValueError(f"{name} должен быть не меньше 1")

    return int(value)


def root(value, degree):
    if degree == 0:
        raise ValueError("Степень корня не может быть равна нулю")

    if value < 0:
        if not float(degree).is_integer() or int(degree) % 2 == 0:
            raise ValueError("Для отрицательного числа нужен нечётный целый корень")
        return -((-value) ** (1 / degree))

    return value ** (1 / degree)


def triangle_area_sides(a, b, c):
    if min(a, b, c) <= 0:
        raise ValueError("Стороны должны быть положительными")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Такие стороны не образуют треугольник")

    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def polygon_area(n, side):
    n = positive_integer(n, "Количество сторон")

    if n < 3:
        raise ValueError("У многоугольника должно быть минимум 3 стороны")

    positive(side, "Сторона")
    return n * side ** 2 / (4 * math.tan(math.pi / n))


# ---------- Арифметические прогрессии ----------

def ap_term(a, d, n):
    n = positive_integer(n)
    return a + (n - 1) * d


def ap_sum(a, d, n):
    n = positive_integer(n)
    return n * (2 * a + (n - 1) * d) / 2


# ---------- Геометрические прогрессии ----------

def gp_term(a, q, n):
    n = positive_integer(n)
    return a * q ** (n - 1)


def gp_sum(a, q, n):
    n = positive_integer(n)

    if q == 1:
        return a * n

    return a * (q ** n - 1) / (q - 1)


# ---------- Математические функции ----------

FUNCTIONS = {
    # Корни, степени и числа
    "sqrt": math.sqrt,
    "cbrt": lambda x: math.copysign(abs(x) ** (1 / 3), x),
    "root": root,
    "pow": pow,
    "abs": abs,
    "factorial": math.factorial,
    "ceil": math.ceil,
    "floor": math.floor,
    "round": round,
    "gcd": math.gcd,
    "lcm": math.lcm,

    # Логарифмы и экспоненты
    "ln": math.log,
    "log": lambda x, base=10: math.log(x, base),
    "log10": math.log10,
    "log2": math.log2,
    "exp": math.exp,

    # Тригонометрия: sin/cos/tan работают с радианами
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,

    # Тригонометрия в градусах
    "sind": lambda x: math.sin(math.radians(x)),
    "cosd": lambda x: math.cos(math.radians(x)),
    "tand": lambda x: math.tan(math.radians(x)),

    # Геометрия: плоские фигуры
    "circle_area": lambda r: math.pi * positive(r, "Радиус") ** 2,
    "circle_circumference": lambda r: 2 * math.pi * positive(r, "Радиус"),
    "rectangle_area": lambda a, b: positive(a, "a") * positive(b, "b"),
    "rectangle_perimeter": lambda a, b: 2 * (positive(a, "a") + positive(b, "b")),
    "triangle_area": lambda b, h: positive(b, "Основание") * positive(h, "Высота") / 2,
    "triangle_area_sides": triangle_area_sides,
    "trapezoid_area": lambda a, b, h: (positive(a) + positive(b)) * positive(h) / 2,
    "polygon_area": polygon_area,

    # Объёмы и поверхности тел
    "cube_volume": lambda a: positive(a, "Сторона") ** 3,
    "cube_area": lambda a: 6 * positive(a, "Сторона") ** 2,
    "cuboid_volume": lambda a, b, c: positive(a) * positive(b) * positive(c),
    "cuboid_area": lambda a, b, c: 2 * (a * b + a * c + b * c),
    "sphere_volume": lambda r: 4 * math.pi * positive(r, "Радиус") ** 3 / 3,
    "sphere_area": lambda r: 4 * math.pi * positive(r, "Радиус") ** 2,
    "cylinder_volume": lambda r, h: math.pi * positive(r) ** 2 * positive(h),
    "cylinder_area": lambda r, h: 2 * math.pi * positive(r) * (positive(r) + positive(h)),
    "cone_volume": lambda r, h: math.pi * positive(r) ** 2 * positive(h) / 3,
    "cone_area": lambda r, l: math.pi * positive(r) * (positive(r) + positive(l)),
    "prism_volume": lambda base, h: positive(base) * positive(h),
    "pyramid_volume": lambda base, h: positive(base) * positive(h) / 3,

    # Прогрессии
    "ap_term": ap_term,
    "ap_sum": ap_sum,
    "gp_term": gp_term,
    "gp_sum": gp_sum,
}

CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
    "tau": math.tau,
}


# ---------- Безопасный разбор выражения ----------

def evaluate_node(node):
    if isinstance(node, ast.Expression):
        return evaluate_node(node.body)

    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value

    if isinstance(node, ast.Name):
        if node.id in CONSTANTS:
            return CONSTANTS[node.id]
        raise ValueError(f"Неизвестная константа: {node.id}")

    if isinstance(node, ast.BinOp) and type(node.op) in BINARY_OPERATORS:
        left = evaluate_node(node.left)
        right = evaluate_node(node.right)

        if isinstance(node.op, ast.Pow) and abs(right) > 10000:
            raise ValueError("Слишком большая степень")

        return BINARY_OPERATORS[type(node.op)](left, right)

    if isinstance(node, ast.UnaryOp) and type(node.op) in UNARY_OPERATORS:
        return UNARY_OPERATORS[type(node.op)](evaluate_node(node.operand))

    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
        name = node.func.id

        if name not in FUNCTIONS:
            raise ValueError(f"Неизвестная функция: {name}")

        if node.keywords:
            raise ValueError("Именованные аргументы не поддерживаются")

        args = [evaluate_node(arg) for arg in node.args]
        return FUNCTIONS[name](*args)

    raise ValueError("Неподдерживаемое выражение")


def calculate_expression(expression):
    logger.info("Expression: %s", expression)

    tree = ast.parse(expression, mode="eval")
    result = evaluate_node(tree)

    if isinstance(result, float) and not math.isfinite(result):
        raise ValueError("Результат не является конечным числом")

    logger.info("Result: %s", result)
    return result


def format_result(result):
    if isinstance(result, float):
        if result.is_integer():
            return str(int(result))
        return f"{result:.12g}"

    return str(result)


def round_multiply_divide_result(result):
    # Округление до ближайшего целого; половины — от нуля.
    if result >= 0:
        return math.floor(result + 0.5)

    return math.ceil(result - 0.5)