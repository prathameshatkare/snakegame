import random

def guess_the_number():
    print("Welcome to the game ")
    print("I'm thinking of a number between 1 and 100.")

    # The computer selects a random number between 1 and 100
    number_to_guess = random.randint(1, 100)

    # Keep track of the number of attempts
    attempts = 0

    while True:
        try:
            # Ask the player for their guess
            guess = int(input("Take a guess: "))
            attempts += 1

            # Check if the guess is too low, too high, or correct
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break  # End the game when the player guesses correctly
        except ValueError:
            print("Please enter a valid number.")

# Start the game
guess_the_number()
