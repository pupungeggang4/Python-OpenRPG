import pygame

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
        'menu': pygame.image.load('image/button/ButtonMenu.png'),
        'back': pygame.image.load('image/button/ButtonBack.png'),
        'close': pygame.image.load('image/button/ButtonClose.png'),
        'info': pygame.image.load('image/button/ButtonInfo.png'),
        'prev': pygame.image.load('image/button/ButtonPrev.png'),
        'next': pygame.image.load('image/button/ButtonNext.png'),
    }

    icon = {
        'profile': pygame.image.load('image/icon/IconProfile.png'),
        'inventory': pygame.image.load('image/icon/IconItem.png'),
        'deck': pygame.image.load('image/icon/IconCard.png'),
        'map': pygame.image.load('image/icon/IconMap.png'),
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

    def load_image(self):
        for i in range(1, 3):
            self.card[i] = pygame.image.load(f'image/card/card{str(i).zfill(3)}.png')
        for i in range(1, 2):
            self.weapon[i] = pygame.image.load(f'image/weapon/weapon{str(i).zfill(3)}.png')
        for i in range(1, 2):
            self.equipment[i] = pygame.image.load(f'image/equipment/equipment{str(i).zfill(3)}.png')
        for i in range(1, 2):
            self.item[i] = pygame.image.load(f'image/item/item{str(i).zfill(3)}.png')