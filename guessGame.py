# import random

# min = 1
# max = 100
# maxAttemps = 10

# # Generate a random number between min and max
# numberToGuess = random.randint(min, max)
# print("Welcome to the number guessing game!")
# print(f"I'm thinking of a number between {min} and {max}.")
# print(f"You have {maxAttemps} attempts to guess it.")

# attempt = 0

# while True:
#     # Ask the user for their guess
#     userGuess = input("Enter your guess: ")
#     # Check if the user wants to quit
#     if attempt == maxAttemps:
#         print("You've reached the maximum number of attempts.")
#         print(f"The correct number was {numberToGuess}. Better luck next time!")
#         break
#     elif userGuess.lower() == "quit":
#         print("Thanks for playing!")
#         break
#     else:
#         # Try to convert the user's guess to an integer
#         try:
#             userGuess = int(userGuess)
#             # Check if the user's guess is in the correct range
#             if userGuess <= numberToGuess:
#                 print(f"Your guess, {userGuess}, is too low. Try again!")
#             elif userGuess > numberToGuess:
#                 print(f"Your guess, {userGuess}, is too high. Try again!")
#             else:
#                 print("Congratulations! You guessed the correct number.")
#                 break
#             attempt += 1
#         except TypeError:
#             print("Error: Invalid input type")
#         except Exception as e:
#             print(f"An error occurred: {str(e)}")

import random

# Game settings
min_number = 1
max_number = 100
max_attempts = 10

# Generate a random number to guess
number_to_guess = random.randint(min_number, max_number)
attempts = 0

print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between {min_number} and {max_number}. Can you guess it?")

# Main game loop
while attempts < max_attempts:
    # Get user input
    try:
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    # Check the guess
    if guess == number_to_guess:
        print("Congratulations! You guessed the correct number!")
        break
    elif guess < number_to_guess:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")

    # Increment attempts
    attempts += 1

# Check if user failed to guess the number
if attempts == max_attempts and guess != number_to_guess:
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
    
input("\nPress Enter to exit the game.")