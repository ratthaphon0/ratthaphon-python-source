import random

def simple_guessing_game():
    random_number = random.randint(1,20)
    
    print("=== SIMPLE GUESSING GAME ===",
          "\nGuess my number between 1 and 20!",
          "\nYou have 6 attempts."
          )
    for attempt in range(1,7):
        try:
            guess_number = int(input(f"Attempt {attempt}/6 - Enter your guess: "))
        except ValueError:
            print("Please enter valid number")
            continue
        if guess_number == random_number:
            print(f"Congratulations! You won in {attempt} attempts!")
            break
        elif guess_number > random_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
    else:
        print("You such a loser! Out of attempt!")
            
if __name__ == "__main__":
    simple_guessing_game()  


"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""