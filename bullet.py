import pygame

from const import *
from pygame import *
from link import Link
from math import sqrt, exp
from collision import Screen

class Bullet:
    def __init__(self, pos_x, pos_y, mouse_click, name, id_bullet, color):
        self.position_x = pos_x
        self.position_y = pos_y
        self.bullet_name = name
        self.bullet_color = color
        self.bullet_speed = BULLET_SPEED
        self.to_x = mouse_click[X]
        self.to_y = mouse_click[Y]
        self.speed_x = self.get_speed()[X]
        self.speed_y = self.get_speed()[Y]
        self.screen = Screen()
        self.link = Link()
        self.id_bullet = id_bullet
        self.main = self.link.get()

    def draw(self, screen):
        pygame.draw.circle(screen, self.bullet_color, (self.position_x, self.position_y), BULLET_RADIUS)
        self.move()

    def get_speed(self):
        speed_x = ((self.to_x - self.position_x)
                    * self.bullet_speed
                    / sqrt((self.to_x - self.position_x) ** 2
                    + (self.to_y - self.position_y) ** 2))

        speed_y = ((self.to_y - self.position_y)
                    * self.bullet_speed
                    / sqrt((self.to_x - self.position_x) ** 2
                    + (self.to_y - self.position_y) ** 2))

        return (speed_x, speed_y)

    def move(self):
        if not self.screen.on_screen(self.position_x, self.position_y):
            self.main.set_objects(self.id_bullet)
            return

        self.position_x += int(self.speed_x)
        self.position_y += int(self.speed_y)