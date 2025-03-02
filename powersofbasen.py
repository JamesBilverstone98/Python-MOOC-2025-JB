# POWERS OF BASE N = similar to previous powers of 2 program, this time ask user for base (multiplication amount)

upper_limit = int(input("Upper limit: ")) # user input for maximum number
base = int(input("Base: ")) # user input for multiplication amount
numbers = 1 # counter starts from 1

while numbers <= upper_limit: # while the counter is less than or equal to the upper limit number
    print(numbers) 
    numbers *= base # numbers multiplied by whatever base user gives