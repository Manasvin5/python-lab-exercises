Author: Manasvin Shrimali
Author: Manasvin Shrimali
# Exercise 1: Accept numbers from a user
num = int(input("Enter a number: "))
print(f"You entered: {num}")

# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
print("Name", "Is", "James", sep="**")

# Exercise 3: Convert Decimal number to octal using print() output formatting
# Handles decimal input by converting to integer for octal conversion
decimal_num = int(float(input("Enter a decimal number (whole part will be considered for octal conversion): ")))
print(f"Octal representation: {oct(decimal_num)}")

# Exercise 4: Display float number with 2 decimal places using print()
float_num = float(input("Enter a float number: "))
print(f"Formatted float number: {float_num:.2f}")

# Exercise 5: Accept a list of 5 float numbers as an input from the user
float_list = []
for i in range(5):
    num = float(input(f"Enter float number {i+1}: "))
    float_list.append(num)
print(f"List of float numbers: {float_list}")

# Exercise 6: Write all content of a given file into a new file by skipping line number 5
input_file = 'input.txt'
output_file = 'output.txt'
try:
    with open(input_file, 'r') as file_in, open(output_file, 'w') as file_out:
        lines = file_in.readlines()
        for i, line in enumerate(lines):
            if i != 4:  # skipping line 5 (index 4)
                file_out.write(line)
    print(f"Content written to {output_file} excluding line 5.")
except FileNotFoundError:
    print(f"File {input_file} not found.")

# Exercise 7: Accept any three strings from one input() call
string1, string2, string3 = input("Enter three strings separated by spaces: ").split()
print(f"You entered: {string1}, {string2}, {string3}")

# Exercise 8: Format variables using a string.format() method
name = "Manasvin"
age = 21
print("My name is {} and I am {} years old.".format(name, age))

# Exercise 9: Check if file is empty or not
file_name = 'input.txt'
try:
    with open(file_name, 'r') as file:
        if file.read().strip():
            print(f"{file_name} is not empty.")
        else:
            print(f"{file_name} is empty.")
except FileNotFoundError:
    print(f"File {file_name} not found.")

# Exercise 10: Read line number 4 from the following file
try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        if len(lines) >= 4:
            print(f"Line 4: {lines[3]}")
        else:
            print("File has less than 4 lines.")
except FileNotFoundError:
    print(f"File {file_name} not found.")

