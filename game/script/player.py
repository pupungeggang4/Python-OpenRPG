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
        self.weapon = Weapon()
        self.equipment = []
        self.item = []

    def start_adventure(self, game):
        ID = game.selected_deck + 1
        self.adventure_mode = True
        self.weapon = Weapon()
        self.weapon.set_data(data_deck[ID]['weapon'])
        self.deck = []
        for i in range(len(data_deck[ID]['card'])):
            card = Card()
            card.set_data(data_deck[ID]['card'][i])
            self.deck.append(card)
        equipment = Equipment()
        equipment.set_data(data_deck[ID]['equipment'])
        self.equipment.append(equipment)
        item = Item()
        item.set_data(1)
        self.item.append(item)
        
    def end_adventure(self, game):
        self.adventure_mode = False
        self.weapon = Weapon()
        self.deck = []
        self.equipment = []
        self.item = []

    def load_save(self, save):
        s = copy.deepcopy(save)
        self.player_level = s['player_level']
        self.player_exp = s['player_exp']
        self.player_exp_max = s['player_exp_max']
        self.adventure_mode = s['adventure_mode']
        self.inventory = []
        for i in range(len(s['inventory'])):
            inventory = InventoryItem()
            self.inventory.append(inventory)
        self.deck = []
        for i in range(len(s['deck'])):
            card = Card()
            card.set_data(s['deck'][i])
            self.deck.append(card)
        self.weapon.set_data(s['weapon'])
        self.equipment = []
        for i in range(len(s['equipment'])):
            equipment = Equipment()
            equipment.set_data(s['equipment'][i])
            self.equipment.append(equipment)
        self.item = []
        for i in range(len(s['item'])):
            item = Item()
            item.set_data(s['item'][i])
            self.item.append(item)

    def write_save(self, save):
        save['player_level'] = self.player_level
        save['player_exp'] = self.player_exp
        save['player_exp_max'] = self.player_exp_max
        save['adventure_mode'] = self.adventure_mode
        save['inventory'] = []
        for i in range(self.inventory):
            ID = self.inventory[i].ID
            save['inventory'].append(ID)
        save['deck'] = []
        for i in range(self.deck):
            ID = self.deck[i].ID
            save['deck'].append(ID)
        save['weapon'] = self.weapon.ID
        save['equipment'] = []
        for i in range(self.equipment):
            ID = self.equipment[i].ID
            save['equipment'].append(ID)
        save['item'] = []
        for i in range(self.item):
            ID = self.item[i].ID
            save['item'].append(ID)

class InventoryThing():
    def __init__(self):
        self.ID = 0
        self.name = ''
        self.element = ''
        self.rarity = ''
        self.effect = []
        self.description = []
        self.surface = pygame.surface.Surface([80, 80], pygame.SRCALPHA)

    def set_data(self, d, dd):
        self.name = d['name']
        self.element = d['element']
        self.rarity = d['rarity']
        self.effect = d['effect']
        self.description = dd['description']

class InventoryItem():
    def __init__(self):
        self.ID = 0

class Weapon(InventoryThing):
    def __init__(self):
        super().__init__()

    def set_data(self, ID):
        self.ID = ID
        if ID != 0:
            d = copy.deepcopy(data_weapon[ID])
            dd = copy.deepcopy(data_weapon_d[ID])
            super().set_data(d, dd)
            self.energy = d['energy']

    def render(self, surface, pos):
        self.surface.fill(Color.transparent)
        self.surface.blit(Image.weapon[self.ID], [0, 0])
        surface.blit(self.surface, pos)

class Equipment(InventoryThing):
    def __init__(self):
        super().__init__()

    def set_data(self, ID):
        d = copy.deepcopy(data_equipment[ID])
        dd = copy.deepcopy(data_equipment_d[ID])
        self.ID = ID
        super().set_data(d, dd)

    def render(self, surface, pos):
        self.surface.fill(Color.transparent)
        self.surface.blit(Image.equipment[self.ID], [0, 0])
        surface.blit(self.surface, pos)

class Item(InventoryThing):
    def __init__(self):
        super().__init__()

    def set_data(self, ID):
        d = copy.deepcopy(data_item[ID])
        dd = copy.deepcopy(data_item_d[ID])
        self.ID = ID
        super().set_data(d, dd)

    def render(self, surface, pos):
        self.surface.fill(Color.transparent)
        self.surface.blit(Image.item[self.ID], [0, 0])
        surface.blit(self.surface, pos)