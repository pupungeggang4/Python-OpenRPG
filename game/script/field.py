import pygame, json
from script.module import *

class PlayerField():
    def __init__(self):
        self.rect = Rect2(0, 0, 80, 80)
        self.surface = pygame.surface.Surface([self.rect.size.x, self.rect.size.y], pygame.SRCALPHA)

    def render(self, surface, camera):
        self.surface.fill(Color.transparent)
        pygame.draw.rect(self.surface, Color.black, [0, 0, 80, 80], 2)
        render_surface_camera(surface, self.surface, self.rect, camera)

class Field():
    def __init__(self):
        self.place = ''
        self.player = PlayerField()
        self.thing = []
        self.monster = []

        self.camera = Rect2(0, 0, 1280, 720)
        self.surface = pygame.surface.Surface([1280, 720])

    def render(self, surface):
        self.surface.fill(Color.white)
        self.player.render(self.surface, self.camera)
        surface.blit(self.surface, [0, 0])

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
