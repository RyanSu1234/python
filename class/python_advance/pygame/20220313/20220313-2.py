import random
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
background_img = "pygame/20220313/snow.jpg"
background = pygame.image.load(background_img)

background_x = background.get_width()
background_y = background.get_height()

screen = pygame.display.set_mode((background_x, background_y))
pygame.display.set_caption("My Game")

typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render('Start', True, (128, 255, 255))
tit_w = title.get_width()
tit_h = title.get_height()

act = False

x_site = random.randrange(0, background_x)  #圓心位置
y_site = random.randrange(-70, -59)  #圓心位置
x_shift = random.randrange(-5, 5)  #x軸偏移量
radius = random.randrange(4, 6)  #半徑和y下降量

clock = pygame.time.Clock()
cnt = 0
while True:
    if cnt <= 10:
        cnt += 1
    else:
        cnt = 0
    x_shift = random.randrange(-5, 5)  #x軸偏移量
    clock.tick(40)
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos, 0, 0, tit_w, tit_h):
                act = not (act)

    screen.blit(background, (0, 0))
    if act == True:
        title = font.render('Stop', True, (0, 0, 0))
    else:
        title = font.render('Start', True, (0, 0, 0))

        pygame.draw.circle(screen, (255, 255, 255), (x_site, y_site), radius)

        x_site += x_shift
        y_site += radius

        if y_site > background_y or x_site > background_x:
            y_site = random.randrange(-10, -1)
            x_site = random.randrange(0, background_x)

    screen.blit(title, (0, 0))

    pygame.display.update()
