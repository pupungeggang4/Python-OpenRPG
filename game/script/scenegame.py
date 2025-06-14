import pygame, sys
from script.module import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)
    pygame.display.flip()

def mouse_up(game, pos, button):
    pass

def key_down(game, key):
    pass

def key_up(game, key):
    pass
