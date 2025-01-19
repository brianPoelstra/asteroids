import pygame
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y, radius=5):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, 5)


    def update(self, dt):
        self.position+=self.velocity*dt

    
