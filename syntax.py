# FIX THE SYNTAX = Fix the provided syntax so that it is in order and the program works correctly

number = int(input("Please type in a number: ")) # user input

if number > 100: # for any input over 100
    print("The number was greater than one hundred")
    number - 100
    print("Now its value has decreased by one hundred")
    print(f"Its value is now {number - 100}")
    print(f"{number - 100} must be my lucky number!")
    print("Have a nice day!")
else: # for all other inputs
    print(f"{number} must be my lucky number!")
    print("Have a nice day!")