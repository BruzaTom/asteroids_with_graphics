import pygame
import math
from circleshape import CircleShape
from shot import Shot
from constants import *

class Logic(CircleShape):
    containers = ()
    def __init__(self):
        #pygame.sprite.Sprite.__init__(self, self.containers)#init pygame class to use containers
        super().__init__(0,0,0)
        self.gameover = False
        self.priority = 1
        self.score = 0
        self.goi = pygame.image.load('sprites/gameoversprite.png').convert_alpha()
        self.restart = False
        
    def draw(self, screen):
        font = pygame.font.Font(None, 36)  # None uses the default font, 36 is the font size
        gameoverTxt = font.render(f'SCORE: {self.score}', True, (255, 255, 255))  # White color
        screen.blit(gameoverTxt, (50, 50))  # Position at (100, 100)
        if self.gameover:
            screen.blit(self.goi, (screen.get_width() / 2 - self.goi.get_width() / 2, 
                                   screen.get_height() / 2 - self.goi.get_height() / 2))
    def update(self, dt):
        if self.gameover:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                self.restart = True
