from circleshape import CircleShape
import pygame
import random
from constants import *


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, 2)

    def update(self, dt):
        self.position+=self.velocity*dt

    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return None
        angle=random.uniform(20, 50)
        
        asteroid_one=Asteroid(self.position[0], self.position[1], self.radius-ASTEROID_MIN_RADIUS)
        asteroid_one.velocity=pygame.Vector2(self.position[0], self.position[1]).rotate(-angle)*0.5


        asteroid_two=Asteroid(self.position[0], self.position[1], self.radius-ASTEROID_MIN_RADIUS)
        asteroid_two.velocity=pygame.Vector2(self.position[0], self.position[1]).rotate(angle)*0.5
