from higher_or_lower_data import data
from higher_or_lower_art import logo
import random

print(logo)

# Bool state if player lost the most recent round
lost = False

# Number of rounds the player has guessed correctly; aka their score
score = 0

while not lost:
    account_1 = random.randint(0, len(data) - 1) # Random integer that references the dictionary of a celebrity
    account_2 = random.randint(0, len(data) - 1) # Random integer that references the dictionary of a celebrity
    
    # To prevent an account vs itself scenerio
    while account_1 == account_2:
        account_2 = random.randint(0, len(data) - 1) # Random integer that references the dictionary of a celebrity

    print(f"Compare A: {data[account_1]['name']}, a {data[account_1]['description']}, from {data[account_1]['country']}")
    print("")
    print("VS")
    print("")
    print(f"Against B: {data[account_2]['name']}, a {data[account_2]['description']}, from {data[account_2]['country']}")

    choice = input("Who has more followers A or B? ")

    if choice == "A":
        print("A")
        if data[account_1]['follower_count'] > data[account_2]['follower_count']:
            score += 1
            print(f"You're right! Your current score is {score}.")
        else:
            lost = True
            print("Sorry that's wrong!")
    elif choice == "B":
        if data[account_2]['follower_count'] > data[account_1]['follower_count']:
            score += 1
            print(f"You're right! Your current score is {score}.")
        else:
            lost = True
            print("Sorry that's wrong!")
    else:
        print("You have to enter 'A' or 'B' next time")
        lost = True
    print("", end='\n\n')

print(f"Your final score was {score}!")