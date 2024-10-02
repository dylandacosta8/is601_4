import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation

def calculate_and_print(a, b, operation_name):
    """Perform the calculation and print the result."""
    calculator = Calculator()  # Create an instance of Calculator

    operation_mappings = {
        'add': calculator.add,       # Use instance methods
        'subtract': calculator.subtract,
        'multiply': calculator.multiply,
        'divide': calculator.divide
    }

    try:
        # Convert inputs to Decimal for precision handling
        a_decimal = Decimal(a)
        b_decimal = Decimal(b)

        # Perform the operation using the instance method
        result_function = operation_mappings.get(operation_name)
        
        if result_function:  # Check if the operation is valid
            result = result_function(float(a_decimal), float(b_decimal))  # Convert to float
            print(f"The result of {a} {operation_name} {b} is equal to {result}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main entry point for the calculator application."""
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    _, a, b, operation = sys.argv  # Unpack command-line arguments
    calculate_and_print(a, b, operation)  # Perform the calculation

if __name__ == '__main__':
    main()
