import pygame

from pygame import *
from const import *

class Screen:
    def on_screen(self, position_x, position_y):
        return self.on_left_screen(position_x) and self.on_right_screen(position_x) and self.on_bottom_screen(position_y) and self.on_top_screen(position_y)

    def on_right_screen(self, position_x):
        return position_x < PLATFORM_WIDTH * (LEVEL_WIDTH - 1) - PLAYER_RADIUS

    def on_left_screen(self, position_x):
        return position_x > PLATFORM_WIDTH + PLAYER_RADIUS

    def on_bottom_screen(self, position_y):
        return position_y < PLATFORM_HEIGHT * (LEVEL_HEIGHT - 1) - PLAYER_RADIUS

    def on_top_screen(self, position_y):
        return position_y > PLATFORM_HEIGHT + PLAYER_RADIUS