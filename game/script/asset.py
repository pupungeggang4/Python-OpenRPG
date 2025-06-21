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