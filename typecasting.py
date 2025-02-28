# TYPECASTING = ask for user input for a float number, then print integer and decimal part separately 

user_input = float(input("Please type in a number: ")) # user input

integer = int(user_input)
decimal = user_input - integer # conversion for the float part of the input

print(f"Integer part: {integer}")
print(f"Decimal part: {decimal}")