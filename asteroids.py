import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radious, image):
        super().__init__(x, y, radious)
        self.image = image
        self.priority = 4

    def update(self, dt):
        self.position += self.velocity * dt
        
    def draw(self, screen):
        #for centering blit positopn
        top_left_position = (self.position[0] - self.image.get_width() // 2, self.position[1] - self.image.get_height() // 2)
        #blit
        screen.blit(self.image, top_left_position)
        #pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        newAngle = random.uniform(20, 50)
        velo1 = self.velocity.rotate(newAngle)
        velo2 = self.velocity.rotate(-newAngle)
        
        if newRadius == 60:
            self.image = pygame.image.load('sprites/asteroid_60.png').convert_alpha()
        if newRadius == 40:
            self.image = pygame.image.load('sprites/asteroid_90.png').convert_alpha()
        if newRadius == 20:
            self.image = pygame.image.load('sprites/asteroid_60.png').convert_alpha()
        lil1 = Asteroid(self.position.x, self.position.y, newRadius, self.image)
        lil1.velocity = velo1 * 1.2
        lil2 = Asteroid(self.position.x, self.position.y, newRadius, self.image)
        lil2.velocity = velo2 * 1.2