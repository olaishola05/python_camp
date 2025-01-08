# with open('sample.txt') as file:  # save us from closing the file manually and also handle exceptions
#     contents = file.read()
#     print(contents)


# with open('sample.txt', 'w') as file: # overwrites the file and creates a new file if it doesn't exist
#     file.write('Hello World')

# appending to a file
# with open('sample.txt', 'a') as file:
#     file.write('\nHello World')

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# TODO: Create a letter using starting_letter.txt

with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace('[name]', stripped_name)
        with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.txt', 'w') as new_file:
            new_file.write(new_letter)

# Save the letters in the folder "ReadyToSend".
