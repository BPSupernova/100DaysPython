import random 
import hangman_words

start = '''
   __________
   |         |
   |        
   |        
   |        
___|_____
'''

first_miss = '''
   __________
   |         |
   |         0
   |        
   |      
___|_____
'''

second_miss = '''
   __________
   |         |
   |        <0
   |        
   |      
___|_____
'''

third_miss = '''
   __________
   |         |
   |        <0> 
   |        
   |        
___|_____
'''

fourth_miss = '''
   __________
   |         |
   |        <0> 
   |         | 
   |        
___|_____
'''

fifth_miss = '''
   __________
   |         |
   |        <0> 
   |         | 
   |        / 
___|_____
'''

last_miss = '''
   __________
   |         |
   |        <0> 
   |         | 
   |        / |
___|_____
'''


lives = 6
game_over = False
missed_guess = False

chosen_Word = hangman_words.word_list[random.randint(0, len(hangman_words.word_list) - 1)]
blank_spaces = []

for num in range(0, len(chosen_Word)):
    blank_spaces.append("_")

def is_hit(letter, word):
    for num in range(0, len(word)):
        if word[num] == letter:
            return True
    return False

def print_hangman_visual(lives_left):
    if lives_left == 6:
        print(start)
    elif lives_left == 5:
        print(first_miss)
    elif lives_left == 4:
        print(second_miss)
    elif lives_left == 3:
        print(third_miss)
    elif lives_left == 2:
        print(fourth_miss)
    elif lives_left == 1:
        print(fifth_miss)
    else:
        print(last_miss)

def print_guessing_status(blank_spaces):
    for space in blank_spaces:
        print(space + " ", end=' ')
    
    # For better spacing
    print("", end='\n\n')

def update_word(blank_spaces, letter, word):
    for num in range(0, len(word)):
        if letter == word[num]:
            blank_spaces[num] = letter

print_guessing_status(blank_spaces)

while (not game_over):
    letter_guess = input("Guess a letter: ").lower()
    # For spacing
    print("")

    hit_status = is_hit(letter_guess, chosen_Word)
    
    if hit_status:
        update_word(blank_spaces, letter_guess, chosen_Word)
        print(f"{letter_guess} was in the word!")

    if not hit_status:
        print(f"{letter_guess} was NOT in the word!")
        lives -= 1

    print_hangman_visual(lives)
    print_guessing_status(blank_spaces)

    if lives <= 0:
        game_over = True
        print("You lost all your lives! The word was " + chosen_Word + ".")

    elif "_" not in blank_spaces:
        game_over = True
        print("You guessed the word! Congrats.")