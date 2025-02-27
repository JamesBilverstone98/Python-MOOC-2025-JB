# ABSOLUTE VALUE = ask user for number, if number less than 0, times it by -1, otherwise print number normally

user_input = int(input("Please type in a number: ")) # user input

if user_input < 0:
    print(f"The absolute value of this number is {user_input * -1}") # for any inputs less than 0
else:
    print(f"The absolute value of this number is {user_input}") # any other inputs