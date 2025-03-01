# STORY = keep asking user for words, if user types in end, program should print out the story with the words formed together. 
# if user also types in the same word twice, program also ends

words = "" # empty string with no characters in it
previous_word = "" # ensures the previous word variable is created and can be called upon in the loop

while True:
    
    word = input("Please type in a word: ")  # user input for word
    
    if word == "end": # if inputted word is 'end', exit program
        break
    
    if word == previous_word: # if user enters 2 words in a row, exit program
        break
    
    words += word + " " # add previous word to each input along with a space
    
    previous_word = word # ensures duplicate words cannot be used straight after each other
         
print(words) # print all entered words
    

        
    

    


    

       
