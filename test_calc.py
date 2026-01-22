""" test to calculator"""

from operations import add, subtract, multiply, divide
from advanced import power, square_root

# basic operations test

assert add(2,3) == 5, "Add fail"
assert subtract(10, 4) == 6, "sub fail"
assert multiply(3,4) == 12, "mul fail"
assert divide(20, 4) == 5, "div fail"


# Advance operations test

assert power(2,3) == 8, "power fail"
assert square_root(16) == 4, "square root fail"