"""
operation
==========
Contains basic arithmetic operations: addition, subtraction, multiplication, division.
"""
from color import print_error


def add(a, b):
#    add two numbers
    return a + b

def subtract(a, b):
#   subtract two numbers
    return a - b


def multiply(a, b):
#   multiply two numbers
    return a * b


def divide(a, b):
#   divide two numbers
    if b == 0:
        print_error("You can't divide by zero!")
    return a / b 