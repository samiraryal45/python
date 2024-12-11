# A simple calculator program with file logging

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def log_to_file(operation, a, b, result):
    with open("calculator_log.txt", "a") as file:
        file.write(f"{operation}: {a}, {b} = {result}\n")

print("Welcome to the Python Calculator!")
print("Choose an operation: add, subtract, multiply, divide")

while True:
    operation = input("Enter operation (or 'exit' to quit): ").lower()
    if operation == "exit":
        print("Goodbye!")
        break

    if operation in ["add", "subtract", "multiply", "divide"]:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if operation == "add":
                result = add(num1, num2)
            elif operation == "subtract":
                result = subtract(num1, num2)
            elif operation == "multiply":
                result = multiply(num1, num2)
            elif operation == "divide":
                result = divide(num1, num2)

            print(f"Result: {result}")
            log_to_file(operation, num1, num2, result)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    else:
        print("Invalid operation. Please try again.")
