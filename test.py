from words import Word, rand_char
import random
from time import sleep

r = [0.1, 1.4, 0.42, 0.34]

w = Word()
while True:
    while w.word:
        sleep(r[random.randrange(len(r))])
        print(w.word, w.char())
        w.shrink()
    print(w.worst_bigram)
    w.get_word()
    # print(w.word, w.worst_bigram)

