import pygame

from collision import Screen
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
        self.screen = Screen()

    def draw(self, screen):
        pygame.draw.circle(screen, self.player_color, (self.position_x, self.position_y), PLAYER_RADIUS)

    def get_diag_speed(self):
        return int(sqrt(2 * self.player_speed * self.player_speed) * TRIANGLE_RULE)

    def move(self, key_event):
        if not self.screen.on_screen(self.position_x, self.position_y):
            self.move_stabilize(self.position_x, self.position_y)
            return

        if (key_event == LEFT):
            self.position_x -= self.player_speed

        if (key_event == RIGHT):
            self.position_x += self.player_speed

        if (key_event == UP):
            self.position_y -= self.player_speed

        if (key_event == DOWN):
            self.position_y += self.player_speed

        if (key_event == DOWN_RIGHT):
            self.position_x += self.get_diag_speed()
            self.position_y += self.get_diag_speed()

        if (key_event == DOWN_LEFT):
            self.position_x -= self.get_diag_speed()
            self.position_y += self.get_diag_speed()

        if (key_event == UP_RIGHT):
            self.position_x += self.get_diag_speed()
            self.position_y -= self.get_diag_speed()

        if (key_event == UP_LEFT):
            self.position_x -= self.get_diag_speed()
            self.position_y -= self.get_diag_speed()

    def move_stabilize(self, pos_x, pos_y):
        if not self.screen.on_left_screen(self.position_x): self.position_x += PLAYER_SPEED
        if not self.screen.on_right_screen(self.position_x): self.position_x -= PLAYER_SPEED
        if not self.screen.on_bottom_screen(self.position_y): self.position_y -= PLAYER_SPEED
        if not self.screen.on_top_screen(self.position_y): self.position_y += PLAYER_SPEED

    def get(self, val):
        if (val == POS_X): return self.position_x
        if (val == POS_Y): return self.position_y
        if (val == NAME): return self.player_name