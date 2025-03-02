# # SUM OF CONSECUTIVE NUMBERS (VERSION 2) = ask user to type in limit, program then calculates sum of consecutive numbers until sum is same as upper limit
# along with the result printed, it should print out calculation performed too

limit = int(input("Limit: ")) # user input
numbers = 1 # counter for numbers summed together
added_together = 0 # counter for the sum
calculation = "" # a variable to store the sum

while added_together < limit: # keep doing this program until the sum reaches whatever user inputs 
    added_together += numbers # sum counter adds the numbers counter
    
    if calculation == "": # ensures a + is not added for the first number in the counter
        calculation = str(numbers)
    else:
        calculation += " + " + str(numbers)
    numbers += 1
    
consecutive_sum = f"The consecutive sum: {calculation} = {added_together}"

print(consecutive_sum) # print sum along with the calculation