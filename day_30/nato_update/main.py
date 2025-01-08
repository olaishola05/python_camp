import pandas

quote = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in quote.iterrows()}
print(phonetic_dict)


def generate_nato_alphabet():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('Sorry!, only letters in the alphabets please.')
        generate_nato_alphabet()
    else:
        print(output_list)
        generate_nato_alphabet()


generate_nato_alphabet()
