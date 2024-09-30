import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroid_field import AsteroidField
from shot import Shot
from logic import Logic
from background import Bg
from star import Star

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    clock = pygame.time.Clock()
    dt = 0
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    #groups
    updatableGroup = pygame.sprite.Group()
    drawableGroup = pygame.sprite.Group()
    asteroidsGroup = pygame.sprite.Group()
    shotsGroup = pygame.sprite.Group()
    #fill class containers
    Asteroid.containers = (asteroidsGroup, updatableGroup, drawableGroup)
    AsteroidField.containers = (updatableGroup)
    Shot.containers = (shotsGroup)
    Player.containers = (updatableGroup, drawableGroup)
    Logic.containers = (updatableGroup, drawableGroup)
    Bg.containers = (updatableGroup)
    Star.containers = (updatableGroup, drawableGroup)
    #create objects
    field = AsteroidField()
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    gamelogic = Logic()
    background = Bg()
    while(True):
        if gamelogic.restart == True:
            return restart(gamelogic)
        screen.fill('Black')        
        for item in updatableGroup:
            item.update(dt)
        for item in sorted(drawableGroup, key = lambda object: object.priority, reverse = True):
            item.draw(screen)
        for item in asteroidsGroup:
            for shot in shotsGroup:
                if shot.collisions(item):
                    shot.kill()
                    item.split()
                    gamelogic.score += 10
            if item.collisions(ship):
                print('Game over!')
                ship.dead = True
                gamelogic.gameover = True
        for item in shotsGroup:
            item.draw(screen)
            item.update(dt)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        pygame.display.flip()#dont ever forget

def restart(gamelogic):
    gamelogic.restart = False
    main()
    

if __name__ == "__main__":
    main()