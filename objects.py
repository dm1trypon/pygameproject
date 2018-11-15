import random

from const import *

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class Objects:
    def __init__(self, nick_name):
        self.bullets = []
        self.borders = []
        self.enemy_players = []
        self.collision = None
        self.nick_name = nick_name

    def get_borders(self):
        return self.borders

    def get_enemy_players(self):
        return self.enemy_players

    def get_bullets(self):
        return self.bullets

    def get_id(self):
        return self.nick_name + str(random.randint(RAND_FROM, RAND_TO))

    def get_collision(self):
        return self.collision

    def set_collision(self, collision):
        self.collision = collision

    def set_add_enemy_players(self, enemy_player):
        self.enemy_players.append(enemy_player)

    def set_add_bullet(self, bullet):
        self.bullets.append(bullet)

    def set_add_border(self, border):
        self.borders.append(border)

    def set_del_bullet(self, bullet_id):
        for item in self.bullets:
            if item.bullet_id == bullet_id:
                self.bullets.remove(item)