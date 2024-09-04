# Author: Manasvin Shrimali
# Date: 4-Sept-2024
# Exercise 1.8: Print the following pattern
def print_pattern(n):
    for i in range(1, n + 1):
        print(" ".join([str(i)] * i))

print_pattern(5)
