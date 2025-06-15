import pygame, sys
from script.module import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)
    pygame.draw.rect(game.surface, Color.black, UI.Game.button_menu, 2)

    if game.menu == True:
        render_menu(game, game.surface)
    pygame.display.flip()

def mouse_up(game, pos, button):
    if button == 1:
        if game.menu == False:
            if point_inside_rect_ui(pos, UI.Game.button_menu):
                game.menu = True

        elif game.menu == True:
            if point_inside_rect_ui(pos, UI.Game.button_menu):
                game.menu = False
            elif point_inside_rect_ui(pos, UI.Menu.button_resume):
                game.menu = False
            elif point_inside_rect_ui(pos, UI.Menu.button_exit):
                game.menu = False
                game.scene = 'title'
                game.state = ''

def key_down(game, key):
    pass

def key_up(game, key):
    pass
