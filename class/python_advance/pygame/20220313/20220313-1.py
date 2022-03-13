import math
import pygame
import sys


def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = pos[0] > x_min and pos[0] < x_max
    y_match = pos[1] > y_min and pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


pygame.init()
width = 640
heigh = 320

screen = pygame.display.set_mode((width, heigh))
pygame.display.set_caption("My Game")

background = pygame.Surface((width, heigh))
background.fill((0, 0, 0))

# pygame.draw.circle(background, (167, 23, 225), (300, 140), 180, 0)
# pygame.draw.circle(background, (0, 0, 225), (200, 100), 30, 0)
# pygame.draw.circle(background, (0, 0, 225), (400, 100), 30, 0)
# pygame.draw.rect(background, (0, 0, 225), [270, 130, 60, 40], 0)
# pygame.draw.ellipse(background, (255, 10, 0), [130, 160, 60, 35], 2)
# pygame.draw.ellipse(background, (255, 10, 0), [400, 160, 60, 35], 2)
# #pygame.draw.polygon(background, (100, 200, 45), [[100, 100],[0,200],[200, 200]], 0)
# pygame.draw.arc(background, (255, 10, 0), [252, 200, 100, 50],
#                 math.radians(230), math.radians(0), 2)

act = False

typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render('Start', True, (128, 255, 255))
tit_w = title.get_width()
tit_h = title.get_height()

while True:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos, 0, 0, tit_w, tit_h):
                act = not (act)

    screen.blit(background, (0, 0))
    if act:
        pygame.draw.circle(background, (167, 23, 225), (300, 140), 180, 0)
        pygame.draw.circle(background, (0, 0, 225), (200, 100), 30, 0)
        pygame.draw.circle(background, (0, 0, 225), (400, 100), 30, 0)
        pygame.draw.rect(background, (0, 0, 225), [270, 130, 60, 40], 0)
        pygame.draw.ellipse(background, (255, 10, 0), [130, 160, 60, 35], 2)
        pygame.draw.ellipse(background, (255, 10, 0), [400, 160, 60, 35], 2)
        #pygame.draw.polygon(background, (100, 200, 45), [[100, 100],[0,200],[200, 200]], 0)
        pygame.draw.arc(background, (255, 10, 0), [252, 200, 100, 50],
                        math.radians(230), math.radians(0), 2)
    else:
        background.fill((0, 0, 0))
        screen.blit(title, (0, 0))

    pygame.display.update()
