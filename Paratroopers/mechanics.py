import pygame
pygame.init()


class Mechanics(object):

    def __init__(self):
       self.font = pygame.font.SysFont('comicsans', 32)

    def update(self, state):

        for paratrooper in state.paratroopers:
            for bullet in state.bullets:

                if paratrooper.x < bullet.x < paratrooper.x + paratrooper.get_width() \
                        and paratrooper.y < bullet.y < paratrooper.y + paratrooper.get_height():
                    paratrooper.killed()
                    state.bullets.remove(bullet)

        for bullet in state.bullets:
            bullet.update()

        for paratrooper in state.paratroopers:
            paratrooper.update()

            if paratrooper.direction>0 and paratrooper.x > state.holdout.x or paratrooper.direction<0 and paratrooper.x < state.holdout.x+state.holdout.holdout.get_width():
                state.game_over = True
                pass

    def draw(self, state):
        if state.game_over:
            lost = self.font.render("Game Over, Loser!", True, (24, 233, 145))
            state.win.blit(lost, ((state.win_width - lost.get_width()) / 2, (state.win_height - lost.get_height()) / 2))

