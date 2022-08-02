import pandas
# Given a word, returns the NATO phonetic code words
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

user_word = input("Give me a word and I'll give you the NATO equivalent: ").upper()
nato_result = [nato_dict[letter] for letter in user_word]
print(nato_result)
