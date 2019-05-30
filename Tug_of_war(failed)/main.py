import pygame as pg

import sys

import random

import math

import time

from os import path

from newsettings import *

from spritesdata import *

clock = pg.time.Clock()

Player_wins = 0

AI_wins = 0

class Game:

    def __init__(self):

        pg.init()

        self.Player_wins = 0

        self.AI_wins = 0

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))

        pg.display.set_caption(TITLE)

        self.clock = pg.time.Clock()

        self.time = pg.time.get_ticks()

        pg.key.set_repeat(500, 100)

        self.all_sprites = pg.sprite.Group()

        self.player = Player(self, 249, 384)

        self.ai = AI(self, 550, 430)

        self.middle_line = Middle_Line(self, 300)

        self.string = String(self, 350, 500)

    def run(self):

        # game loop - set self.playing = False to end the game

        self.playing = True

        while self.playing:

            self.dt = self.clock.tick(FPS) / 1000

            self.events()

            self.update()

            self.draw()

    def quit(self):

        pg.quit()

        sys.exit()



    def update(self):

        self.all_sprites.update()

        self.string.check_win(self.middle_line)

        self.all_sprites.update()

    def draw(self):

        self.screen.fill(BGCOLOR)

        self.all_sprites.draw(self.screen)

        font = pg.font.SysFont('Arial', 30, True, False)

        text = font.render("PLAYER WINS:" + str(Player_wins), True, BLACK)

        screen.blit(text, [50, 50])

        font = pg.font.SysFont('Arial', 30, True, False)

        text = font.render("AI WINS:" + str(AI_wins), True, BLACK)

        screen.blit(text, [790, 50])

        self.all_sprites.update()

        pg.display.flip()

    def events(self):

        # catch all events here

        for event in pg.event.get():

            if event.type == pg.QUIT:

                self.quit()