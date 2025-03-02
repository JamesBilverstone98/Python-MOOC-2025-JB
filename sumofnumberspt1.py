# SUM OF CONSECUTIVE NUMBERS (VERSION 1) = ask user to type in limit, program then calculates sum of consecutive numbers until sum is same as upper limit

limit = int(input("Limit: ")) # user input
numbers = 1 # counter for numbers summed together
added_together = 0 # counter for the sum

while added_together < limit: # keep doing this program until the sum reaches whatever user inputs 
    added_together += numbers # sum counter adds the numbers counter
    numbers += 1 # number counter increases each time

print(added_together) # print sum
