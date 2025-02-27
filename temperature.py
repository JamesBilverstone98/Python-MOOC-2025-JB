# TEMPERATURES = ask user for temp in fahrenheit, print it out in celsius

temperature = int(input("Please type in a temperature (F): ")) # user input
celsius = ((temperature - 32) * 5 / 9) # temperature conversion calculation

if temperature >= 32: # if temp is greater than or equal to 32 degrees fahrenheit (equivalent to 0 degrees celsius)
    print(f"{temperature} degrees Fahrenheit equals {celsius} degrees Celsius")
else: # any other temps
    print(f"{temperature} degrees Fahrenheit equals {celsius} degrees Celsius")
    print("Brr! It's cold in here!")