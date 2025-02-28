# GREATER THAN OR EQUAL TO = aks for 2 numbers, print out which is more

num1 = int(input("Please type in the first number: "))
num2 = int(input("Please type in another number: "))    

if num1 > num2: # if first input is more than the second
    print(f"The greater number was {num1}")
elif num1 < num2: # if second input is more than the first
    print(f"The greater number was {num2} ")
else: # draw
    print("The numbers are equal!")