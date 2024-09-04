# Author: Manasvin Shrimali
# Date: 4-Sept-2024
# Exercise 1.9: Check Palindrome Number
def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

print(is_palindrome_number(545))  # True
print(is_palindrome_number(123))  # False
