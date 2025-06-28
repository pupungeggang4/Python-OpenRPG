class UI():
    class Title():
        text_title = [24, 24]
        button_start = [160, 160, 960, 80]
        text_start = [184, 184]
        button_info = [160, 240, 960, 80]
        text_info = [184, 264]
        button_erase = [160, 320, 960, 80]
        text_erase = [184, 344]

    class Game():
        button_menu = [1180, 20, 80, 80]
        button_info = [1180, 620, 80, 80]

    class Battle():
        pass

    class Info():
        rect = [160, 40, 960, 640]
        button_close = [1080, 40, 40, 40]
        tab_profile = [160, 40, 200, 40]
        icon_profile = [240, 40]
        tab_inventory = [360, 40, 200, 40]
        icon_inventory = [440, 40]
        tab_deck = [560, 40, 200, 40]
        icon_deck = [640, 40]
        tab_map = [760, 40, 200, 40]
        icon_map = [840, 40]

        text_start = [164, 84]
        portrait = [200, 120, 160, 160]
        
        text_level = [164, 284]
        text_exp = [164, 324]

        text_weapon = [444, 84]
        weapon = [440, 160, 80, 80]
        description_rect_profile = [760, 160, 320, 80]
        text_equipment = [444, 284]
        equipment_start = [440, 360]
        equipment_rect = [80, 80, 80, 80]
        text_item = [444, 484]
        item_start = [440, 560]
        item_rect = [80, 80, 80, 80]

        button_prev = [180, 340, 40, 40]
        button_next = [1060, 340, 40, 40]
        description_rect_inventory = [240, 160, 800, 80]
        inventory_start = [240, 240]
        inventory_rect = [80, 80, 80, 80]

        deck_start = [240, 120]
        deck_rect = [200, 240, 200, 240]
        deck_image_start = [300, 120]
        deck_text_name = [244, 204]
        deck_text_start = [244, 224]
        deck_text_interval = [0, 18]

    class Shop():
        pass

    class Reward():
        pass

    class Card():
        size = [200, 240]
        image = [20, 20, 160, 120]
        text_energy = [4, 4]
        text_name = [4, 142]
        text_d_start = [4, 162]
        text_d_interval = [0, 18]

    class Menu():
        rect = [320, 200, 640, 320]
        text_paused = [344, 224]
        button_resume = [320, 280, 640, 80]
        text_resume = [344, 304]
        button_surrender = [320, 360, 640, 80]
        text_surrender = [344, 384]
        button_exit = [320, 440, 640, 80]
        text_exit = [344, 464]
