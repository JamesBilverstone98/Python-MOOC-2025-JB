# INPUT VALIDATION = ask user for integer numbers, program fails if 0, any other number print out square root

from math import sqrt
# needed for maths equations

while True:
    # user input
    numbers = int(input("Please type in a number: "))
   
    if numbers == 0: 
        break # if user input is 0, break out of loop and program

    elif numbers < 0:
        print("Invalid number") # for any numbers that are 0, print invalid
        continue

    print(sqrt(numbers)) # for all other inputs, do this maths calculation

print("Exiting...")
    


