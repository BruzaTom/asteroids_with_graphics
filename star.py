import pygame
import random
from circleshape import CircleShape
from constants import *


class Star(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.priority = 50

    def update(self, dt):
        self.position += self.velocity * dt
        if self.position.y > SCREEN_HEIGHT:
            self.kill()
            velocity = pygame.Vector2(0, 1) * STAR_SPEED
            position = random.randint(0, SCREEN_WIDTH), 0
            self.spawn(1, position, velocity)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def spawn(self, radius, position, velocity):
        asteroid = Star(position[0], position[1], radius)
        asteroid.velocity = velocity

        