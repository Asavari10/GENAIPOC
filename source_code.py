# source_code.py
def add_numbers(a, b):
    """Add two numbers and return the result."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b

def subtract_numbers(a, b):
    """Subtract two numbers and return the result."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a - b

def divide_numbers(a, b):
    """Divide two numbers and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_even(number):
    """Check if a number is even."""
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    return number % 2 == 0

class Calculator:
    def __init__(self):
        self.history = []
    
    def calculate(self, operation, a, b):
        if operation == "add":
            result = add_numbers(a, b)
        elif operation == "subtract":
            result = subtract_numbers(a, b)
        elif operation == "divide":
            result = divide_numbers(a, b)
        else:
            raise ValueError("Unsupported operation")
        
        self.history.append(f"{a} {operation} {b} = {result}")
        return result
    
    def get_history(self):
        return self.history