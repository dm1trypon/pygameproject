import pygame

from const import *
from pygame import *

class Level:
    def __init__(self, width, height):
        self.width_level = width
        self.height_level = height
        
    def generate_level(self):
        level = []
        i = 0
        while i < self.height_level:
            if i == 0 or i == self.height_level - 1 :
                level.append(self.get_line_minus())
            else:
                level.append(self.get_line_space())
            
            i = i + 1

        return level
            
    def get_line_space(self):
        line = ""
        i = 0
        while i < self.width_level:
            if i == 0 or i == self.width_level - 1:
                line += BLOCK
            else:
                line += SPACE
            
            i = i + 1

        return line

    def get_line_minus(self):
        line = ""
        i = 0
        while i < self.width_level:
            line += BLOCK
            i = i + 1

        return line

    def draw_map(self, screen):
        x = y = 0
        for row in self.generate_level():
            for col in row:
                if col == BLOCK:
                    pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                    pf.fill(Color(PLATFORM_COLOR)) 
                    screen.blit(pf, (x, y))
                            
                x += PLATFORM_WIDTH
            y += PLATFORM_HEIGHT
            x = 0    