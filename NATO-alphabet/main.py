# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
#
# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#

import pandas

phonetic_data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_data_dictionary = {row.letter: row.code for (index, row) in phonetic_data.iterrows()}
# print(phonetic_data_dictionary)

# is_continue = True
#
# while is_continue:
#     name = input("Enter a word: ")
#     try:
#         result = [phonetic_data_dictionary[letter.upper()] for letter in name]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please")
#     else:
#         print(result)
#         is_continue = False


def generate_password():
    name = input("Enter a word: ")
    try:
        result = [phonetic_data_dictionary[letter.upper()] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_password()
    else:
        print(result)


generate_password()
