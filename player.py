import pygame
import math
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    containers = ()
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shotTimer = 0
        self.frameTimer = 0
        self.frame = 0
        self.dead = False
        self.priority = 2
        self.original_image = pygame.image.load('sprites/space_jet.png').convert_alpha()
        self.image = self.original_image
        self.explo_frames = []
        for i in range(0, 81):
            self.explo_frames.append(pygame.image.load(f'sprites/explo_frames/{i}.png').convert_alpha())

    def explo(self):
        if self.frameTimer < 0:
            self.frameTimer = 0.1
            self.image = self.explo_frames[self.frame]
            self.frame += 3
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        #for centering blit positopn
        top_left_position = (self.position[0] - self.image.get_width() // 2, self.position[1] - self.image.get_height() // 2)
        #blit
        rotated_image = pygame.transform.rotate(self.image, -self.rotation)
        new_rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, new_rect.topleft)
        #pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shotTimer -= dt
        if (self.dead):
            if (self.frame < len(self.explo_frames)):
                self.frameTimer -= dt
                self.explo()
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.rotate(-dt)
            if keys[pygame.K_d]:
                self.rotate(dt)
            if keys[pygame.K_w]:
                self.move(dt)
            if keys[pygame.K_s]:
                self.move(-dt)
            if keys[pygame.K_SPACE]:
                if self.shotTimer < 0:
                    self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        self.shotTimer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, self.rotation)
        shot.velocity = (pygame.Vector2(0,1).rotate(self.rotation)) * PLAYER_SHOOT_SPEED
