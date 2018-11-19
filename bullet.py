import pygame

from const import *
from pygame import *
from math import sqrt, exp
from collision import Collision
from objects import Objects

class Bullet:
    def __init__(self, position_x, position_y, mouse_click, nick_name, bullet_id, color, objects):
        self.position_x = position_x
        self.position_y = position_y
        self.bullet_name = nick_name
        self.bullet_color = color
        self.bullet_speed = BULLET_SPEED
        self.player_speed = PLAYER_SPEED
        self.mouse_click_x = mouse_click[X]
        self.mouse_click_y = mouse_click[Y]
        self.speed_x = self.get_speed()[X]
        self.speed_y = self.get_speed()[Y]
        self.bullet_id = bullet_id
        self.objects = objects
        self.collision = Collision()
        

    def draw(self, screen):
        pygame.draw.circle(screen, self.bullet_color, (self.position_x, self.position_y), BULLET_RADIUS)
        self.move()

    def get_speed(self):
        speed_x = ((self.mouse_click_x - self.position_x)
                    * self.bullet_speed
                    / sqrt((self.mouse_click_x - self.position_x) ** 2
                    + (self.mouse_click_y - self.position_y) ** 2))

        speed_y = ((self.mouse_click_y - self.position_y)
                    * self.bullet_speed
                    / sqrt((self.mouse_click_x - self.position_x) ** 2
                    + (self.mouse_click_y - self.position_y) ** 2))

        return (speed_x, speed_y)

    def move(self):
        print("Move bullet id: ", self.bullet_id, ", pos_x = ", self.position_x, ", pos_y = ", self.position_y)
        if not self.collision.on_screen(self.position_x, self.position_y):
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