import pygame


class Holdout(object):

    holdout = pygame.image.load('Holdout_02.png')

    def __init__(self, state):
        self.state = state
        self.x = self.state.win_width/2
        self.y = self.state.surface - self.holdout.get_height()
    #   If soldier is facing the west it is negative, else it's positive 
        self.direction = -1

    def update(self):
        self.holdout = pygame.transform.flip(self.holdout, True, False)
        self.direction *= -1

    def draw(self):
        self.state.win.blit(pygame.transform.flip(self.holdout, True, False), (self.x, self.y))
