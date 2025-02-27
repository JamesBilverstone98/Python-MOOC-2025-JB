# WHAT TO WEAR = ask user for weather and then suggest weather-appropriate clothing

print("What is the weather forecast for tomorrow?")
temperature = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")
print("Wear jeans and a T-shirt")

if temperature < 21: # temps less than 21
    print("I recommend a jumper as well")

if temperature < 11: # temps less than 11
    print("Take a jacket with you")

if temperature < 6:  # temps less than 6
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

if rain == "yes": # if input for rain is yes, include this (no matter what temperature is input)
    print("Don't forget your umbrella!")

