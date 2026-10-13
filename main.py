
from logger import logger

logger.info("Calculator started")

operations = ["+", "-", "*", "/", "//", "**", "%"]

try:
    num1 = float(input("Enter number 1: "))
    operation = input("Enter operation: ")
    num2 = float(input("Enter number 2: "))

    logger.debug(f"Input: {num1} {operation} {num2}")

    if operation not in operations:
        logger.warning(f"Unknown operation: {operation}")
        print("Unknown operation!")

    elif operation in ["/", "//", "%"] and num2 == 0:
        logger.error("Division by zero")
        print("Error: division by zero!")

    else:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        elif operation == "//":
            result = num1 // num2
        elif operation == "**":
            result = num1 ** num2
        elif operation == "%":
            result = num1 % num2

        logger.success(f"Result: {result}")
        print("Result:", result)

except ValueError:
    logger.exception("Invalid number entered")
    print("Error: please enter valid numbers")

logger.info("Calculator finished")
