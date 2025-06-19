import pygame, sys
from script.module import *

def loop(game):
    if game.menu == False:
        if game.state == '':
            game.field.handle_tick(game)

    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.field.render(game.surface)
    pygame.draw.rect(game.surface, Color.black, UI.Game.button_menu, 2)
    pygame.draw.rect(game.surface, Color.black, UI.Game.button_info, 2)

    if game.state == 'info':
        render_info(game.surface, game, game.player)

    if game.menu == True:
        render_menu(game.surface, game)

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
                game.player.write_save(game.save)
                game.field.write_save(game.save)
                write_save_data(game)

def key_down(game, key):
    if game.menu == False:
        if game.state == '':
            if key == pygame.K_r:
                game.state = 'info'

        elif game.state == 'info':
            if key == pygame.K_r:
                game.state = ''

def key_up(game, key):
    pass
