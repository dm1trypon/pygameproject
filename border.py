import pygame

from const import *

class Border:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.speed = PLAYER_SPEED

    def move(self, key_event):
        self.position_x -= self.speed
        self.position_y -= self.speed