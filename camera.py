import pygame

from pygame import *
from objects import Objects
from bullet import Bullet

class Camera:
    def __init__(self, position_x, position_y, nick_name):
        self.position_x = position_x
        self.position_y = position_y
        self.objects = Objects(nick_name)

    def move(self, key_event):
        pf = self.objects.get_pf_list()
        enemy_players = self.objects.get_enemy_players()
        bullets = self.objects.get_bullets()
        