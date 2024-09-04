# Exercise 8: Print the following pattern
def print_pattern(n):
    for i in range(1, n + 1):
        print(" ".join([str(i)] * i))

print_pattern(5)
