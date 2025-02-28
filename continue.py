# SHALL WE CONTINUE = say hello and whether to continue until user says no

while True: # While condition is true, following program runs
    print("hi")
    question = input("Shall we continue? ")
    if question == "no":
        break # If user says no, then the loop ends, if any other response, the loop repeats as below

print("okay then") # print this only when user input is actually 'no'