import pygame

from pygame import *
from const import *
from objects import Objects

class Screen:
    def __init__(self, nick_name, pos_x, pos_y, bullet_id):
        self.border_right = PLATFORM_WIDTH * (LEVEL_WIDTH - 1) - PLAYER_RADIUS
        self.border_left = PLATFORM_WIDTH + PLAYER_RADIUS
        self.border_bottom = PLATFORM_HEIGHT * (LEVEL_HEIGHT - 1) - PLAYER_RADIUS
        self.border_top = PLATFORM_HEIGHT + PLAYER_RADIUS
        self.player_speed = PLAYER_SPEED
        self.objects = Objects(nick_name)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.bullet_id = bullet_id

    def on_screen(self, position_x, position_y):
        print(position_x, position_y, self.border_right)
        return self.on_left_screen(position_x) and self.on_right_screen(position_x) and self.on_bottom_screen(position_y) and self.on_top_screen(position_y)

    def on_right_screen(self, position_x):
        return position_x < PLATFORM_WIDTH * (LEVEL_WIDTH - 1) - PLAYER_RADIUS

    def on_left_screen(self, position_x):
        return position_x > PLATFORM_WIDTH + PLAYER_RADIUS

    def on_bottom_screen(self, position_y): 
        return position_y < PLATFORM_HEIGHT * (LEVEL_HEIGHT - 1) - PLAYER_RADIUS

    def on_top_screen(self, position_y):
        return position_y > PLATFORM_HEIGHT + PLAYER_RADIUS

    def move_camera(self, key_event):
        for obj in self.objects.get_borders():
            if self.pos_x + BULLET_RADIUS > obj.position_x and self.pos_x < obj.position_x + PLATFORM_WIDTH:
                print("Delete bullet id: ", self.bullet_id)
                obj.set_del_bullet(self.bullet_id)
            if self.pos_y + BULLET_RADIUS > obj.position_y and self.pos_y < obj.position_y + PLATFORM_HEIGHT:
                print("Delete bullet id: ", self.bullet_id)
                obj.set_del_bullet(self.bullet_id)