# Author: Manasvin Shrimali
# Date: 4-Sept-2024
# Exercise 1.5: Check if the first and last number of a list is the same
def is_first_and_last_same(lst):
    return lst[0] == lst[-1]

print(is_first_and_last_same([10, 20, 30, 10]))  # True
print(is_first_and_last_same([10, 20, 30, 40]))  # False
