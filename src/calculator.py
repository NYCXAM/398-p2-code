"""
This file implement the basic calculator operations, including
addition, subtraction, multiplication, division, and modulus.
"""

# deleted excessive debug logging
def add(a, b):
    """Add two numbers."""
    result = a + b
    return result

def subtract(a, b):
    """Subtract b from a."""
    result = a - b
    return result

def multiply(a, b):
    """Multiply two numbers."""
    result = a * b
    return result

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    return result

def modulo(a, b):
    """Return remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    result = a % b
    return result

def power(a, b):
    """Raise a to the power of b."""
    return a ** b
# Experimental feature placeholder
