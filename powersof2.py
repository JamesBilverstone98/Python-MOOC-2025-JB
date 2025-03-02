# POWERS OF TWO = ask user for upper limit, program then prints out numbers that each subsequent number is the previous one doubled, starting from 1

upper_limit = int(input("Upper limit: ")) # user input for number
numbers = 1 # counter starts from 1

while numbers <= upper_limit: # while the counter is less than or equal to the inputted number
    print(numbers) 
    numbers *= 2 # number counter doubles each time
    
                   