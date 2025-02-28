# THE NEXT LEAP YEAR = asks user for the year, prints out the next leap year

year = int(input("Year: ")) # user input for year
leap_year = year

while True:

    year += 1 # counter starts
    if year % 4 == 0 and (year % 100 != 0 and year % 400 != 0): # leap year calculation from previous exercise
        break

    elif year % 100 == 0 and year % 400 == 0:
        break

print(f"The next leap year after {leap_year} is {year}")
    


