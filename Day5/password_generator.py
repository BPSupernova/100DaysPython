import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

zero_to_nine = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

other = ['!', '#', '$', '%', '^', '&', '*', '(', ')', ':', ';', '~', '`', '?', '<', '>', ',', '.', '+', '=']

print("Welcome to Ben's Epic Password Generator!")
print("How many letters would you like in your password?")
letters = input("")

print("How many symbols would you like?")
symbols = input("")

print("How many numbers would you like?")
numbers = input("")

password = ""
for letter in range(0, int(letters)):
    password += alphabet[random.randint(0, len(alphabet) - 1)]

for num in range(0, int(numbers)):
    password += zero_to_nine[random.randint(0, len(zero_to_nine) - 1)]

for thing in range(0, int(symbols)):
    password += other[random.randint(0, len(other) - 1)]

char_list = list(password)  # Convert the string to a list of characters
random.shuffle(char_list)  # Shuffle the list in-place
shuffled_password = ''.join(char_list)  # Convert the shuffled list back to a string

print("Here's your super epic password: " + shuffled_password)