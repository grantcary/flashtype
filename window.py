import pygame
import random
from time import time

import words

W, H = 1280, 720
FPS = 60

pygame.init()
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
running = True

pygame.font.init()
my_font = pygame.font.SysFont('Monospace Bold', 75)

c1, c2 = 'a', 'b'
w = words.get_pair_words(c1, c2)
r = random.randrange(len(w))
test_word = w[r]

alpha_surface = pygame.Surface((W, H))
alpha_surface.fill((255, 0, 0))
red_alpha = 0
alpha_surface.set_alpha(red_alpha)

prev_char = None
curr_char = None
bigrams = []
errors = 0
worst = ''
new_word = True
start_time = time()
while running:
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            key_press = pygame.key.name(event.key)
            if key_press == test_word[0]:
                if new_word:
                    reaction = time() - start_time
                    new_word = False
                else:
                    bigrams.append((round(time() - start_time, 3), (curr_char, test_word[0])))
                    prev_char = curr_char
                    curr_char = test_word[0]

                curr_char = test_word[0]
                start_time = time()
                test_word = test_word[1:]
                                
            else:
                red_alpha = 255
                errors += 1

    if not test_word and len(w) > 1:
        bigrams.sort(key=lambda x: x[0])
        c1, c2 = bigrams[-1][1]
        w = words.get_pair_words(c1, c2)
        r = random.randrange(len(w))
        test_word = w[r]
        bigrams = []
        worst = f'{c1}{c2}'

        new_word = True
        start_time = time()

    alpha_surface.set_alpha(red_alpha)
    screen.blit(alpha_surface, (0, 0))

    if red_alpha > 0:
        red_alpha -= 10

    text_surface = my_font.render(test_word, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(W // 2, H // 2))
    screen.blit(text_surface, text_rect)

    error_counter = my_font.render(str(errors), True, (255, 255, 255))
    errcntr_rect = error_counter.get_rect(top=5, right=W - 5)
    screen.blit(error_counter, errcntr_rect)

    reaction_time = my_font.render(worst, True, (255, 255, 255))
    react_time_rect = reaction_time.get_rect(top=5, left=5)
    screen.blit(reaction_time, react_time_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()