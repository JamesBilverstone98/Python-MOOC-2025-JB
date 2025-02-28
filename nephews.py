# NEPHEWS = ask for users name, if certain names, print out statements 

name = input("Please type in your name: ") # user input
 
if name == "Huey" or name == "Dewey" or name == "Louie": # if input includes any of these names
    print("I think you might be one of Donald Duck's nephews.")
elif name == "Morty" or name == "Ferdie": # or these names
    print("I think you might be one of Mickey Mouse's nephews.")
else: # or any other name at all
    print("You're not a nephew of any character I know of.")