import pandas

nato_alfa_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alfa_dict = {row.letter: row.code for (index, row) in nato_alfa_df.iterrows()}
user_word = input("Enter a word: ").upper()

generated_nato_alphas = [nato_alfa_dict[letter] for letter in user_word]

print(generated_nato_alphas)