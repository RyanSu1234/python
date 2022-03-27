import random
from turtle import ycor
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

mp3_path = 'pygame/20220320/music1.mp3'
pygame.mixer.music.load(mp3_path)
pygame.mixer.music.play()
pygame.mixer.music.fadeout(600000)

typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render('Start', True, (0, 35, 245))
tit_w = title.get_width()
tit_h = title.get_height()
title1 = font.render('Fast', True, (0, 35, 245))
tit_w1 = title.get_width()
tit_h1 = title.get_height()

act = False
speed = False  # F=slow , T=fast

snow_list = []

for i in range(300):
    x_site = random.randrange(0, background_x)  #圓心位置
    y_site = random.randrange(-1000, -1)  #圓心位置
    x_shift = random.randrange(-5, 0)  #x軸偏移量
    radius = random.randrange(4, 6)  #半徑和y下降量
    snow_list.append([x_site, y_site, x_shift, radius])

clock = pygame.time.Clock()
cnt = 0
while True:
    if cnt <= 10:
        cnt += 1
    else:
        cnt = 0
    x_shift = random.randrange(-5, 0)  #x軸偏移量

    if speed == True:
        title1 = font.render('Fast', True, (0, 0, 1))
        clock.tick(80)
    else:
        title1 = font.render('Slow', True, (0, 0, 0))
        clock.tick(20)

    mouse_pos = pygame.mouse.get_pos()
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos, 0, 0, tit_w, tit_h):
                act = not (act)
            if check_click(mouse_pos, 0, 50, tit_w1, tit_h1 + 50):
                speed = not (speed)

    if act == True:
        title = font.render('Stop', True, (0, 0, 0))
    else:
        title = font.render('Start', True, (0, 0, 0))

        #pygame.draw.circle(screen, (255, 255, 255), (x_site, y_site), radius)
        for snow in snow_list:
            pygame.draw.circle(screen, (0, 35, 245), (snow[0], snow[1]),
                               snow[3])

            snow[0] += snow[2]
            snow[1] += snow[3]

            if snow[1] > background_y or snow[0] > background_x:
                snow[1] = random.randrange(-10, -1)
                snow[0] = random.randrange(0, background_x)

    screen.blit(title, (0, 0))
    screen.blit(title1, (0, 50))
    pygame.display.update()
