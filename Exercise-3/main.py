Author: Manasvin Shrimali
# Exercise 1: Print First 10 natural numbers using while loop
i = 1
while i <= 10:
    print(i, end=' ')
    i += 1
print()

# Exercise 2: Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# Exercise 3: Calculate the sum of all numbers from 1 to a given number
n = int(input("Enter a number: "))
total_sum = sum(range(1, n + 1))
print(f"Sum of numbers from 1 to {n}: {total_sum}")

# Exercise 4: Write a program to print multiplication table of a given number
num = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Exercise 5: Display numbers from a list using loop
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number, end=' ')
print()

# Exercise 6: Count the total number of digits in a number
number = int(input("Enter a number: "))
digit_count = len(str(number))
print(f"Total number of digits in {number}: {digit_count}")

# Exercise 7: Print the following pattern
# *
# * *
# * * *
# * * * *
# * * * * *
for i in range(1, 6):
    print('* ' * i)

# Exercise 8: Print list in reverse order using a loop
numbers = [10, 20, 30, 40, 50]
for i in range(len(numbers)-1, -1, -1):
    print(numbers[i], end=' ')
print()

# Exercise 9: Display numbers from -10 to -1 using for loop
for i in range(-10, 0):
    print(i, end=' ')
print()

# Exercise 10: Use else block to display a message “Done” after successful execution of for loop
for i in range(5):
    print(i, end=' ')
else:
    print("\nDone")

# Exercise 11: Write a program to display all prime numbers within a range
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=' ')
print()

# Exercise 12: Display Fibonacci series up to 10 terms
a, b = 0, 1
print(a, b, end=' ')
for _ in range(8):
    a, b = b, a + b
    print(b, end=' ')
print()

# Exercise 13: Find the factorial of a given number
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num}: {factorial}")

# Exercise 14: Reverse a given integer number
num = int(input("Enter a number to reverse: "))
reversed_num = int(str(num)[::-1])
print(f"Reversed number: {reversed_num}")

# Exercise 15: Use a loop to display elements from a given list present at odd index positions
numbers = [10, 20, 30, 40, 50, 60, 70]
for i in range(1, len(numbers), 2):
    print(numbers[i], end=' ')
print()

# Exercise 16: Calculate the cube of all numbers from 1 to a given number
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(f"Cube of {i}: {i ** 3}")

# Exercise 17: Find the sum of the series upto n terms
n = int(input("Enter the number of terms: "))
sum_series = sum(range(1, n + 1))
print(f"Sum of series upto {n} terms: {sum_series}")

# Exercise 18: Print the following pattern [Reverse of E-2]
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

