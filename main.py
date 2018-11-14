#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random

from const import *
from pygame import *
from key_events import Keys
from level import Level
from player import Player
from bullet import Bullet
from objects import Objects
from camera import Camera

clock = pygame.time.Clock()

class Main:
    def __init__(self):
        self.nick_name = "Player"
        self.screen = pygame.display.set_mode(DISPLAY)
        self.bg = Surface((WIN_WIDTH, WIN_HEIGHT))
        self.player = Player(100, 100, self.nick_name, PLAYER_COLOR)
        self.keys = Keys()
        self.objects = Objects(self.nick_name)
        self.level = Level(LEVEL_WIDTH, LEVEL_HEIGHT)
        self.camera = Camera(100, 100, self.nick_name)

    def add_bullet(self, mouse_click):
        return Bullet(self.player.get(POS_X),
                    self.player.get(POS_Y),
                    mouse_click, self.player.get(NAME),
                    self.objects.get_id(),
                    BULLET_COLOR)

    def animation(self):
        while True:
            pressed = pygame.mouse.get_pressed()
            if pressed[0]:
                self.objects.set_add(self.add_bullet(pygame.mouse.get_pos()))

            for obj in self.objects.get_bullets():
                obj.draw(self.screen)

            self.player.draw(self.screen)
            e = pygame.event.poll()
            if e.type == pygame.QUIT:
                return

            # self.keys.key_events(self.player)
            self.keys.key_events(self.camera)
            pygame.display.update()
            self.screen.blit(self.bg, (0, 0))
            self.level.draw_map(self.screen)
            clock.tick(FPS)

    def main(self):
        pygame.init()
        pygame.display.set_caption(DESCRIPTION_GAME)
        bg = Surface((WIN_WIDTH, WIN_HEIGHT))
        bg.fill(Color(BACKGROUND_COLOR))
        self.level = Level(LEVEL_WIDTH, LEVEL_HEIGHT)
        self.animation()


if __name__ == "__main__":
    main = Main()
    main.main()