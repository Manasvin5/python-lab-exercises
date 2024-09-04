def multiply_or_sum(a, b):
    product = a * b
    if product <= 1000:
        return product
    else:
        return a + b

# Example usage:
print(multiply_or_sum(20, 30))  # Output: 600
print(multiply_or_sum(40, 30))  # Output: 70
