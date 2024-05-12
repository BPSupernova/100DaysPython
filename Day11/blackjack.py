import random

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
print("")

logo = '''
 ____________
|          J |
|      _     |____
|    <")}    |  A |
|   (    )   |    |
|            |    |
| J          |)   |
|____________|    |
     | A          |
     |____________|
'''

def calc_card_sum(card1, card2):
    """Calculates the sum of the cards in a hand"""
    return card1 + card2

def is_bust(card_sum):
    """Determines if a Blackjack hand totals over 21"""
    return card_sum > 21

if play == 'y':
    game_over = False
    
    # Prints the game logo
    print(logo)

    # Dictionary of Cards & Their Values in Blackjack
    cards = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
    }

    # Cards obtained by hitting
    added_cards = []

    # Cards obtained by computer when under 17 with their initial hand
    added_com_cards = []

    # List of cards to utilize indexing
    card_names = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # Cards dealt initially to the player
    player_card_1 = card_names[random.randint(0, len(card_names) - 1)]
    player_card_2 = card_names[random.randint(0, len(card_names) - 1)]

    # Cards dealt initially to the computer
    com_card_1 = card_names[random.randint(0, len(card_names) - 1)]
    com_card_2 = card_names[random.randint(0, len(card_names) - 1)]

    # Sum of cards in the player & computer's hands respectively
    player_sum = calc_card_sum(cards[player_card_1], cards[player_card_2])
    com_sum = calc_card_sum(cards[com_card_1], cards[com_card_2])

    # Fixing Ace card value to 11 if obtained off the initial dealing
    if player_card_1 == "A" or player_card_2 == "A":
        player_sum += 10
    elif com_card_1 == "A" or com_card_2 == "A":
        com_sum += 10

    # Computer must draw until their hand totals over 17
    while com_sum < 17:
        com_card_3 = card_names[random.randint(0, len(card_names) - 1)]
        added_com_cards.append(com_card_3)
        com_sum = calc_card_sum(com_sum, cards[com_card_3])

    print(f"Your cards are [{player_card_1},{player_card_2}] which total {player_sum}. The computer has a {com_card_1}.")
    
    # Beginning of hit loop (for obtaining new cards from the dealer)
    while not game_over:
        hit_decision = input("Press 'y' to hit for another card or 'n' to keep what you have. ")
        print("") # For spacing
        
        if hit_decision == 'y':
            added_card = card_names[random.randint(0, len(card_names) - 1)]
            added_cards.append(added_card)
            player_sum = calc_card_sum(player_sum, cards[added_card])
            if is_bust(player_sum):
                game_over = True
            else:
                print(f"Your cards are [{player_card_1},{player_card_2}", end="")
                for card in added_cards:
                    print("," + card, end="")
                print(f"] which total {player_sum}. The computer has a {com_card_1}.")
        else:
            game_over = True

    print(f"Your final hand: [{player_card_1},{player_card_2}", end="")
    for card in added_cards:
        print("," + card, end="")
    print(f"] which total {player_sum}.")

    print(f"The computer's final hand: [{com_card_1},{com_card_2}", end="")
    for card in added_com_cards:
        print("," + card, end="")
    print(f"] which total {com_sum}.")

    if is_bust(player_sum):
        print("You went over 21! You lost :(")
    elif is_bust(com_sum):
        print("The computer went over! You won :)")
    elif player_sum > com_sum:
        print("You won, congrats!")
    elif player_sum == com_sum:
        print("In a tie the computer wins. So close!")
    else:
        print("The computer won this one.")