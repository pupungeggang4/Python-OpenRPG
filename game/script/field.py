import pygame, json
from script.module import *

class PlayerField():
    def __init__(self):
        self.rect = Rect2(0, 0, 80, 80)
        self.surface = pygame.surface.Surface([self.rect.size.x, self.rect.size.y])

class Field():
    def __init__(self):
        self.place = ''
        self.thing = []
        self.monster = []

class FieldThing():
    def __init__(self):
        self.type = ''
        self.rect = Rect2(0, 0, 80, 80)
        self.surface = pygame.surface.Surface([self.rect.size.x, self.rect.size.y])

class FieldMonster(FieldThing):
    pass

class FieldEvent(FieldThing):
    pass

class FieldShop(FieldThing):
    pass

class FieldResource(FieldThing):
    pass
