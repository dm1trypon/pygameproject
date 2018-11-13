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
        self.player_speed = 5

    def create(self, screen):
        pygame.draw.circle(screen, self.player_color, (self.position_x, self.position_y), PLAYER_RADIUS)

    def get_diag_speed(self):
        return int(sqrt(2 * self.player_speed * self.player_speed) * TRIANGLE_RULE)

    def move(self, key_event):
        if not self.on_screen():
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
        if not self.on_left_screen(): self.position_x += 5
        if not self.on_right_screen(): self.position_x -= 5
        if not self.on_bottom_screen(): self.position_y -= 5
        if not self.on_top_screen(): self.position_y += 5

    def on_screen(self):
        return self.on_left_screen() and self.on_right_screen() and self.on_bottom_screen() and self.on_top_screen()

    def on_right_screen(self):
        return self.position_x < PLATFORM_WIDTH * (LEVEL_WIDTH - 1) - PLAYER_RADIUS

    def on_left_screen(self):
        return self.position_x > PLATFORM_WIDTH + PLAYER_RADIUS

    def on_bottom_screen(self):
        return self.position_y < PLATFORM_HEIGHT * (LEVEL_HEIGHT - 1) - PLAYER_RADIUS

    def on_top_screen(self):
        return self.position_y > PLATFORM_HEIGHT + PLAYER_RADIUS