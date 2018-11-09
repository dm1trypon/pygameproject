#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

from const import *
from pygame import *
from level import level

def draw_map(screen):
    x=y=0
    for row in level:
        for col in row:
            if col == "-":
                pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                pf.fill(Color(PLATFORM_COLOR)) 
                screen.blit(pf,(x,y))
                        
            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0 

def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("PyGame")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))

    bg.fill(Color(BACKGROUND_COLOR))

    while 1:
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit
        screen.blit(bg, (0,0)) 
        pygame.display.update()
        draw_map(screen)
        

if __name__ == "__main__":
    main()