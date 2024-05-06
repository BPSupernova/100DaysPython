import random

print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
choice = int(input(""))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
        ________)
---._________)
'''

scissors = '''
    _______
---'   ____)____
         _______)
     ____________)
     (_____)
---._(___)
'''

if choice == 0:
   print(rock)
elif choice == 1:
   print(paper)
elif choice == 2:
   print(scissors)
else:
   print("Your hand was unrecognizable. Please visit a doctor.")

comp_choice = random.randint(0, 2)
print(f"The computer choice: {comp_choice}")

if choice == comp_choice:
   print("It twas a draw.")
elif (choice == 0 and comp_choice == 1) or (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 0):
   print("The computer won. Better luck next time!")
elif (comp_choice == 0 and choice == 1) or (comp_choice == 1 and choice == 2) or (comp_choice == 2 and choice == 0):
   print("You won! Woo-Hoo")
else:
   print("The computer won. Better luck next time!")