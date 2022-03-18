import pygame
from holdout import Holdout
from battlefield import Battlefield


class State(object):

    def __init__(self):
        self.win_width = 1300
        self.win_height = 650
        self.surface = self.win_height - 50
        self.win = pygame.display.set_mode((self.win_width, self.win_height))
        self.paratroopers = []
        self.bullets = []
        self.holdout = Holdout(self)
        self.field = Battlefield(self)
        self.game_over = False
