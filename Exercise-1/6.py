# Exercise 6: Display numbers divisible by 5 from a list
def divisible_by_5(lst):
    return [num for num in lst if num % 5 == 0]

print(divisible_by_5([10, 20, 33, 46, 55]))  # [10, 20, 55]
