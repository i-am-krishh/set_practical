"""
This module provides basic calculator functions for arithmetic operations
and finding the maximum of three numbers.
"""

def add(x, y):
    """Add two numbers and return the result."""
    return x + y

def subtract(x, y):
    """Subtract the second number from the first and return the result."""
    return x - y

def multiply(x, y):
    """Multiply two numbers and return the result."""
    return x * y

def divide(x, y):
    """Divide the first number by the second and return the result.
    
    Raises:
        ValueError: If the second number is zero.
    """
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y

def maximum_of_three(x, y, z):
    """Return the maximum of three numbers."""
    return max(x, y, z)
