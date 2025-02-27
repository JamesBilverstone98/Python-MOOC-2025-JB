# LOYALTY = ask user for input, depending on how many points they have, they get certain bonus %

points = int(input("How many points are on your card? "))
discount1 = points * 1.1 # calculation 1 for points less than 100
discount2 = points * 1.15 # calculation 2 for points more than 100

if points < 100: # if user input is less than 100
    print("Your bonus is 10 %")
    print(f"You now have {discount1} points")
else: # any other input
    print("Your bonus is 15 %")
    print(f"You now have {discount2} points")