import pygame
import sys
import random
import os

os.chdir(sys.path[0])


def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = pos[0] > x_min and pos[0] < x_max
    y_match = pos[1] > y_min and pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


pygame.init()
bg_img = "Gophers_BG_800x600.png"
bg = pygame.image.load(bg_img)
bg_x = bg.get_width()
bg_y = bg.get_height()
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
screen = pygame.display.set_mode([bg_x, bg_y])
sur = pygame.Surface([bg_x, bg_y])
pygame.display.set_caption("打地鼠")

gophers = pygame.image.load("Gophers150.png")

pos6 = [[195, 305], [400, 305], [610, 305], [2195, 450], [400, 450],
        [610, 450]]

tick = 0
max_tick = 20
pos = pos6[0]

score = 0
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 24)

clock = pygame.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            if check_click(mpos, pos[0] - 50, pos[1] - 50, pos[0] + 50,
                           pos[1] + 50):
                tick = max_tick + 1
                score += 1

    if tick > max_tick:
        new_pos = random.randint(0, 5)
        pos = pos6[new_pos]
        tick = 0
    else:
        tick += 1

    sur.blit(bg, (0, 0))
    sur.blit(
        gophers,
        (pos[0] - gophers.get_width() / 2, pos[1] - gophers.get_height() / 2))
    screen.blit(sur, (0, 0))

    score_sur = score_font.render(str(score), False, RED)
    screen.blit(score_sur, (10, 10))
    pygame.display.update()
