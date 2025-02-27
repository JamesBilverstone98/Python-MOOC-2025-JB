# SOUP OR NO SOUP = ask user for name, if name anything other than Jerry, program prints out certain stuff

user_input = input("Please tell me your name: ") # user input

if user_input == "Jerry":
    print("Next please!") # if user input is Jerry 
else:
    soup = int(input("How many portions of soup? ")) # for any other inputs other than Jerry
    print(f"The total cost is {soup * 5.90}")
    print("Next please!")