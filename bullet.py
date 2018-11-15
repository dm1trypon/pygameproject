import pygame

from const import *
from pygame import *
from math import sqrt, exp
from collision import Screen
from objects import Objects

class Bullet:
    def __init__(self, pos_x, pos_y, mouse_click, nick_name, bullet_id, color):
        self.position_x = pos_x
        self.position_y = pos_y
        self.bullet_name = nick_name
        self.bullet_color = color
        self.bullet_speed = BULLET_SPEED
        self.player_speed = PLAYER_SPEED
        self.to_x = mouse_click[X]
        self.to_y = mouse_click[Y]
        self.speed_x = self.get_speed()[X]
        self.speed_y = self.get_speed()[Y]
        self.bullet_id = bullet_id
        self.screen = Screen(nick_name, pos_x, pos_y, self.bullet_id)
        self.objects = Objects(nick_name)

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
        print("Move bullet id: ", self.bullet_id, ", pos_x = ", self.position_x, ", pos_y = ", self.position_y)
        if not self.screen.on_screen(self.position_x, self.position_y):
            print("Delete bullet id: ", self.bullet_id)
            self.objects.set_del_bullet(self.bullet_id)
            return

        self.position_x += int(self.speed_x)
        self.position_y += int(self.speed_y)

    def get_diag_speed(self):
        return int(sqrt(2 * self.player_speed * self.player_speed) * TRIANGLE_RULE)

    def move_camera(self, key_event):
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