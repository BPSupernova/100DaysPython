import random

def interpret_guess(guess, number): 
    """Evaluates whether the guess is higher, lower, or equal to the number"""
    if guess == number:
        return True
    elif guess > 100 or guess < 1:
        print("Your guess was not even in between 1 and 100. Guess again.")
        return False
    elif guess > number:
        print("You guessed too high, please guess again.")
        return False
    else:
        print("You guessed too low, please guess again")
        return False

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Choose your difficulty: easy -> 10 attempts; hard -> 5 attempts
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Bool to end guessing loop if guess is correct
guessed_correctly = False

num_to_guess = random.randint(1, 100)
attempts = 0
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5

while not attempts == 0 and not guessed_correctly:
    print(f"You have {attempts} attempts left.")
    guess = int(input("Make a guess: "))
    guessed_correctly = interpret_guess(guess, num_to_guess)
    attempts -= 1

if guessed_correctly:
    print("You guessed correctly! Congrats.")
else:
    print(f"You almost had it! The number was {num_to_guess}.")