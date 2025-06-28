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

    def render(self, surface, pos):
        self.surface.fill(Color.white)
        self.surface.blit(Font.neodgm_32.render(f'{self.energy}', False, Color.black), UI.Card.text_energy)
        pygame.draw.rect(self.surface, Color.black, [0, 0, UI.Card.size[0], UI.Card.size[1]], 2)
        self.surface.blit(Image.card[self.ID], UI.Card.image)
        pygame.draw.rect(self.surface, Color.black, UI.Card.image, 2)
        self.surface.blit(Font.neodgm_16.render(f'{self.name}', False, Color.black), UI.Card.text_name)
        render_text_box(self.surface, Font.neodgm_16, self.description, UI.Card.text_d_start, UI.Card.text_d_interval)
        surface.blit(self.surface, pos)