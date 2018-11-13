#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

from const import *
from pygame import *
from key_events import Keys
from level import Level
from player import Player

clock = pygame.time.Clock()

def main():
    
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption(DESCRIPTION_GAME)
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color(BACKGROUND_COLOR))
    player = Player(100, 100, "Player", PLAYER_COLOR)
    keys = Keys()
    level = Level(LEVEL_WIDTH, LEVEL_HEIGHT)
    while True:
        player.create(screen)
        e = pygame.event.poll()
        if e.type == pygame.QUIT:
            return

        keys.key_events(player)
        pygame.display.update()
        screen.blit(bg, (0, 0))
        level.draw_map(screen)
        clock.tick(FPS)


if __name__ == "__main__":
    main()