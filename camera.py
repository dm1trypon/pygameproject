import pygame

from pygame import *
from collision import Screen
from objects import Objects
from bullet import Bullet
from const import *

class Camera:
    def __init__(self, position_x, position_y, nick_name):
        self.position_x = position_x
        self.position_y = position_y
        self.objects = Objects(nick_name)
        self.collision = Screen(nick_name, position_x, position_y, nick_name)

    def move(self, key_event):
        for obj in self.objects.get_borders():
                obj.move_camera(key_event)

        for obj in self.objects.get_bullets():
                obj.move_camera(key_event)
