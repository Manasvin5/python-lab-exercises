def sum_of_current_and_previous():
    previous_num = 0
    for i in range(1, 11):
        current_sum = previous_num + i
        print(f"Current Number: {i}, Previous Number: {previous_num}, Sum: {current_sum}")
        previous_num = i

# Example:
sum_of_current_and_previous()

