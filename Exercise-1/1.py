# Author: Manasvin Shrimali
# Date: 4-Sept-2024
# Exercise 1.1: Calculate the multiplication and sum of two numbers
def multiply_or_sum(a, b):
    product = a * b
    if product <= 1000:
        return product
    else:
        return a + b

# Example usage:
print(multiply_or_sum(20, 30))  # Output: 600
print(multiply_or_sum(40, 30))  # Output: 70
