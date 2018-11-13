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

clock = pygame.time.Clock()

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class Main:
    def __init__(self):
        self.nick_name = "Player"
        self.bullets = []
        self.player = Player(100, 100, self.nick_name, PLAYER_COLOR)

    def get_objects(self, mouse_click):
        id_bullet = self.nick_name + str(random.randint(1, 1000))
        self.bullets.append(Bullet(self.player.get(POS_X), self.player.get(POS_Y), mouse_click, self.player.get(NAME), id_bullet, BULLET_COLOR))

    def set_objects(self, id_bullet):
        self.bullets.remove(id_bullet)

    def main(self):
        pygame.init()
        screen = pygame.display.set_mode(DISPLAY)
        pygame.display.set_caption(DESCRIPTION_GAME)
        bg = Surface((WIN_WIDTH, WIN_HEIGHT))
        bg.fill(Color(BACKGROUND_COLOR))
        keys = Keys()
        level = Level(LEVEL_WIDTH, LEVEL_HEIGHT)
        while True:
            pressed = pygame.mouse.get_pressed()
            if pressed[0]:
                mouse_click = pygame.mouse.get_pos()
                self.get_objects(mouse_click)

            for obj in self.bullets:
                obj.draw(screen)

            self.player.draw(screen)
            e = pygame.event.poll()
            if e.type == pygame.QUIT:
                return

            keys.key_events(self.player)
            pygame.display.update()
            screen.blit(bg, (0, 0))
            level.draw_map(screen)
            clock.tick(FPS)


if __name__ == "__main__":
    main = Main()
    main.main()