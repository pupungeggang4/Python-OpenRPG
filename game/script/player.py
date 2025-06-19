class Player():
    def __init__(self):
        self.player_level = 1
        self.player_exp = 0
        self.player_exp_max = 0

    def load_save(self, save):
        self.player_level = save['player_level']
        self.player_exp = save['player_exp']
        self.player_exp_max = save['player_exp_max']

    def write_save(self, save):
        save['player_level'] = self.player_level
        save['player_ext'] = self.player_exp
        save['player_exp_max'] = self.player_exp_max

class InventoryThing():
    pass

class Equipment(InventoryThing):
    pass

class Weapon(InventoryThing):
    pass

class Item(InventoryThing):
    pass
