import pygame

from collision import Collision
from const import *
from math import sqrt, exp

class Border:
    def __init__(self, screen, position_x, position_y, border_id, objects):
        self.screen = screen
        self.position_x = position_x
        self.position_y = position_y
        self.player_speed = PLAYER_SPEED
        self.border_color = BORDER_COLOR
        self.border_id = border_id
        self.objects = objects
        self.collision = Collision()

    def get_diag_speed(self):
        return int(sqrt(2 * self.player_speed * self.player_speed) * TRIANGLE_RULE)

    def move_camera(self, key_event):
        if not self.collision.on_screen(self.position_x, self.position_y):
            print ("Collision...")
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

    def move_stabilize(self):
        if not self.collision.on_left_screen(self.position_x): self.position_x += PLAYER_SPEED
        if not self.collision.on_right_screen(self.position_x): self.position_x -= PLAYER_SPEED
        if not self.collision.on_bottom_screen(self.position_y): self.position_y -= PLAYER_SPEED
        if not self.collision.on_top_screen(self.position_y): self.position_y += PLAYER_SPEED

    def draw(self):
        pygame.draw.rect(self.screen, self.border_color, ((int(self.position_x), int(self.position_y)), (PLATFORM_WIDTH, PLATFORM_HEIGHT)))