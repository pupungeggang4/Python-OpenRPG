from script.module import *

class Color():
    transparent = [0, 0, 0, 0]
    black = [0, 0, 0]
    gray = [127, 127, 127]
    white = [255, 255, 255]

class Font():
    neodgm_16 = None
    neodgm_32 = None

class Image():
    button = {
        'menu': pygame.image.load('image/button/buttonmenu.png'),
        'back': pygame.image.load('image/button/buttonback.png'),
        'close': pygame.image.load('image/button/buttonclose.png'),
        'info': pygame.image.load('image/button/buttoninfo.png'),
        'prev': pygame.image.load('image/button/buttonprev.png'),
        'next': pygame.image.load('image/button/buttonnext.png'),
    }

    icon = {
        'profile': pygame.image.load('image/icon/iconprofile.png'),
        'inventory': pygame.image.load('image/icon/iconitem.png'),
        'deck': pygame.image.load('image/icon/iconcard.png'),
        'map': pygame.image.load('image/icon/iconmap.png'),
    }

    deck = [
        pygame.image.load('image/deck/decknormal.png'),
        pygame.image.load('image/deck/deckfire.png'),
        pygame.image.load('image/deck/deckwater.png'),
        pygame.image.load('image/deck/deckwind.png'),
        pygame.image.load('image/deck/deckearth.png'),
        pygame.image.load('image/deck/decklight.png'),
        pygame.image.load('image/deck/deckdark.png'),
        pygame.image.load('image/deck/deckspecial.png')
    ]

    card = {
    }

    weapon = {
    }

    equipment = {
    }

    item = {
    }

    field = {
        'monster': pygame.image.load('image/field/monster.png')
    }

    m = pygame.image.load('image/map.png')
    player = pygame.image.load('image/player.png')
    player_profile = pygame.image.load('image/playerprofile.png')
    select_frame_80 = pygame.image.load('image/selectframe80.png')

    def load_image(self):
        for i in range(1, 3):
            self.card[i] = pygame.image.load(f'image/card/card{str(i).zfill(3)}.png')
        for i in range(1, 2):
            self.weapon[i] = pygame.image.load(f'image/weapon/weapon{str(i).zfill(3)}.png')
        for i in range(1, 2):
            self.equipment[i] = pygame.image.load(f'image/equipment/equipment{str(i).zfill(3)}.png')
        for i in range(1, 2):
            self.item[i] = pygame.image.load(f'image/item/item{str(i).zfill(3)}.png')