# Task1 sample solution
# Fizzbuzz problem.
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# Task2 sample solution
import random


guesses_left = 3
random_number = random.randint(0, 10)
while guesses_left > 0:
    guess = input("Please guess a number between 1 and 10:")

    if guess == random_number:
        print("Congrats! you guessed the number correctly!")
        break
    else:
        print("That was wrong!")
        guesses_left = guesses_left - 1

# Task3 sample solution
for x in range(5):
    for y in range(x):
            print("*", end="")
    print("")

for x in range(5, -1, -1):
    for y in range(x):
        print("*", end="")
    print("")






