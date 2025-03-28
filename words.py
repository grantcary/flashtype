import json
import random
import string

with open('english_25k.json', 'r') as file:
    data = json.load(file)

print(data['name'])
WORDS = data['words']
ALPHA = string.ascii_lowercase

def get_word(char_1, char_2):
    word_group = [w for w in WORDS if (char_1 + char_2) in w]
    rand_index = random.randrange(len(word_group))
    return word_group[rand_index].lower()

def rand_char():
    rand_index = random.randrange(26)
    return ALPHA[rand_index]