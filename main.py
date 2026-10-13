from imports import math
from logger import logger

logger.info("Calculator started")
operations = ["+", "-", "*", "/", "//", "**", "%"]

try:
    # Enter first number
    first_num = float(input("Enter first: "))
    
    # Enter operation from operations
    operation = input("Enter operation: ")
    
    # Enter second number
    second_num = float(input("Enter second: "))

    # Logs the first number, arithmetic operator, and second number entered by the user
    logger.debug(f"Input: {first_num} {operation} {second_num}")

    
    # Check whether the entered operator is supported
    if operation not in operations:
        # Log a warning if the operator is unknown
        logger.warning(f"Unknown operation: {operation}")
        print("Unknown operation")

    # Check whether the user is trying to divide by zero
    elif operation in ["/", "//", "%"] and second_num == 0:
        # Log an error because division by zero is not allowed
        logger.error("Division by zero")
        print("Error: division by zero!")

    else:
        # Perform addition
        if operation == "+":
            result = first_num + second_num

        # Perform subtraction
        elif operation == "-":
            result = first_num - second_num


        # Perform multiplication
        elif operation == "*":
            result = first_num * second_num

            if result - math.floor(result) < 0.5:
                rounded_result = math.floor(result)
                print("Rounded result:", rounded_result)
            elif result - math.floor(result) > 0.5:
                print("Result:", result)
            else:
                rounded_result = math.ceil(result)
                print("Rounded result:", rounded_result)
            # print("Result:", result)

        # Perform division
        elif operation == "/":
            result = first_num / second_num

            if result - math.floor(result) < 0.5:
                rounded_result = math.floor(result)
                print("Rounded result:", rounded_result)
            elif result - math.floor(result) > 0.5:
                print("Result:", result)
            else:
                rounded_result = math.ceil(result)
                print("Rounded result:", rounded_result)

            # print("Result:", result)

        # Perform floor division (round down to an integer quotient)
        elif operation == "//":
            result = first_num // second_num

        # Raise the first number to the power of the second number
        elif operation == "**":
            result = first_num ** second_num

        # Calculate the remainder after division
        elif operation == "%":
            result = first_num % second_num

        # Log the successful calculation and its result
        logger.success(f"Result: {result}")
        print("Result:", result)

# Handle invalid number input, such as entering letters instead of numbers
except ValueError:
    logger.exception("Invalid number entered")
    print("Error: please enter valid numbers")

    # Log a message when the calculator finishes running
    logger.info("Calculator finished")
