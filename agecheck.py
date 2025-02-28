# AGE CHECK = ask user for age, depending on age, print out responses

age = int(input("What is your age? ")) # user input for age

if age >= 5:
    print(f"Ok, you're {age} years old") # if input is 5 or greater
elif age < 0:
    print("That must be a mistake") # input less than 0
else:
    print("I suspect you can't write quite yet...") # any age between 0 and 4