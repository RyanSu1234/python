#===載入套件開始
from turtle import screensize
import pygame
import sys
import os
import random

os.chdir(sys.path[0])
from pygame.locals import *
#***載入套件結束***

#===初始化設定開始===
LIMIT_LOW = 140
LIMIT_HIGH = 140
PTERA_LIMIT_LOW = 110
pygame.init()
timer = 0
clock = pygame.time.Clock()
RED = (255, 0, 0)
stuff = 0
#***初始化設定結束***

#===載入圖片開始===
img = pygame.image.load("bg.png")
img_dinosaur = [
    pygame.image.load("小恐龍1.png"),
    pygame.image.load("小恐龍2.png"),
]
img_cacti = pygame.image.load('cacti.png')
img_gg = pygame.image.load('gameover.png')

img_ptera = [
    pygame.image.load("翼龍飛飛1.png"),
    pygame.image.load("翼龍飛飛2.png"),
]

img_bend_down = [
    pygame.image.load("小恐龍蹲下1.png"),
    pygame.image.load("小恐龍蹲下2.png"),
]
#***載入圖片結束***

#===遊戲視窗設定開始===
bg_x = img.get_width()
bg_y = img.get_height()
bg_size = (bg_x, bg_y)
roll_x = 0

pygame.display.set_caption("Dinosuar")
screen = pygame.display.set_mode(bg_size)
#***遊戲視窗設定結束***

#===分數設定開始===
score = 0
typefase = pygame.font.get_default_font()
score_font = pygame.font.Font(typefase, 36)


def get_score(win):
    global score

    score_sur = score_font.render(str(score), True, RED)
    win.blit(score_sur, [10, 10])


#***分數設定結束***

#===恐龍設定開始===
dino_show = img_dinosaur
dino_limit = LIMIT_LOW
ds_x = 50
ds_y = dino_limit
jumpState = False
jumpValue = 0


def get_dino_limit(dino_img):
    return bg_y - 100 - dino_img[0].get_height()


def move_dinosaur(win, timer):
    global ds_x, ds_y, jumpState, jumpValue, dino_show, dino_limit

    if jumpState:
        if ds_y >= dino_limit:
            jumpValue = -5
        if ds_y <= 0:
            jumpValue = 10
        ds_y += jumpValue

        if ds_y >= LIMIT_LOW:
            jumpState = False
    win.blit(dino_show[timer % 20 // 10], [ds_x, ds_y])


#***恐龍設定結束***

#===仙人掌設定開始===
casti_w = img_cacti.get_width()
casti_h = img_cacti.get_height()
cacti_x = bg_x - 10
cacti_y = LIMIT_LOW
cacti_shift = 10
cacti_dist = int((casti_w + casti_h) / 2)


def move_cacti(win):
    global cacti_x, cacti_y, cacti_shift
    global score
    global stuff

    cacti_x -= cacti_shift
    win.blit(img_cacti, [cacti_x, cacti_y])
    if (cacti_x < 0):
        stuff = random.randint(0, 1)
        score += 1
        if (score > 20):
            cacti_x = bg_x - random.randint(100, 300)
            cacti_shift = random.randint(15, 30)
        elif (score > 10):
            cacti_x = bg_x - 100
            cacti_shift = random.randint(10, 30)
        else:
            cacti_x = bg_x - 100
            cacti_shift = 10


#***仙人掌設定結束***

#===翼龍設定開始===
ptera_w = img_ptera[0].get_width()
ptera_h = img_ptera[0].get_height()
ptera_x = bg_x - 100
ptera_y = PTERA_LIMIT_LOW
ptera_shift = 10
ptera_dist = int((ptera_w + ptera_h) / 2)


def move_ptera(win, timer):
    global ptera_x, ptera_y, ptera_shift
    global score
    global stuff

    ptera_x -= ptera_shift
    win.blit(img_ptera, [ptera_x, ptera_y])
    if (ptera_x < 0):
        stuff = random.randint(0, 1)
        score += 1
        if (score > 20):
            ptera_x = bg_x - random.randint(100, 300)
            ptera_shift = random.randint(15, 30)
        elif (score > 10):
            ptera_x = bg_x - 100
            ptera_shift = random.randint(10, 30)
        else:
            ptera_x = bg_x - 100
            ptera_shift = 10


#***翼龍設定結束***


#***碰撞設定結束***
def is_hit(x1, y1, x2, y2, r):
    if ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) < (r * r):
        return True
    else:
        return False


#***碰撞設定結束***

#===GameOver設定開始===
gg = False
gg_w = img_gg.get_width()
gg_h = img_gg.get_height()


def game_over(win):
    win.blit(img_gg, ((bg_x - gg_w) / 2, (bg_y - gg_h) / 2))


#***GameOver設定結束***

#===主程式開始===
while True:
    #===計時與速度===
    clock.tick(20)
    timer += 1
    #===偵測鍵盤事件開始===
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and ds_y <= dino_limit:
                jumpState = True
            elif event.key == K_RETURN and gg == True:
                gg = False
                cacti_x = bg_x - 100
                ds_x = 50
                ds_y = dino_limit
                score = 0
                jumpState = False
            elif event.key == K_DOWN and jumpState == False:
                dino_show = img_bend_down
                dino_limit = get_dino_limit(dino_show)
                ds_y = dino_limit
        elif event.type == KEYUP:
            if event.key == K_DOWN and jumpState == False:
                dino_show = img_dinosaur
                dino_limit = get_dino_limit(dino_show)
                ds_y = dino_limit

    if (gg == True):
        #===遊戲結束===
        game_over(screen)
    else:
        #===遊戲進行===
        roll_x = (roll_x - 10) % bg_x
        screen.blit(img, [roll_x - bg_x, 0])
        screen.blit(img, [roll_x, 0])
        #===更新角色狀態===
        move_dinosaur(screen, timer)

        if (stuff == 0):
            move_cacti(screen)
        else:
            move_ptera(screen, timer)

        get_score(screen)
        if (is_hit(ds_x, ds_y, ptera_x, ptera_y, ptera_dist)
                or is_hit(ds_x, ds_y, cacti_x, cacti_y, cacti_dist)):
            gg = True

    pygame.display.update()
#===主程式結束===