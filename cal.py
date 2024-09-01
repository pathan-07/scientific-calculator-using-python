import logging
import math

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        logging.error("Attempted to divide by zero.")
        raise ValueError("Division by zero is not allowed.")
    return a / b

def modulus(a, b):
    return a % b

def exponentiate(a, b):
    return a ** b

def logarithm(a, base=10):
    if a <= 0:
        logging.error("Attempted to take logarithm of non-positive number.")
        raise ValueError("Logarithm of non-positive number is not allowed.")
    return math.log(a, base)

def square_root(a):
    if a < 0:
        logging.error("Attempted to take square root of negative number.")
        raise ValueError("Square root of negative number is not allowed.")
    return math.sqrt(a)

def sine(a):
    return math.sin(math.radians(a))

def cosine(a):
    return math.cos(math.radians(a))

def tangent(a):
    return math.tan(math.radians(a))

def get_operation_choice():
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Logarithm")
    print("8. Square Root")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("12. Exit")
    return input("Enter the operation (1/2/3/4/5/6/7/8/9/10/11/12): ")

def get_numbers(single_input=False):
    while True:
        try:
            if single_input:
                num1 = float(input("Enter the number: "))
                return num1, None
            else:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            logging.warning("Invalid numeric input encountered.")

def calculator():
    print("Simple Calculator")

    while True:
        operation = get_operation_choice()

        if operation == '12':
            confirm_exit = input("Are you sure you want to exit? (yes/no): ").lower()
            if confirm_exit == 'yes':
                print("Exiting the calculator. Goodbye!")
                logging.info("Calculator session ended by user.")
                break
            else:
                continue

        if operation not in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'}:
            print("Invalid operation choice. Please select a valid option.")
            logging.warning("Invalid operation choice.")
            continue

        if operation in {'7', '8', '9', '10', '11'}:
            num1, _ = get_numbers(single_input=True)
            num2 = None  # Explicitly set num2 to None for single input operations
        else:
            num1, num2 = get_numbers()

        try:
            if operation == '1':
                result = add(num1, num2)
                print(f"The result of {num1} + {num2} is: {result}")
            elif operation == '2':
                result = subtract(num1, num2)
                print(f"The result of {num1} - {num2} is: {result}")
            elif operation == '3':
                result = multiply(num1, num2)
                print(f"The result of {num1} * {num2} is: {result}")
            elif operation == '4':
                result = divide(num1, num2)
                print(f"The result of {num1} / {num2} is: {result}")
            elif operation == '5':
                result = modulus(num1, num2)
                print(f"The result of {num1} % {num2} is: {result}")
            elif operation == '6':
                result = exponentiate(num1, num2)
                print(f"The result of {num1} ^ {num2} is: {result}")
            elif operation == '7':
                base = float(input("Enter the base for logarithm (default is 10): ") or 10)
                result = logarithm(num1, base)
                print(f"The result of log base {base} of {num1} is: {result}")
            elif operation == '8':
                result = square_root(num1)
                print(f"The result of sqrt({num1}) is: {result}")
            elif operation == '9':
                result = sine(num1)
                print(f"The result of sin({num1}) is: {result}")
            elif operation == '10':
                result = cosine(num1)
                print(f"The result of cos({num1}) is: {result}")
            elif operation == '11':
                result = tangent(num1)
                print(f"The result of tan({num1}) is: {result}")
            
            logging.info(f"Operation: {operation}, Numbers: {num1}, {num2 if num2 is not None else 'N/A'}, Result: {result}")
        except ValueError as e:
            print(e)
            logging.error(f"Error during calculation: {e}")

# Call the calculator function
calculator()