import json
import random
import string
from time import time

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

class Word():
    def __init__(self):
        self.word = get_word('a', 'b')
        self.start_time = 0.0
        self.worst_time = 0.0
        self.bigram = ('', '')
        self.worst_bigram = self.bigram[0] + self.bigram[1]
        self.errors = 0
        self.new_word = True
        self.prev_char = None

    @classmethod
    def shrink(self):
        if self.new_word:
            self.new_word = False
        else:
            if (t := round(time() - self.start_time, 3)) > self.worst_time:
                self.worst_time = t
                self.bigram = (self.prev_char, self.word[0])

        self.word = self.word[1:]
        self.start_time = time()

    def get_word(self, char_1, char_2):
        word_group = [w for w in WORDS if (char_1 + char_2) in w]
        rand_index = random.randrange(len(word_group))
        self.word = word_group[rand_index].lower()