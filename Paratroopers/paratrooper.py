import random
import pygame


class Paratrooper(object):
    paratrooper_dropping = [pygame.image.load('Paratrooper_01.png'), pygame.image.load('Paratrooper_02.png')]
    paratrooper_landing = [pygame.image.load('Paradrop_01.png'), pygame.image.load('Paradrop_02.png'),
                           pygame.image.load('Paradrop_03.png')]
    paratrooper_running = [pygame.image.load('Running_01.png'), pygame.image.load('Running_02.png'), pygame.image.load('Running_03.png')]
    paratrooper_firing = []
    paratrooper_dying = [pygame.image.load('Dying_01.png')]

    def __init__(self, state):
        self.variant = random.choice(self.paratrooper_dropping)
        self.distance = random.randrange(state.win_width//15, (state.win_width-self.variant.get_width())//2)
        self.direction = 1 if random.random() < 0.5 else -1
        self.x = (state.win_width/2)-self.direction*(self.distance)
        self.y = 0
        self.vel_x = self.direction*14
        self.vel_y = 5
        self.count = -1
        self.alive = True
        self.state = state

    def update(self):
        if not self.state.game_over:
            if self.alive:
                if self.y < self.state.surface-self.get_height():
                    self.move(0, self.vel_y)
                else:
                    self.land()
                if self.count >= 3 * 4:
                    self.attack()
            else:
                self.die()

    def draw(self):
        self.state.win.blit(self.variant, (self.x, self.y))

    def move(self, x, y):
        self.x += x
        self.y += y

    def get_width(self):
        return self.variant.get_width()

    def get_height(self):
        return self.variant.get_height()

    def land(self):
        self.count += 1
        x = 4
        if self.count < 3 * x:
            self.variant = self.paratrooper_landing[self.count // x]
            if self.count // x == 0:
                self.y = self.state.surface-self.get_height()
            if self.count // x == 1:
                self.y = self.state.surface-self.get_height()
            if self.count // x == 2:
                self.y = self.state.surface-self.get_height()

    def attack(self):
        self.count += 1
        self.variant = self.paratrooper_running[self.count%3]
        if self.direction<0:
            self.variant = pygame.transform.flip(self.variant, True, False)
        self.y = self.state.surface - self.get_height()
        self.move(self.vel_x, 0)

    def killed(self):
        self.alive = False

    def die(self):
        self.variant = self.paratrooper_dying[0]
        self.y = self.state.surface - self.get_height()