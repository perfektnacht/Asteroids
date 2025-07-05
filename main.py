# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

# importing variables from the constants.py, player.py, and circleshape.py
from constants import *
from player import *
from circleshape import * 
from asteroid import *
from asteroidfield import *
from shot import *

# main function
def main():
    
    #initialize pygame here
    pygame.init()

    #starting messages that print to console
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #set up the screen resolution
    screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    
# GAME VARIABLES
    #game_running sets up the condition for the infinite game loop
    game_running = True
    #setting up 60 FPS
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    shots = []

    #create two groups (updatable & drawable)
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    
    #create a third group for asteroids
    asteroid_group = pygame.sprite.Group()

    #create a fourth group for asteroids
    shots_group = pygame.sprite.Group()

    #set both groups above as containers for the Player
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (shots_group, updatable_group, drawable_group)

    player = Player (x,y)
    asteroidfield = AsteroidField()
    shots = []

    #infinite game loop
    while game_running:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return

        pygame.Surface.fill(screen,(0,0,0))
        
        #Sets up the player rotation
        for update in updatable_group:
            if isinstance(update, Player):
                update.update(dt, shots)
            else:
                update.update(dt)

        for asteroid in asteroid_group:
            if asteroid.collision(player) == True:
                print("Game Over!")
                pygame.quit()
                sys.exit()
            else:
                pass
        for shot in shots:
            shot.update(dt)
            shot.draw(screen)

        #Draw a player before flipping the screen
        for draw in drawable_group:
            draw.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        dt = (clock.get_time() / 1000)

if __name__ == "__main__":
    main()
