import pygame, sys
from script.module import *
import script.scenetitle as scenetitle
import script.scenegame as scenegame

class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.load_asset()
        self.save = {}
        load_save_data(self)

        self.key_pressed = {
            'up': False, 'left': False, 'down': False, 'right': False
        }

        self.key_binding = {
            'up': pygame.K_w, 'left': pygame.K_a, 'down': pygame.K_s, 'right': pygame.K_d
        }
        self.player = Player()
        self.field = Field()
        self.battle = Battle()
        self.shop = Shop()

        self.scene = 'title'
        self.state = ''
        self.menu = False
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode([1280, 720], pygame.SCALED, vsync = 1)
        pygame.display.set_caption('Ceramic Card RPG')

    def load_asset(self):
        Font.neodgm_16 = pygame.font.Font('font/neodgm.ttf', 16)
        Font.neodgm_32 = pygame.font.Font('font/neodgm.ttf', 32)

    def run(self):
        while True:
            self.clock.tick(self.FPS)
            self.handle_input()
            self.handle_scene()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                button = event.button
                if self.scene == 'title':
                    scenetitle.mouse_up(self, mouse, button)
                elif self.scene == 'game':
                    scenegame.mouse_up(self, mouse, button)

            if event.type == pygame.KEYDOWN:
                key = event.key
                for k in self.key_pressed:
                    if key == self.key_binding[k]:
                        self.key_pressed[k] = True
                if self.scene == 'title':
                    scenetitle.key_down(self, key)
                elif self.scene == 'game':
                    scenegame.key_down(self, key)

            if event.type == pygame.KEYUP:
                key = event.key
                for k in self.key_pressed:
                    if key == self.key_binding[k]:
                        self.key_pressed[k] = False
                if self.scene == 'title':
                    scenetitle.key_up(self, key)
                elif self.scene == 'game':
                    scenegame.key_up(self, key)

    def handle_scene(self):
        if self.scene == 'title':
            scenetitle.loop(self)
        elif self.scene == 'game':
            scenegame.loop(self)

Game().run()
