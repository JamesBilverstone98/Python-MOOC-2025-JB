# ORDER OF MAGNITUDE = ask user for number, program then prints whether its smaller than certain numbers

user_input = int(input("Please type in a number: ")) # user input

if user_input > 1000: # if user input is more than 1000
    print("Thank you!")
elif user_input > 100: # if user input is more than 100
    print("This number is smaller than 1000")
    print("Thank you!")
elif user_input > 10: # if user input is more than 100
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("Thank you!")
else: # any other input
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("This number is smaller than 10")
    print("Thank you!")