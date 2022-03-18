import pygame
pygame.init()


class Bullet(object):

    gunshot_sound = pygame.mixer.Sound('M1_Garand.wav')

    def __init__(self, state, x, y, direction):
        self.bullet = pygame.image.load('Bullet.png')
        self.x = x
        self.y = y
        self.vel = direction*30
        self.state = state
        self.gunshot_sound.play()

    def update(self):
        if not self.state.game_over:
            if self.x < 0:
                self.state.bullets.remove(self)
            self.move(self.vel, 0)

    def draw(self):
        self.state.win.blit(self.bullet, (self.x, self.y))

    def move(self, x, y):
        self.x += x
        self.y += y
