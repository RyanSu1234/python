import pygame
import sys
import random
import os
import time

os.chdir(sys.path[0])
from pygame.locals import *


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
gophers1 = pygame.image.load("Gophers2_150.png")

ham1 = pygame.image.load("Hammer1.png")
ham2 = pygame.image.load("Hammer2.png")
pygame.mixer.music.load("hit.mp3")

pos6 = [[195, 305], [400, 305], [610, 305], [195, 450], [400, 450], [610, 450]]

tick = 0
max_tick = 50
pos = pos6[0]

times = 0
times_max = 100

score = 0
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 24)

end_font = pygame.font.Font(typeface, 36)
end_sur = end_font.render(str(times), True, RED)

pygame.mouse.set_visible(False)  #隱藏滑鼠
mpos = (0, 0)

clock = pygame.time.Clock()
while True:
    clock.tick(30)
    hammer = ham2
    hitsur = gophers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            hammer = ham1
            mpos = pygame.mouse.get_pos()
            if check_click(mpos, pos[0] - 50, pos[1] - 50, pos[0] + 50,
                           pos[1] + 50):
                if times < times_max:
                    tick = max_tick + 1
                    pygame.mixer.music.play()
                    score += 1
                    hitsur = gophers1
        elif event.type == pygame.MOUSEMOTION:
            mpos = pygame.mouse.get_pos()

    if times > times_max:
        sur.fill((0, 0, 0))
        pygame.mouse.set_visible(True)
        end_sur = score_font.render(
            "Your Score is:{}/{}".format(score, times_max), False, RED)
        screen.blit(sur, (0, 0))
        screen.blit(end_sur, (100, 100))
        pygame.display.update()
    else:

        if tick > max_tick:
            times = times + 1
            score_sur = score_font.render(str(score), True, RED)
            end_sur = score_font.render(str(times), True, RED)
            new_pos = random.randint(0, 5)
            pos = pos6[new_pos]
            tick = 0
        else:
            tick += 1

        sur.blit(bg, (0, 0))
        sur.blit(hitsur, (pos[0] - hitsur.get_width() / 2,
                          pos[1] - hitsur.get_height() / 2))
        sur.blit(hammer, (mpos[0] - hammer.get_width() / 2,
                          mpos[1] - hammer.get_height() / 2))
        screen.blit(sur, (0, 0))
        score_sur = score_font.render(str(score), False, RED)
        screen.blit(score_sur, (10, 10))
        pygame.display.flip()
        if (hammer == ham1 or hitsur == gophers1):
            time.sleep(0.05)
