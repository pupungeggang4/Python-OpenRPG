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

    if game.info_tab_player == 'profile':
        surface.blit(Font.neodgm_32.render('Name', False, Color.black), UI.Info.text_start)
        pygame.draw.rect(surface, Color.black, UI.Info.portrait, 2)
        surface.blit(Font.neodgm_32.render(f'Lv.{player.player_level}', False, Color.black), UI.Info.text_level)
        surface.blit(Font.neodgm_32.render(f'Exp.{player.player_exp}/{player.player_exp_max}', False, Color.black), UI.Info.text_exp)

        pygame.draw.rect(surface, Color.black, UI.Info.description_rect_profile, 2)
        surface.blit(Image.player_profile, UI.Info.portrait)

        surface.blit(Font.neodgm_32.render('Weapon', False, Color.black), UI.Info.text_weapon)
        if player.weapon.ID != 0:
            player.weapon.render(surface, UI.Info.weapon)
        pygame.draw.rect(surface, Color.black, UI.Info.weapon, 2)
        surface.blit(Font.neodgm_32.render('Equipment', False, Color.black), UI.Info.text_equipment)
        for i in range(8):
            rect = [UI.Info.equipment_start[0] + UI.Info.equipment_rect[0] * i, UI.Info.equipment_start[1] + UI.Info.item_rect[1] * i, UI.Info.equipment_rect[2], UI.Info.equipment_rect[3]]
            if i < len(player.equipment):
                player.equipment[i].render(surface, rect)
            if i == game.info_profile_index:
                surface.blit(Image.select_frame_80, rect)
            pygame.draw.rect(surface, Color.black, rect, 2)
        surface.blit(Font.neodgm_32.render('Item', False, Color.black), UI.Info.text_item)
        for i in range(8):
            rect = [UI.Info.item_start[0] + UI.Info.item_rect[0] * i, UI.Info.item_start[1] + UI.Info.item_rect[1] * i, UI.Info.item_rect[2], UI.Info.item_rect[3]]
            if i < len(player.item):
                player.item[i].render(surface, rect)
            if i == game.info_profile_index - 8:
                surface.blit(Image.select_frame_80, rect)
            pygame.draw.rect(surface, Color.black, rect, 2)

        if game.info_profile_index == -1:
            if player.weapon.ID != 0:
                surface.blit(Image.select_frame_80, UI.Info.weapon)
                surface.blit(Font.neodgm_16.render(player.weapon.name, False, Color.black), UI.Info.description_text_name)
                render_text_box(surface, Font.neodgm_16, player.weapon.description, UI.Info.description_text_start, UI.Info.description_text_interval)
        elif game.info_profile_index >= 0 and game.info_profile_index < 8:
            i = game.info_profile_index
            if i < len(player.equipment):
                surface.blit(Font.neodgm_16.render(player.equipment[i].name, False, Color.black), UI.Info.description_text_name)
                render_text_box(surface, Font.neodgm_16, player.equipment[i].description, UI.Info.description_text_start, UI.Info.description_text_interval)
        else:
            i = game.info_profile_index - 8
            if i < len(player.item):
                surface.blit(Font.neodgm_16.render(player.item[i].name, False, Color.black), UI.Info.description_text_name)
                render_text_box(surface, Font.neodgm_16, player.item[i].description, UI.Info.description_text_start, UI.Info.description_text_interval)
            
    elif game.info_tab_player == 'inventory':
        surface.blit(Font.neodgm_32.render('Inventory', False, Color.black), UI.Info.text_start)
        pygame.draw.rect(surface, Color.black, UI.Info.description_rect_inventory, 2)
        for i in range(40):
            row = int(i / 10)
            col = i - row * 10
            rect = [UI.Info.inventory_start[0] + UI.Info.inventory_rect[0] * col, UI.Info.inventory_start[1] + UI.Info.inventory_rect[1] * row, UI.Info.inventory_rect[2], UI.Info.inventory_rect[3]]
            pygame.draw.rect(surface, Color.black, rect, 2)
        surface.blit(Image.button['prev'], UI.Info.button_prev)
        surface.blit(Image.button['next'], UI.Info.button_next)

    elif game.info_tab_player == 'deck':
        surface.blit(Font.neodgm_32.render('Deck', False, Color.black), UI.Info.text_start)
        for i in range(8):
            row = int(i / 4)
            col = i - row * 4
            rect = [UI.Info.deck_start[0] + UI.Info.deck_rect[0] * col, UI.Info.deck_start[1] + UI.Info.deck_rect[1] * row, UI.Info.deck_rect[2], UI.Info.deck_rect[3]]
            pygame.draw.rect(surface, Color.black, rect, 2)
        surface.blit(Image.button['prev'], UI.Info.button_prev)
        surface.blit(Image.button['next'], UI.Info.button_next)
        if player.adventure_mode == False:
            for i in range(8):
                row = int(i / 4)
                col = i - row * 4
                pos_image = [UI.Info.deck_image_start[0] + UI.Info.deck_rect[0] * col, UI.Info.deck_image_start[1] + UI.Info.deck_rect[1] * row]
                surface.blit(Image.deck[i], pos_image)
                pos_text = [UI.Info.deck_text_name[0] + UI.Info.deck_rect[0] * col, UI.Info.deck_text_name[1] + UI.Info.deck_rect[1] * row]
                surface.blit(Font.neodgm_16.render(data_deck[i + 1]['name'], False, Color.black), pos_text)
                pos_start = [UI.Info.deck_text_start[0] + UI.Info.deck_rect[0] * col, UI.Info.deck_text_start[1] + UI.Info.deck_rect[1] * row]
                render_text_box(surface, Font.neodgm_16, data_deck_d[i + 1]['description'], pos_start, UI.Info.deck_text_interval)
        else:
            for i in range(8):
                row = int(i / 4)
                col = i - row * 4
                index = game.info_deck_page * 8 + i
                pos = [UI.Info.deck_start[0] + UI.Info.deck_rect[0] * col, UI.Info.deck_start[1] + UI.Info.deck_rect[1] * row]
                if index < len(player.deck):
                    player.deck[i].render(surface, pos)

    elif game.info_tab_player == 'map':
        surface.blit(Font.neodgm_32.render('Map', False, Color.black), UI.Info.text_start)
        surface.blit(Image.m, UI.Info.map_image)

def render_text_box(surface, font, text_list, start, interval):
    for i in range(len(text_list)):
        pos = [start[0] + interval[0] * i, start[1] + interval[1] * i]
        surface.blit(font.render(text_list[i], False, Color.black), pos)

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