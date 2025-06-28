import copy, pygame
from script.module import *

class Player():
    def __init__(self):
        self.player_level = 1
        self.player_exp = 0
        self.player_exp_max = 0
        self.adventure_mode = False
        self.inventory = []
        self.deck = []
        self.weapon = []
        self.equipment = []
        self.item = []

    def load_save(self, save):
        s = copy.deepcopy(save)
        self.player_level = s['player_level']
        self.player_exp = s['player_exp']
        self.player_exp_max = s['player_exp_max']
        self.inventory = s['inventory']
        self.adventure_mode = s['adventure_mode']

    def write_save(self, save):
        save['player_level'] = self.player_level
        save['player_exp'] = self.player_exp
        save['player_exp_max'] = self.player_exp_max
        save['inventory'] = copy.deepcopy(self.inventory)
        save['adventure_mode'] = self.adventure_mode

class InventoryThing():
    def __init__(self):
        self.ID = 0
        self.name = ''
        self.element = ''
        self.rarity = ''
        self.effect = []
        self.description = []
        self.surface = pygame.surface.Surface([80, 80])

    def set_data(self, d, dd):
        self.name = d['name']
        self.element = d['element']
        self.rarity = d['rarity']
        self.effect = d['effect']
        self.description = dd['description']

class Weapon(InventoryThing):
    def __init__(self):
        super().__init__()

    def set_data(self, ID):
        d = copy.deepcopy(data_weapon[ID])
        dd = copy.deepcopy(data_weapon_d[ID])
        self.ID = ID
        super().set_data(d, dd)
        self.energy = d['energy']

    def render(self, surface):
        pass

class Equipment(InventoryThing):
    def __init__(self):
        super().__init__()

    def set_data(self, ID):
        d = copy.deepcopy(data_equipment[ID])
        dd = copy.deepcopy(data_equipment_d[ID])
        self.ID = ID
        super().set_data(d, dd)

class Item(InventoryThing):
    def __init__(self):
        super().__init__()

    def set_data(self, ID):
        d = copy.deepcopy(data_item[ID])
        dd = copy.deepcopy(data_item_d[ID])
        self.ID = ID
        super().set_data(d, dd)