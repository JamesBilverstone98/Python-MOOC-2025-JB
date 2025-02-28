# ALPHABETICALLY LAST = ask user for 2 words, print which comes alphabetically last

word1 = input("Please type in the 1st word: ")
word2 = input("Please type in the 2nd word: ")

if word1 < word2: # if the last letter of word 1 comes after the last letter of word 2
    print(f"{word2} comes alphabetically last")
elif word1 > word2:
    print(f"{word1} comes alphabetically last")
else: # draw
    print("You gave the same word twice.")