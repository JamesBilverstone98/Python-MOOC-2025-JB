# NUMBERS = ask user for number, then print out all integer numbers greater than 0, but smaller than the input

upper_limit = int(input("Upper limit: "))
numbers = 1 # counter

while numbers < upper_limit: # whilst numbers is less than any input 
    print(numbers)
    numbers += 1 # print all numbers before the user input, in size order

