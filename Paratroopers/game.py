from paratrooper import Paratrooper
from bullet import Bullet
from mechanics import Mechanics
from state import State
import pygame
pygame.init()

pygame.display.set_caption('Midway')
clock = pygame.time.Clock()
state = State()
mechanics = Mechanics()


def redraw_game():
    state.win.fill((0,0,0))
    state.field.draw()
    state.holdout.draw()
    for paratrooper in state.paratroopers:
        paratrooper.draw()
    for bullet in state.bullets:
        bullet.draw()

    mechanics.draw(state)
    pygame.display.update()


while True:
    clock.tick(24)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state.bullets.append(Bullet(state, state.holdout.x, state.holdout.y + (state.holdout.holdout.get_height())/4, state.holdout.direction))
            
            if event.key == pygame.K_LEFT and state.holdout.direction>0:
                state.holdout.update()

            if event.key == pygame.K_RIGHT and state.holdout.direction<0:
                state.holdout.update()

    if not state.game_over:
        if pygame.time.get_ticks()%51 == 50:
            state.paratroopers.append(Paratrooper(state))

    mechanics.update(state)
    redraw_game()
