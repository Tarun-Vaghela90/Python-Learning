def function_demo():
    return "Hello, welcome to the function demo! This is an example of a function with output."

def add(a, b):
        return a + b

def subtract(a, b):
        return a - b

def multiply(a, b):
        return a * b

def divide(a, b):
    if b != 0:
            return a / b
    else:
            return "Division by zero is not allowed."

def greet(name):
        return f"Hello, {name}! Welcome to learning Python functions with output."

print(function_demo())
print(add(5, 3))          # Output: 8           
print(subtract(10, 4))    # Output: 6
print(multiply(2, 3))      # Output: 6

print(divide(8, 2))        # Output: 4.0
print(divide(8, 0))        # Output: Division by zero is not allowed.
print(greet("Alice"))      # Output: Hello, Alice! Welcome to learning Python functions with output.
# Output: Hello, welcome to the function demo! This is an example of a function with output.