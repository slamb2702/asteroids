# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *


def main():

    pygame.init()
<<<<<<< HEAD

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
=======
    screen  = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock   = pygame.time.clock()
    dt      = 0
>>>>>>> 16254e4 (second initial commit)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
<<<<<<< HEAD
        pygame.Surface.fill(screen,(0,0,0))
        pygame.display.flip()

=======
        screen.fill(screen,(0,0,0))
        pygame.display.flip()

        #limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

>>>>>>> 16254e4 (second initial commit)

if __name__ == "__main__":
    main()
