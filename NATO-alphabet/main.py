import pandas as pd

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

df = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# print(phonetic_dict)

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
