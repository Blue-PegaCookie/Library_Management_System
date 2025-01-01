# I'll be creating a number guessing game

import random

def number_guessing_game():
    print("Welcome to the number guessing game!")

    # Choose difficulty level
    print("Choose your difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Extremely Hard")

    # Set the difficulty level
    difficulty = input("Enter difficulty level (1/2/3/4): ")

    # Generate random number based on difficulty level
    if difficulty == '1':
        # Generate random number between 1 and 10 (Computer's guess)
        easy = random.randint(1, 10)

        # Set the number of attempts
        attempts = 5

        # Print the number of attempts
        print("You have 6 attempts to guess the number between 1 and 10")

        # Loop through the number of attempts
        while attempts > 0:

            # Get user's guess
            guess = input("Enter your guess: ")

            # Check if the input is a number
            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input")
                continue

            # Check if the number is between 1 and 10 (Boundary Testing)
            if guess < 1 or guess > 10:
                print("Number must be between 1 and 10")
                continue

            # Check if the guess is correct
            if guess < easy:
                print("Too low")
            elif guess > easy:
                print("Too high")
            else:
                print("Congratulations! You guessed the number")
                break
            # Decrement the number of attempts
            attempts -= 1
            print(f"You have {attempts} attempts left")

    elif difficulty == '2':
        medium = random.randint(1,50)
        attempts = 12
        print("You have 15 attempts to guess the number between 1 and 50")

        while attempts > 0:

            guess = int(input("Enter your guess: "))

            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input")
                continue

            if guess < 1 or guess > 50:
                print("Number must be between 1 and 50")
                continue

            if guess < medium:
                print("Too low")
            elif guess > medium:
                print("Too high")
            else:
                print("Congratulations! You guessed the number")
                break
            attempts -= 1
            print(f"You have {attempts} attempts left")

    elif difficulty == '3':
        hard = random.randint(1, 100)
        attempts = 17
        print("You have 20 attempts to guess the number between 1 and 100")

        while attempts > 0:

            guess = int(input("Enter your guess: "))

            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input")
                continue

            if guess < 1 or guess > 100:
                print("Number must be between 1 and 100")
                continue

            if guess < hard:
                print("Too low")
            elif guess > hard:
                print("Too high")
            else:
                print("Congratulations! You guessed the number")
                break
            attempts -= 1
            print(f"You have {attempts} attempts left")

    elif difficulty == '4':
        extremely_hard = random.randint(1, 1000)
        attempts = 125
        print("You have 25 attempts to guess the number between 1 and 1000")

        while attempts > 0:
            guess = int(input("Enter your guess: "))

            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input")
                continue

            if guess < 1 or guess > 1000:
                print("Number must be between 1 and 1000")
                continue


            if guess < extremely_hard:
                print("Too low")
            elif guess > extremely_hard:
                print("Too high")
            else:
                print("Congratulations! You guessed the number")
                break
            attempts -= 1
            print(f"You have {attempts} attempts left")

    else:
        print("Invalid input")
        number_guessing_game()

    # Ask user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ")

    # Check if the input is valid
    if play_again.lower() == "yes":
        number_guessing_game()
    elif play_again.lower() == "no":
        print("Goodbye!")
        exit()
    else:
        print("Invalid input")
        number_guessing_game()

# Call the function
number_guessing_game()

# The above code is a number guessing game
# It generates a random number based on the difficulty level chosen by the user

# The user has a limited number of attempts to guess the number
