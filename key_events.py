import pygame

from pygame import *
from const import *

class Keys:
    def key_events(self, player):
        press = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] and keys[pygame.K_d] and not press:
            player.move(DOWN_RIGHT)
            press = True

        if keys[pygame.K_s] and keys[pygame.K_a] and not press:
            player.move(DOWN_LEFT)
            press = True

        if keys[pygame.K_w] and keys[pygame.K_d] and not press:
            player.move(UP_RIGHT)
            press = True

        if keys[pygame.K_w] and keys[pygame.K_a] and not press:
            player.move(UP_LEFT)
            press = True

        if keys[pygame.K_a] and not press :
            player.move(LEFT)
            press = True

        if keys[pygame.K_d] and not press:
            player.move(RIGHT)
            press = True

        if keys[pygame.K_w] and not press:
            player.move(UP)
            press = True

        if keys[pygame.K_s] and not press:
            player.move(DOWN)
            press = True