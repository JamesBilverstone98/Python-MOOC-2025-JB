# WORKING WITH NUMBERS = ask user for integer numbers, keep asking for numbers until user enters 0
# then print out how many numbers were typed in, the sum, the mean, and how many positive and negative

print("Please type in integer numbers. Type in 0 to finish.")
attempts = 0 # counter for amount of numbers entered
added_together = 0
mean = 0
positive = 0 # counter for positive numbers
negative = 0 # counter for negative numbers

while True:
    number = int(input("Number: "))
    attempts += 1 # counter starts for input
    
    if number == 0:
        break # once user enters 0, exit program
    
    if number < 0:
        negative += 1 # counter starts for negative numbers
        
    if number > 0:
        positive += 1 # counter starts for positive numbers
        
    added_together += int(number) # calculation for sum
    mean = added_together / attempts # calculation for mean
    
    
print("... the program asks for numbers")
print(f"Numbers typed in {attempts - 1}") # this removes the 0 which will be entered
print(f"The sum of the numbers is {added_together}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")