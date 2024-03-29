#===載入套件開始===
import pygame
import sys
import os

os.chdir(sys.path[0])
from pygame.locals import *
import random
#***載入套件結束***

img_gg = pygame.image.load('gameover.png')
gg_w = img_gg.get_width()
gg_h = img_gg.get_height()


def game_over(win):
    global live

    win.blit(img_gg, ((bg_x - gg_w) / 2, (bg_y - gg_h) / 2))


#===初始化設定開始===
'''顏色'''
BlOCK = (0, 0, 0)
WHITE = (225, 225, 225)
RED = (225, 0, 0)
BLUE = (0, 255, 255)
BLUE2 = (113, 231, 255)
'''初始'''
pygame.init()
'''時脈'''
clock = pygame.time.Clock()

game_mode = 1


def resetGame():
    global brick_num, bricks_list, dx, dy, act

    for bricks in bricks_list:
        r = random.randint(100, 200)
        g = random.randint(100, 200)
        b = random.randint(100, 200)
        bricks[5] = (r, g, b)
        bricks[4] = True

    brick_num = TOTAL_BLOCK
    dx = 8
    dy = -8
    act = False


'''
遊戲狀態
#False:等待開球
#True:遊戲進行中
'''

act = False
live = 3
#***初始化設定結束***

#===遊戲視窗設定開始===
bg_x = 800
bg_y = 600
bg_size = (bg_x, bg_y)

pygame.display.set_caption("打磚塊遊戲")

screen = pygame.display.set_mode(bg_size)

#***遊戲視窗設定結束***

#===磚塊設定開始===
TOTAL_BLOCK = 99
bricks_list = []
brick_num = 0
brick_x = 70
brick_y = 60
brick_w = 0
brick_h = 0
brick_v = True

for i in range(0, TOTAL_BLOCK):
    if ((i % 11) == 0):
        brick_w = 0
        brick_h += 18
    bricks_list.append(
        [brick_w + brick_x, brick_h + brick_y, 58, 16, brick_v, BLUE])
    brick_w += 60


def brick_update(win):
    global brick_num, dy
    for bricks in bricks_list:

        if (is_hit(ball_x, ball_y,
                   [bricks[0], bricks[1], bricks[2], bricks[3]])):
            if (bricks[4]):
                brick_num -= 1

                if (brick_num <= 0):
                    resetGame()
                    break

                dy = -dy

            bricks[4] = False
    for bricks in bricks_list:
        if (bricks[4] == True):
            block_rect = [bricks[0], bricks[1], bricks[2], bricks[3]]
            pygame.draw.rect(win, bricks[5], block_rect)


#===磚塊設定結束===

#===顯示磚塊數量設定開始===
typeface = pygame.font.get_default_font()
number_font = pygame.font.Font(typeface, 36)


def get_block_num(win):
    global brick_num

    sur = number_font.render(str(brick_num), True, RED)
    win.blit(sur, [10, 10])


def get_live_num(win):
    global live

    sur1 = number_font.render(str(live), True, BLUE2)
    win.blit(sur1, [10, 60])


#===顯示磚塊數量設定結束===


#===碰撞設定開始===
def is_hit(x, y, boxRect):
    xmatch = x >= boxRect[0] and x <= boxRect[0] + boxRect[2]
    ymatch = y >= boxRect[1] and y <= boxRect[1] + boxRect[3]
    if (xmatch and ymatch):
        return True
    return False


#===碰撞設結束===

#===初始遊戲設定開始===
#===初始遊戲設定結束===

#===底板設定開始===
paddle_x = 0
paddle_y = (bg_y - 24)


def paddle_update(win):
    global dy, dx
    paddle_rect = [paddle_x, paddle_y, 100, 10]

    pygame.draw.rect(win, RED, paddle_rect)

    if (is_hit(ball_x, ball_y, paddle_rect)):
        dy = -dy


#===底板設定結束===

#===球設定開始===
ball_x = 400
ball_y = 300
ball_radius = 8
ball_diameter = ball_radius * 2
ball_color = WHITE
dx = 8
dy = -8


def ball_update(win):
    global ball_x, ball_y, brick_num
    global dx, dy, act, game_mode, live

    if (act == False):
        ball_x = paddle_x + 50
        ball_y = paddle_y - ball_radius
    else:

        ball_x += dx
        ball_y += dy

        if brick_num < 70:

            if dy < 0:
                dy = -10
            else:
                dy = 10

            if dx < 0:
                dx = -10
            else:
                dx = 10

        if 47 < brick_num < 50:
            if dx < 0:
                dx = -8
            else:
                dx = 8
            if dy < 0:
                dy = -8
            else:
                dy = 8
            live += 1

        if brick_num < 30:

            if dy < 0:
                dy = -13
            else:
                dy = 13

            if dx < 0:
                dx = -13
            else:
                dx = 13

        if (ball_y > bg_y - ball_diameter):
            live -= 1
            act = False
            if (live <= 0.9):
                game_mode = 0

        if (ball_x > bg_x - ball_diameter or ball_x < ball_diameter):
            dx = -dx

        if (ball_y < ball_diameter):
            dy = -dy

    pygame.draw.circle(win, ball_color, [ball_x, ball_y], ball_radius)


#===球設定結束===

#===初始遊戲設定開始===

#===初始遊戲設定結束===
resetGame()
#-------------------------------------------------------------------------
# 主迴圈.
#-------------------------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            paddle_x = pygame.mouse.get_pos()[0] - 50

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (act == False):
                act = True

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                resetGame()
                game_mode = 1
                live = 3

    if (game_mode):

        screen.fill(BlOCK)

        ball_update(screen)

        paddle_update(screen)

        brick_update(screen)

        get_block_num(screen)

        get_live_num(screen)

    else:

        game_over(screen)

    pygame.display.update()
    clock.tick(60)
