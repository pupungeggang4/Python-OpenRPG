from script.module import *

def loop(game):
    if game.menu == False:
        if game.state == '' and game.info == False:
            game.field.handle_tick(game)

    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.field.render(game.surface)
    game.surface.blit(Image.button['menu'], UI.Game.button_menu)
    game.surface.blit(Image.button['info'], UI.Game.button_info)

    if game.info == True:
        render_info(game.surface, game, game.player)

    if game.menu == True:
        render_menu(game.surface, game)

    pygame.display.flip()

def mouse_up(game, pos, button):
    if button == 1:
        if game.menu == False:
            if point_inside_rect_ui(pos, UI.Game.button_menu):
                game.menu = True

            if game.info == False:
                if point_inside_rect_ui(pos, UI.Game.button_info):
                    game.info = True
                    game.info_tab_player = 'profile'
                    game.info_profile_index = -1
                    game.info_deck_page = 0

                if game.state == '':
                    pass

            elif game.info == True:
                if point_inside_rect_ui(pos, UI.Game.button_info) or point_inside_rect_ui(pos, UI.Info.button_close):
                    game.info = False
                if point_inside_rect_ui(pos, UI.Info.tab_profile):
                    game.info_tab_player = 'profile'
                    game.info_profile_index = -1
                elif point_inside_rect_ui(pos, UI.Info.tab_inventory):
                    game.info_tab_player = 'inventory'
                elif point_inside_rect_ui(pos, UI.Info.tab_deck):
                    game.info_tab_player = 'deck'
                    game.info_deck_page = 0
                elif point_inside_rect_ui(pos, UI.Info.tab_map):
                    game.info_tab_player = 'map'

                if game.info_tab_player == 'profile':
                    click_info_profile(game, pos)

        elif game.menu == True:
            if point_inside_rect_ui(pos, UI.Game.button_menu):
                game.menu = False
            elif point_inside_rect_ui(pos, UI.Menu.button_resume):
                game.menu = False
            elif point_inside_rect_ui(pos, UI.Menu.button_exit):
                game.menu = False
                game.scene = 'title'
                game.state = ''
                if game.state == '':
                    game.player.write_save(game.save)
                    game.field.write_save(game.save)
                    write_save_data(game)

def click_info_profile(game, pos):
    if point_inside_rect_ui(pos, UI.Info.weapon):
        game.info_profile_index = -1
    for i in range(8):
        rect = [UI.Info.equipment_start[0] + UI.Info.equipment_rect[0] * i, UI.Info.equipment_start[1] + UI.Info.equipment_rect[1] * i, UI.Info.equipment_rect[2], UI.Info.equipment_rect[3]]
        if point_inside_rect_ui(pos, rect):
            game.info_profile_index = i
    for i in range(8):
        rect = [UI.Info.item_start[0] + UI.Info.item_rect[0] * i, UI.Info.item_start[1] + UI.Info.item_rect[1] * i, UI.Info.item_rect[2], UI.Info.item_rect[3]]
        if point_inside_rect_ui(pos, rect):
            game.info_profile_index = i + 8

def key_down(game, key):
    if game.menu == False:
        if game.info == False:
            if key == pygame.K_r:
                game.info = True
            if game.state == '':
                pass

        elif game.info == True:
            if key == pygame.K_r:
                game.info = False

def key_up(game, key):
    pass
