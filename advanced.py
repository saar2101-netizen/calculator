"""
advanced
==========
Contains advanced arithmetic operations: exponent, square root, modulo.
"""
def power(base, exponent):
#   number in power
    return base ** exponent


def square_root(n):
#   square root of a number
    if n < 0:
        return "ERROR: There is no square root to a minus number"
    return n ** 0.5


def modulo(a, b):
#   modulo of two numbers
    return a % b

def factorial(n):
#   Calculate the factorial of a number
    if n < 0:
        return "ERROR: There is no factorial for negative numbers "
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
