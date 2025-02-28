# REPEAT PASSWORD = ask user for password, ask to type in again, keep on asking until user enters first password again

password = input("Password: ") # user input for first password

while True: 
    password2 = input("Repeat password: ") # asks for repeat password

    if password2 == password:
        break # if repeat password is same as original password, program ends
    else:
        print("They do not match!") # if repeat password is different, code repeats on loop until they match

print("User account created!")
        
