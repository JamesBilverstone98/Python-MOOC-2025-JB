# NUMBER OF CHARACTERS = ask for user input which then prints out number of characters if there was more than 1

user_input = input("Please type in a word: ") # user input

if len(user_input) == 1: # for all input which only has 1 letter
    print("Thank you!")
else: # for any other inputs
    print(f"There are {len(user_input)} letters in the word {user_input}") # len function counts the amount of characters
    print("Thank you!")
      