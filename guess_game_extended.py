# This will be a simple number guessing game
# The user will have tu guess a number between 1 and 10
# if the user guess number is incorrect , the program will tell
# either "to high" "too low"   

# Problems:
# Does not handle multiple guesses

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10")

import random

parsed_guess =  0 # Initialize parsed_guess to ensure it is defined before the loop
number_to_guess = random.randint(1, 10)

while parsed_guess != number_to_guess:
    user_input = input("Please enter your guess (or type 'quit' to exit): ")


    if user_input.lower() == 'quit':
        print("Game exited. Goodbye!")
        exit()

    print("You guessed: " + user_input)
#print(f"You guessed: {user_input}")

    try:
        parsed_guess = int(user_input)
    except Exception:  
        print("Invalid input! Please enter a valid integer.")
        exit()

    if parsed_guess < 1 or parsed_guess > 10:
        print("your guess is out of range! Please enter a number between 1 and 10")
    elif parsed_guess < number_to_guess:
        print("Too low")
    elif parsed_guess > number_to_guess:
            print("Too high")
    else:
        print("Congralutions! You guessed the number correctly")