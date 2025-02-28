# COUNTDOWN = print out a program which counts down

number = 5 # starting counter
print("Countdown!")
while True:
    print(number)
    number = number - 1 # keep printing numbers and when doing so each new number is the previous number minus one
    if number == 0: # once the number gets to 0, exit the program
        break
print("Now!")