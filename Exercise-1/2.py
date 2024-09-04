# Author: Manasvin Shrimali
# Date: 4-Sept-2024
# Exercise 1.2: Print the sum of the current number and the previous number
def sum_of_current_and_previous():
    previous_num = 0
    for i in range(1, 11):
        current_sum = previous_num + i
        print(f"Current Number: {i}, Previous Number: {previous_num}, Sum: {current_sum}")
        previous_num = i

# Example:
sum_of_current_and_previous()

