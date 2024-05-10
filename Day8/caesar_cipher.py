def encode(word, shift):
    char_list = list(word)  # Convert the string to a list of characters
    for num in range(0, len(char_list)):
        ascii_char_equiv = ord(char_list[num]) + shift
        if ascii_char_equiv > 122:
            ascii_char_equiv = 97 + (ascii_char_equiv - 123)
        char_list[num] = chr(ascii_char_equiv)

    encoded_word = ''.join(char_list)
    print(f"Your encrypted word: {encoded_word}")

def decode(word, shift):
    char_list = list(word)  # Convert the string to a list of characters
    for num in range(0, len(char_list)):
        ascii_char_equiv = ord(char_list[num]) - shift
        if ascii_char_equiv < 97:
            ascii_char_equiv = 122 - (96 - ascii_char_equiv)
        char_list[num] = chr(ascii_char_equiv)

    encoded_word = ''.join(char_list)
    print(f"Your encrypted word: {encoded_word}")

print("Welcome to Ben's Epic Caesar Cipher!!")
option = input("Would you like to encode or decode a word? Please type 'encode' or 'decode'. ")
shift = int(input("What is the shift you want for this cipher? "))

word_to_transform = ""
if option == 'encode':
    word_to_transform += input("What word would you like to encode? ")
    encode(word_to_transform, shift)

elif option == 'decode':
    word_to_transform += input("What word would you like to decode? ")
    decode(word_to_transform, shift)

