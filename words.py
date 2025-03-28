import json

with open('english_25k.json', 'r') as file:
    data = json.load(file)

print(data['name'])
WORDS = data['words']

def get_pair_words(a, b):
    pairs = []
    for w in WORDS:
        if (a + b) in w:
            pairs.append(w)
    return pairs
