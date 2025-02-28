# PIN AND NUMBER OF ATTEMPTS = ask user for PIN until they enter correct one 

attempts = 0 # counter starts at 0

while True:
    pin = input("PIN: ") # user input for PIN
    attempts +=1 # counter starts increasing from first attempt

    if pin == "4321":
        if attempts == 1:
            print("Correct! It only took you one single attempt!") # if user guesses first time, print out this
        else:
            print(f"Correct! It took you {attempts} attempts") # prints out amount of guesses once correct pin entered
        break # program ends

    print("Wrong") 



