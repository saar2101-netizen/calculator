"""
stats
======
Basic statistical operations.
"""

def average(numbers):
#   Calculate the average of a group of numbers
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_max(numbers):
#   finding the biggest number
    if not numbers:
        return None
    return max(numbers)

def find_min(numbers):
#   finding the smallest numbers
    if not numbers:
        return None
    return min(numbers)
