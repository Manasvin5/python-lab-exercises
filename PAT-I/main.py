Author: Manasvin Shrimali
# Q1: Calculate the commission for a salesman based on the monthly sale.
def calculate_commission(sales):
    if sales > 500000:
        return sales * 0.10
    elif sales > 250000:
        return sales * 0.05
    else:
        return sales * 0.025

# Q2: Find the grade based on score using "if-elif-else"
def find_grade(marks):
    if marks >= 90:
        return "S"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"

# Q3: Convert Celsius to Fahrenheit and compare with normal body temperature
def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    if fahrenheit > 98.6:
        return fahrenheit, "Above normal body temperature"
    elif fahrenheit < 98.6:
        return fahrenheit, "Below normal body temperature"
    else:
        return fahrenheit, "Normal body temperature"

# Q4: Print name and reg number using a while loop
def print_name_and_reg(name, reg_num):
    count = 0
    while count < 3:
        for _ in range(5):
            print(name)
        print(reg_num)
        count += 1

# Taking user inputs

# Q1: Sales input
sales = float(input("Enter the monthly sales in Rupees: "))
print(f"Commission for sales: Rs {calculate_commission(sales)}")

# Q2: Marks input
marks = int(input("Enter your marks: "))
print(f"Grade: {find_grade(marks)}")

# Q3: Celsius input
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit, temp_status = convert_to_fahrenheit(celsius)
print(f"Temperature in Fahrenheit: {fahrenheit}, Status: {temp_status}")

# Q4: Name and Registration Number input
name = input("Enter your name: ")
reg_num = input("Enter your registration number: ")
print_name_and_reg(name, reg_num)

