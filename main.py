import pandas
# Given a word, returns the NATO phonetic code words
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}


def convert_to_nato():
    user_word = input("Give me a word and I'll give you the NATO equivalent: ").upper()
    try:
        nato_result = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letter in the alphabet please.")
        convert_to_nato()
    else:
        print(nato_result)


convert_to_nato()
