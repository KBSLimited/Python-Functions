#Task 1: Create functions for each arithmetic operation.

def add(x, y):
    """Function to perform addition."""
    return x + y

def subtract(x, y):
    """Function to perform subtraction."""
    return x - y

def multiply(x, y):
    """Function to perform multiplication."""
    return x * y

def divide(x, y):
    """Function to perform division."""
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Example usage:
a = 10
b = 5

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))

#Task 2: Implement user input to receive numbers and an operation choice.

def add(x, y):
    """Function to perform addition."""
    return x + y

def subtract(x, y):
    """Function to perform subtraction."""
    return x - y

def multiply(x, y):
    """Function to perform multiplication."""
    return x * y

def divide(x, y):
    """Function to perform division."""
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def get_operation_choice():
    """Function to get the user's choice of operation."""
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("Enter choice (1/2/3/4): ")
    return choice

# Get numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Get operation choice from the user
operation = get_operation_choice()

# Perform the selected operation
if operation == '1':
    print("Result:", add(num1, num2))
elif operation == '2':
    print("Result:", subtract(num1, num2))
elif operation == '3':
    print("Result:", multiply(num1, num2))
elif operation == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid operation choice")

#Task 3: Ensure your program can handle division by zero and other potential errors.

def add(x, y):
    """Function to perform addition."""
    return x + y

def subtract(x, y):
    """Function to perform subtraction."""
    return x - y

def multiply(x, y):
    """Function to perform multiplication."""
    return x * y

def divide(x, y):
    """Function to perform division."""
    try:
        result = x / y
    except ZeroDivisionError:
        return "Cannot divide by zero"
    else:
        return result

def get_operation_choice():
    """Function to get the user's choice of operation."""
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("Enter choice (1/2/3/4): ")
    return choice

# Get numbers from the user
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
else:
    # Get operation choice from the user
    operation = get_operation_choice()

    # Perform the selected operation
    if operation == '1':
        print("Result:", add(num1, num2))
    elif operation == '2':
        print("Result:", subtract(num1, num2))
    elif operation == '3':
        print("Result:", multiply(num1, num2))
    elif operation == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation choice")
