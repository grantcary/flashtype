import json
import random
import string
from time import time

with open('english_25k.json', 'r') as file:
    data = json.load(file)

print(data['name'])
WORDS = data['words']
ALPHA = string.ascii_lowercase

def rand_char():
    rand_index = random.randrange(26)
    return ALPHA[rand_index]

class Word():
    def __init__(self, char_1='t', char_2='h'):
        self.bigram = (char_1, char_2)
        self.word = ''
        self.start_time = 0.0
        self.worst_time = 0.0
        self.worst_bigram = self.bigram[0] + self.bigram[1]
        self.new_word = True
        self.prev_char = None

        self.get_word()

    def char(self):
        return self.word[0]

    def shrink(self):
        if self.new_word:
            self.new_word = False
            self.prev_char = self.char()
        elif (t := round(time() - self.start_time, 3)) >= self.worst_time:
            self.worst_time = t
            self.bigram = (self.prev_char, self.char())

        self.prev_char = self.char()
        self.word = self.word[1:]
        self.start_time = time()

    def get_word(self):
        if not self.word:
            self.worst_bigram = self.bigram[0] + self.bigram[1]
            word_group = [w for w in WORDS if (self.bigram[0] + self.bigram[1]) in w]
            rand_index = random.randrange(len(word_group))
            self.word = word_group[rand_index].lower()
            self.worst_time = 0.0
            self.new_word = True