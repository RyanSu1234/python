import math
import pygame
import sys

pygame.init()
width = 640
heigh = 320



screen = pygame.display.set_mode((width, heigh))
pygame.display.set_caption("My Game")

background = pygame.Surface((width, heigh))
background.fill((22,224,225))

pygame.draw.circle(background, (0, 0, 225), (200, 100), 30, 0)
pygame.draw.rect(background, (0, 0, 225), [270, 130,60,40], 0)
pygame.draw.ellipse(background, (0, 0, 225), [130,160,60,35], 0)
pygame.draw.polygon(background, (100, 200, 45), [[100, 100],[0,200],[200, 200]], 0)
pygame.draw.arc(background, (255, 10, 0), [100, 100, 100, 50], math.radians(180),math.radians(0), 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(background, (0, 0))
    pygame.display.update()