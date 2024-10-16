#AdvancedNumberGuessingGame.py
import random

def get_hint(guess, actual, previous_guess=None):
    if guess == actual:
        return "Correct!"
    
    # Calculate the absolute difference
    difference = abs(guess - actual)

    # Hint logic based on difference
    if previous_guess is None:
        if difference > 20:
            return "Way too cold!"
        elif difference > 10:
            return "Cold!"
        elif difference > 5:
            return "Warm!"
        else:
            return "You're getting really warm!"
    else:
        previous_difference = abs(previous_guess - actual)
        if difference < previous_difference:
            return "Warmer!"
        elif difference > previous_difference:
            return "Colder!"
        else:
            return "Same distance!"

def play_game():
    actual_number = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0
    previous_guess = None
    
    print("Welcome to the Advanced Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Get the hint based on the guess and actual number
            hint = get_hint(guess, actual_number, previous_guess)
            print(hint)
            
            if guess == actual_number:
                break
            
            previous_guess = guess  # Updating the previous guess
        except ValueError:
            print("Please enter a valid integer.")
    
    # Scoring system: 100 points minus 2 points for each wrong attempt
    score = max(100 - (attempts - 1) * 2, 0)
    print(f"Congratulations! You guessed the number in {attempts} attempts.")
    print(f"Your score: {score}")

# Start the game

play_game()

