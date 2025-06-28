import pygame, copy
from script.module import *

class Card():
    def __init__(self):
        self.ID = 0
        self.name = ''
        self.energy = ''
        self.element = ''
        self.type = ''
        self.energy = 0
        self.effect = []
        self.description = []

        self.surface = pygame.surface.Surface(UI.Card.size)

    def set_data(self, ID):
        data_c = copy.deepcopy(data_card[ID])
        data_d = copy.deepcopy(data_card_d[ID])
        self.ID = ID
        self.name = data_c['name']
        self.energy = data_c['energy']
        self.element = data_c['element']
        self.type = data_c['type']
        self.effect = data_c['effect']
        self.description = data_d['description']