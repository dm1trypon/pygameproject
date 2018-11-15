import pygame

from pygame import *
from const import *
from math import sqrt, exp

class Player:
    def __init__(self, pos_x, pos_y, name, color):
        self.position_x = pos_x
        self.position_y = pos_y
        self.player_name = name
        self.player_color = color
        self.player_speed = PLAYER_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, self.player_color, (self.position_x, self.position_y), PLAYER_RADIUS)

    def get(self, val):
        if (val == POS_X): return self.position_x
        if (val == POS_Y): return self.position_y
        if (val == NAME): return self.player_name