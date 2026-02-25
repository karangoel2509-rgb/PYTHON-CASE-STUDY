
import random
def ngg():
    number = random.randint(1,100)
    guess = 0
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")
    while guess != number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess > number:
                print("Too high! Try again.")
            elif guess < number:
                print("Too low! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")

ngg()