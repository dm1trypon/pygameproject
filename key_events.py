import pygame

from pygame import *
from const import *

class Keys:
    def key_events(self, obj):
        press = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] and keys[pygame.K_d] and not press:
            obj.move(UP_LEFT)
            press = True

        if keys[pygame.K_s] and keys[pygame.K_a] and not press:
            obj.move(UP_RIGHT)
            press = True

        if keys[pygame.K_w] and keys[pygame.K_d] and not press:
            obj.move(DOWN_LEFT)
            press = True

        if keys[pygame.K_w] and keys[pygame.K_a] and not press:
            obj.move(DOWN_RIGHT)
            press = True

        if keys[pygame.K_a] and not press:
            obj.move(RIGHT)
            press = True

        if keys[pygame.K_d] and not press:
            obj.move(LEFT)
            press = True

        if keys[pygame.K_w] and not press:
            obj.move(DOWN)
            press = True

        if keys[pygame.K_s] and not press:
            obj.move(UP)
            press = True