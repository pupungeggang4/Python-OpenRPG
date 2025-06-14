import pygame, sys
from script.module import *
import script.scenetitle as scenetitle
import script.scenegame as scenegame

class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.player = Player()
        self.field = Field()
        self.battle = Field()
        self.shop = Shop()

        self.scene = 'title'
        self.state = ''
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode([1280, 720])
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

    def handle_scene(self):
        if self.scene == 'title':
            scenetitle.loop(self)

        if self.scene == 'game':
            scenegame.loop(self)

Game().run()
