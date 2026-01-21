from operations import add, subtract, multiply, divide
from advanced import power, square_root, modulo


print("Welcome to calculator")
print("==============================")


result1 = add(5, 3)
print(f"5 + 3 = {result1}")

result2 = subtract(10, 4)
print(f"10 - 4 = {result2}")

print(f"6 * 7 = {multiply(6, 7)}")
print(f"20 / 4 = {divide(20, 4)}")
print(f"10 / 10 = {divide(10, 10)}")

print("\n Advanced operations")

print(f"2 ^ 8 = {power(2, 8)}")
print(f"√16 = {square_root(16)}")
print(f"17 % 5 = {modulo(17, 5)}")
