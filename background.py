import pygame
import random
from circleshape import CircleShape
from shot import Shot
from constants import *
from star import Star

class Bg(pygame.sprite.Sprite):
    containers = ()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.makeStars = True

    def spawn(self, radius, position, velocity):
        asteroid = Star(position[0], position[1], radius)
        asteroid.velocity = velocity

    def update(self, dt):
        if self.makeStars:
            self.makeStars = False
            for i in range(30):
                velocity = pygame.Vector2(0, 1) * STAR_SPEED
                position = random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)
                self.spawn(1, position, velocity)