# CALCULATOR = ask user for 2 numbers, depending on what operation, do the maths calculation for it

num1 = int(input("Number 1: "))  
num2 = int(input("Number 2: "))  
operator = input("Operation: ")

if operator == "add":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "subtract":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "multiply":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")