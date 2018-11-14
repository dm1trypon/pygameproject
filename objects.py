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
    def __init__(self, name):
        self.bullets = []
        self.nick_name = name

    def get_bullets(self):
        return self.bullets

    def get_id(self):
        return self.nick_name + str(random.randint(RAND_FROM, RAND_TO))

    def set_add(self, bullet):
        self.bullets.append(bullet)
        
    def set_del(self, bullet_id):
        for item in self.bullets:
            if item.bullet_id == bullet_id:
                self.bullets.remove(item)