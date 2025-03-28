import pygame
from words import Word

def window(w, h, fps):
    pygame.init()
    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()
    running = True

    pygame.font.init()
    my_font = pygame.font.SysFont('Monospace Bold', 75)

    error_flash = pygame.Surface((w, h))
    error_flash.fill((255, 0, 0))
    error_flash_alpha = 0
    error_flash.set_alpha(error_flash_alpha)

    errors = 0
    word = Word()
    while running:
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                key_press = pygame.key.name(event.key)
                if key_press == word.char():
                    word.shrink()
                else:
                    error_flash_alpha = 255
                    errors += 1

        word.get_word()

        error_flash.set_alpha(error_flash_alpha)
        screen.blit(error_flash, (0, 0))

        if error_flash_alpha > 0:
            error_flash_alpha -= 10

        text_surface = my_font.render(word.word, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(w // 2, h // 2))
        screen.blit(text_surface, text_rect)

        error_counter = my_font.render(str(errors), True, (255, 255, 255))
        error_counter_rect = error_counter.get_rect(top=5, right=w - 5)
        screen.blit(error_counter, error_counter_rect)

        worst_keystroke = my_font.render(word.worst_bigram, True, (255, 255, 255))
        worst_keystroke_rect = worst_keystroke.get_rect(top=5, left=5)
        screen.blit(worst_keystroke, worst_keystroke_rect)

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    window(1280, 720, 60)