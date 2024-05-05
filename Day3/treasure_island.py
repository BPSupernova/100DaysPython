game_over = False

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

print("You start at a fork in the road. Which way will you go?")
direction = input("'Left' or 'Right'? ")
if direction == "Left":
    print("You had a pleasant walk!\n")
else:
    print("A dinosaur came out of nowhere and ran you over! Game Over.\n")
    game_over = True

if game_over == False:
    print("At the end of the path you come across a river.")
    river_action = input("'Swim' across or 'Wait' for a boat? ")
    if river_action == "Wait":
        print("You made it across the river safe and sound!\n")
    else:
        print("It turns out the river was full of volcanic acid and you were burned alive. Game Over.\n")
        game_over = True

if game_over == False:
    print("Upon docking you come across three doors. One holds the Legendary Treasure of Awesomeness!")
    door = input("Which door will you go through? The 'Red', 'Blue', or 'Yellow' one? ")
    if door == "Yellow":
        print("The Legendary Treasure of Awesomeness is officially yours! Congratulations.")
    elif door == "Blue":
        print("A shark named Marcey invites you in for a tea party, but there's only one chair so the both of you play musical chairs and you lose. Game Over.")
    elif door == "Red":
        print("You enter into a couples therapy session with a partner who believes they are married to you. The door closes with no exit. Game Over.")
    else:
        print("As you reach for something that clearly isn't a door for whatever reason, you are sniped by Logan Fournier. Game Over.")