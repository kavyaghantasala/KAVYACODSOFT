def get_number(prompt):
    """Prompt user for a number and validate it."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

def get_operation():
    """Prompt user for an operation and validate it."""
    valid_operations = ['+', '-', '*', '/']
    while True:
        operation = input("Enter operation (+, -, *, /): ").strip()
        if operation in valid_operations:
            return operation
        print("Error: Please enter a valid operation (+, -, *, /).")

def calculate(num1, num2, operation):
    """Perform the calculation based on the operation."""
    try:
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return num1 / num2
    except ZeroDivisionError as e:
        raise e

def main():
    """Main function to run the calculator."""
    print("Simple Calculator")
    print("----------------")

    # Get inputs
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = get_operation()

    # Perform calculation
    try:
        result = calculate(num1, num2, operation)
        print(f"\nResult: {num1} {operation} {num2} = {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()