# THE ELDER = ask user for names and ages, print out name of eldest

print("Person 1:")
person1_name = input("Name: ")
person1_age = int(input("Age: "))
print("Person 2:")
person2_name = input("Name: ")
person2_age = int(input("Age: "))

if person1_age > person2_age: # if person 1 is older than person 2
    print(f"The elder is {person1_name}")
elif person1_age == person2_age: # draw
    print(f"{person1_name} and {person2_name} are the same age")
else: # person 2 is older than person 1
    print(f"The elder is {person2_name}")
