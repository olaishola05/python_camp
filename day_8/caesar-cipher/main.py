from alphabets import alphabet
from art import logo


def caesar(word, amount_of_shift, cipher_type):
    cipher_text = ""

    if cipher_type == "decode":
        amount_of_shift *= -1

    for char in word:
        if char in alphabet:
            pos = alphabet.index(char)
            new_pos = pos + amount_of_shift
            cipher_text += alphabet[new_pos]
        else:
            cipher_text += char
    print(f"The {cipher_type}d text is {cipher_text}")


print(logo)

SHOULD_CONTINUE = True

while SHOULD_CONTINUE:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26  # if the user enter shift bigger than the lenght of alphabet

    caesar(word=text, amount_of_shift=shift, cipher_type=direction)

    result = input("Type 'yes' if you want to go again. Otherwise 'no'.\n").lower()

    if result == "no":
        SHOULD_CONTINUE = False
        print("GoodBye")
