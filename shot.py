import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    containers = ()
    def __init__(self, x, y, radious, angle):
        super().__init__(x, y, radious)
        self.original_image = image = pygame.image.load('sprites/green_lazer.png').convert_alpha()
        self.image = self.original_image
        self.rotation = angle
        self.priority = 3

    def update(self, dt):
        self.position += self.velocity * dt
        
    def draw(self, screen):
        #for centering blit positopn
        self.image = pygame.transform.rotate(self.original_image, -self.rotation)
        top_left_position = (self.position[0] - self.image.get_width() // 2, self.position[1] - self.image.get_height() // 2)
        #blit
        screen.blit(self.image, top_left_position)
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)