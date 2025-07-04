# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# importing variables from the constants.py file
from constants import * 

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

    #infinite game loop
    while game_running:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return

        pygame.Surface.fill(screen,(0,0,0))
        pygame.display.flip()
        clock.tick(60)
        dt = (clock.get_time() / 1000) 

if __name__ == "__main__":
    main()
