import pygame
import sys
from pygame.locals import *
pygame.init()
TestWindow = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Test Window')
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_q:
                print("You are quitting")
                pygame.time.delay(1000)
                pygame.quit()
                sys.exit()
