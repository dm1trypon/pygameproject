import pygame

from pygame import *
from objects import Objects
from bullet import Bullet
from const import *

class Camera:
    def __init__(self, position_x, position_y, objects):
        self.position_x = position_x
        self.position_y = position_y
        self.objects = objects

    def move(self, key_event):
        for obj in self.objects.get_borders():
            obj.move_camera(key_event)

        for obj in self.objects.get_bullets():
            obj.move_camera(key_event)
