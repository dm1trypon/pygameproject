import pygame

from const import *
from pygame import *
from border import Border
from objects import Objects

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class Level:
    def __init__(self, width, height, objects, screen):
        self.objects = objects
        self.point_xy = 0
        self.width_level = width
        self.height_level = height
        self.generate_map(screen)
        
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

    def set_point_xy(self, point_xy):
        self.point_xy = point_xy

    def get_line_minus(self):
        line = ""
        i = 0
        while i < self.width_level:
            line += BLOCK
            i = i + 1

        return line

    def generate_map(self, screen):
        position_x = position_y = 0
        for row in self.generate_level():
            for col in row:
                if col == BLOCK:
                    self.objects.set_add_border(Border(screen, position_x, position_y, self.objects.get_id(), self.objects))

                position_x += PLATFORM_WIDTH
            position_y += PLATFORM_HEIGHT
            position_x = 0

    def draw(self):
        for obj in self.objects.get_borders():
            obj.draw()