import imports

operations = ["+", "-", "*", "/", "//", "**", "%"]

# num1 = float(input("Enter num 1: "))
# num2 = float(input("Enter num 2: "))
# operation = input("Enter operetion: ")

# if operation == "+":
#     result = num1 + num2
#     print(result)
#     print(math.ceil(result))

def calculate(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ZeroDivisionError("Division by zero")
        return num1 / num2
    elif operation == "//":
        return num1 // num2
    elif operation == "**":
        return num1 ** num2
    elif operation == "%":
        return num1 % num2
    else:
        raise ValueError("Unknown operation")
