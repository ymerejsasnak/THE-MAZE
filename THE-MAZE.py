import pygame
import maze as m


# constants for screen size and areas of screen
SIDEBAR_WIDTH = 300
SCR_HEIGHT = MAZE_SIZE = 820
SCR_WIDTH = SIDEBAR_WIDTH + MAZE_SIZE

NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)

# temp -
difficulty = 'easy'


def run_game():
    
    pygame.init()
    screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    pygame.display.set_caption('THE MAZE')
    
    running = True
    
    
    maze = m.Maze(difficulty)
    maze.draw(screen)
    
    
    # Start the main loop for the game.
    while running:
    
    
    
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            maze.move(NORTH)
            maze.draw(screen)
        elif keys[pygame.K_DOWN]:
            maze.move(SOUTH)
            maze.draw(screen)
        elif keys[pygame.K_LEFT]:
            maze.move(WEST)
            maze.draw(screen)
        elif keys[pygame.K_RIGHT]:
            maze.move(EAST)
            maze.draw(screen)
        elif keys[pygame.K_ESCAPE]:
            running = False
        
        # Make the most recently drawn screen visible (change this to only draw on maze itself or sidebar when nec)
        pygame.display.flip()


run_game()
