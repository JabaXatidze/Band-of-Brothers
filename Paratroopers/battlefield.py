import pygame


class Battlefield(object):

    trench = pygame.image.load('Trench_01.png')

    def __init__(self, state):
        self.state = state
        self.x = self.state.win_width - (self.state.win_width/1.9)
        self.y = self.state.surface - (self.trench.get_height()/3)

    def draw(self):
        self.state.win.blit(self.trench, (self.x, self.y))


