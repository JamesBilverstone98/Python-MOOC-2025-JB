# DAILY WAGES = ask user for hourly wage, hours worked, day of the week, then print out figures for it

hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
weekday = input("Day of the week: ")

if weekday == "Sunday": # only if user input is a Sunday
    print(f"Daily wages: {hourly_wage * 2 * hours_worked} euros")
else: # any other day
    print(f"Daily wages: {hourly_wage * hours_worked} euros")