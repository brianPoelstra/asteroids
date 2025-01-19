import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shots import Shot
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt=0
    

    updateables=pygame.sprite.Group()
    drawables=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    shots=pygame.sprite.Group()

    Asteroid.containers=(updateables, drawables, asteroids)
    AsteroidField.containers=(updateables)
    Player.containers = (updateables, drawables)
    Shot.containers = (updateables, drawables, shots)

    player=Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field=AsteroidField()

    while running:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                running = False
        for object in updateables:
            object.update(dt)
        screen.fill("black")
       
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                pygame.quit()
                sys.exit()
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        for object in drawables:
            object.draw(screen)

        pygame.display.flip()

        dt=clock.tick(60)/1000
    
    pygame.quit()

if __name__=="__main__":
    main()
