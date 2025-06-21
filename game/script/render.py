import pygame
from script.module import *

def render_surface_camera(surface_target, surface, rect, camera):
    pos = [rect.position.x - rect.size.x / 2 - camera.position.x + camera.size.x / 2, rect.position.y - rect.size.y / 2 - camera.position.y + camera.size.y / 2]
    surface_target.blit(surface, pos)

def render_info(surface, game, player):
    pygame.draw.rect(surface, Color.white, UI.Info.rect)
    pygame.draw.rect(surface, Color.black, UI.Info.rect, 2)
    surface.blit(Image.button['close'], UI.Info.button_close)

    pygame.draw.rect(surface, Color.black, UI.Info.tab_profile, 2)
    surface.blit(Image.icon['profile'], UI.Info.icon_profile)
    pygame.draw.rect(surface, Color.black, UI.Info.tab_inventory, 2)
    surface.blit(Image.icon['inventory'], UI.Info.icon_inventory)
    pygame.draw.rect(surface, Color.black, UI.Info.tab_deck, 2)
    surface.blit(Image.icon['deck'], UI.Info.icon_deck)
    pygame.draw.rect(surface, Color.black, UI.Info.tab_map, 2)
    surface.blit(Image.icon['map'], UI.Info.icon_map)

def render_menu(surface, game):
    pygame.draw.rect(surface, Color.white, UI.Menu.rect)
    pygame.draw.rect(surface, Color.black, UI.Menu.rect, 2)

    surface.blit(Font.neodgm_32.render('Paused', False, Color.black), UI.Menu.text_paused)
    pygame.draw.rect(surface, Color.black, UI.Menu.button_resume, 2)
    surface.blit(Font.neodgm_32.render('Resume [R]', False, Color.black), UI.Menu.text_resume)
    pygame.draw.rect(surface, Color.black, UI.Menu.button_surrender, 2)
    if game.state != 'battle':
        surface.blit(Font.neodgm_32.render('Surrender [S]', False, Color.gray), UI.Menu.text_surrender)
    else:
        surface.blit(Font.neodgm_32.render('Surrender [S]', False, Color.black), UI.Menu.text_surrender)
        pygame.draw.rect(surface, Color.black, UI.Menu.button_exit, 2)
    surface.blit(Font.neodgm_32.render('Exit [E]', False, Color.black), UI.Menu.text_exit)