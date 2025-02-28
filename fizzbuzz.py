# FIZZBUZZ = asks user for integer, depending on wether number is divisible by a certain number, print out statement

number = int(input("Number: "))

if number % 3 == 0 and number % 5 == 0:
    # This condition must be evaluated first, because if this is true,
    # also both of the following conditions are true
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(f"Number: {number}")




