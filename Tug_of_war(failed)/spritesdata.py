import pygame as pg
from pygame import surface

from os import path

import os

from newsettings import WIDTH, HEIGHT, BLACK, YELLOW, WHITE, RED

size = (WIDTH, HEIGHT)

screen = pg.display.set_mode(size)

pg.display.init()

game_folder = os.path.dirname(__file__)

resources_folder = os.path.join(game_folder, 'resources')

stickmanplayer_img = pg.image.load(os.path.join(resources_folder, 'stickmanplayer.jpg')).convert()

stickmanai_img = pg.image.load(os.path.join(resources_folder, 'stickmanplayer.jpg')).convert()

#https://www.shutterstock.com/image-vector/stick-figure-pulling-rope-coiled-1140317804?src=c7Vbr97B4rIRsJ9OYUVcLw-1-0

string = pg.sprite.Group()

all_sprites = pg.sprite.Group()

stickman_ai = pg.sprite.Group()

stickman_player = pg.sprite.Group()

AI_wins = 0

Player_wins = 0

class Player(pg.sprite.Sprite):

    def __init__(self, game, x, y):

        self.groups = game.all_sprites

        pg.sprite.Sprite.__init__(self, self.groups)

        self.game = game

        self.image = stickmanplayer_img

        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y

        self.dx = 1

    def move_left(self,lol):

        if self.rect.left > 10 and lol.rect.x > 310:

            self.rect.x -= 30

            lol.rect.x -= 30

        else:

            self.rect.left = 10



    def update(self):

        if self.rect.right < 770:

            self.rect.x += self.dx

class AI(pg.sprite.Sprite):

    def __init__(self, game, x, y):

        self.groups = game.all_sprites

        pg.sprite.Sprite.__init__(self, self.groups)

        self.game = game

        self.image = stickmanai_img

        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y

        self.dx = 1

    def update(self):

        if self.rect.right < 1000:

            self.rect.x += self.dx



class String(pg.sprite.Sprite):

    def __init__(self, game, x, y, height = 10, width = 320):

        self.game = game

        self.groups = game.all_sprites

        pg.sprite.Sprite.__init__(self, self.groups)

        self.height = height

        self.width = width

        self.surface = surface.Surface((2 * self.width,2 * self.height))

        self.surface.fill(YELLOW)

        self.surface.set_colorkey(YELLOW)

        pg.draw.line(self.surface, BLACK, [0,0], [self.width,0], self.height)

        self.image = self.surface

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y

        self.dx = 1

    def move_to_player(self):

        if self.rect.left > 100:

            self.rect.x -= 30

        else:

            self.rect.left = 100

    def update(self):

        if self.rect.right < 1300:

            self.rect.x += self.dx

    def check_win(self,lol):

        global Player_wins

        global AI_wins

        if self.rect.right < lol.rect.x:

            Player_wins += 1

            print("player wins")

        if self.rect.left > lol.rect.x:

            AI_wins += 1

            print("ai wins")

class Middle_Line(pg.sprite.Sprite):

    def __init__(self, game, x):

        self.game = game

        self.groups = game.all_sprites

        pg.sprite.Sprite.__init__(self, self.groups)

        self.width = WIDTH + 100

        self.height = HEIGHT

        self.surface = surface.Surface((2 * self.width, 2 * self.height))

        self.surface.fill(WHITE)

        self.surface.set_colorkey(WHITE)

        pg.draw.line(self.surface, RED, [200, 0], [200, self.height], 5)

        self.image = self.surface

        self.rect = self.image.get_rect()

        self.rect.x = x

