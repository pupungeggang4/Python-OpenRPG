import pygame, copy
from script.module import *

class PlayerField():
    def __init__(self):
        self.rect = Rect2(0, 0, 80, 80)
        self.surface = pygame.surface.Surface([self.rect.size.x, self.rect.size.y], pygame.SRCALPHA)

    def handle_tick(self, game, field):
        self.move(game)
        self.check_village(game)

    def move(self, game):
        if game.key_pressed['up'] == True:
            self.rect.position.y -= 200.0 / game.FPS
        if game.key_pressed['left'] == True:
            self.rect.position.x -= 200.0 / game.FPS
        if game.key_pressed['down'] == True:
            self.rect.position.y += 200.0 / game.FPS
        if game.key_pressed['right'] == True:
            self.rect.position.x += 200.0 / game.FPS

    def check_village(self, game):
        v = False
        player = game.player
        for i in range(len(village_zone)):
            if self.rect.inside_rect(village_zone[i]):
                v = True
                break

        if v == False and player.adventure_mode == False:
            player.start_adventure(game)

        elif v == True and player.adventure_mode == True:
            player.end_adventure(game)

    def render(self, surface, camera):
        self.surface.fill(Color.transparent)
        self.surface.blit(Image.player, [0, 0])
        render_surface_camera(surface, self.surface, self.rect, camera)

class Field():
    def __init__(self):
        self.place = ''
        self.player = PlayerField()
        self.thing_list = []
        self.monster_list = [FieldMonster()]
        self.monster_list[0].rect.position = Vector2(0, 480)

        self.camera = Rect2(0, 0, 1280, 720)
        self.surface = pygame.surface.Surface([1280, 720])

    def handle_tick(self, game):
        self.player.handle_tick(game, self)
        self.camera.position.x = self.player.rect.position.x
        self.camera.position.y = self.player.rect.position.y

    def load_save(self, save):
        s = copy.deepcopy(save)
        self.player.rect.position.x = s['position'][0]
        self.player.rect.position.y = s['position'][1]

    def write_save(self, save):
        save['position'][0] = self.player.rect.position.x
        save['position'][1] = self.player.rect.position.y

    def render(self, surface):
        self.surface.fill(Color.white)
        for i in range(len(self.monster_list)):
            self.monster_list[i].render(self.surface, self.camera)
        self.player.render(self.surface, self.camera)
        surface.blit(self.surface, [0, 0])

class FieldThing():
    def __init__(self):
        self.type = ''
        self.rect = Rect2(0, 0, 80, 80)
        self.surface = pygame.surface.Surface([self.rect.size.x, self.rect.size.y], pygame.SRCALPHA)

class FieldWall(FieldThing):
    pass

class FieldMonster(FieldThing):
    def __init__(self):
        super().__init__()
        self.type = 'monster'

    def render(self, surface, camera):
        self.surface.fill(Color.transparent)
        self.surface.blit(Image.field['monster'], [0, 0])
        render_surface_camera(surface, self.surface, self.rect, camera)

class FieldEvent(FieldThing):
    pass

class FieldShop(FieldThing):
    pass

class FieldResource(FieldThing):
    pass
