# Author: Manasvin Shrimali
# Date: 4-Sept-2024

# Exercise 1.10: Create a new list from two lists using the following condition
def create_new_list(list1, list2):
    new_list = [x for x in list1 if x % 2 != 0] + [x for x in list2 if x % 2 == 0]
    return new_list

print(create_new_list([10, 20, 25, 30, 35], [40, 45, 60, 75, 90]))  # [25, 35, 40, 60, 90]
