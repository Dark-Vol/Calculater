from imports import math
from logger import logger

logger.info("Calculator started")
OPERATIONS = ["+", "-", "*", "/", "//", "**", "%"]


def round_multiply_divide_result(result):
    if result - math.floor(result) < 0.5:
        rounded_result = math.floor(result)
    elif result - math.floor(result) > 0.5:
        rounded_result = result
    else:
        rounded_result = math.ceil(result)
    return rounded_result


def parse_expression(expression):
    """Split a two-operand expression like '12+3' or '-2**4' into parts."""
    text = str(expression).replace(" ", "").replace("(", "").replace(")", "")
    operators = ["**", "//", "%", "*", "/", "+", "-"]
    start = 1 if text.startswith("-") else 0
    i = start
    while i < len(text):
        for op in operators:
            if text.startswith(op, i):
                left = text[:i]
                right = text[i + len(op) :]
                if left == "" or right == "":
                    raise ValueError("Incomplete expression")
                return float(left), op, float(right)
        i += 1
    raise ValueError("No operation found")


def calculate(first_num, operation, second_num):
    """Perform one arithmetic operation and return the result."""
    logger.debug(f"Input: {first_num} {operation} {second_num}")

    if operation not in OPERATIONS:
        logger.warning(f"Unknown operation: {operation}")
        raise ValueError("Unknown operation")

    if operation in ["/", "//", "%"] and second_num == 0:
        logger.error("Division by zero")
        raise ZeroDivisionError("Division by zero")

    if operation == "+":
        result = first_num + second_num
    elif operation == "-":
        result = first_num - second_num
    elif operation == "*":
        result = first_num * second_num
        rounded_result = round_multiply_divide_result(result)
        print("Result:", result)
        print("Rounded result:", rounded_result)
    elif operation == "/":
        result = first_num / second_num
        rounded_result = round_multiply_divide_result(result)
        print("Result:", result)
        print("Rounded result:", rounded_result)
    elif operation == "//":
        result = first_num // second_num
    elif operation == "**":
        result = first_num ** second_num
    elif operation == "%":
        result = first_num % second_num

    logger.success(f"Result: {result}")
    return result


if __name__ == "__main__":
    from gui import run

    run()
