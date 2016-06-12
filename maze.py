import random as r
import pygame
import sys


# grid size is # of cells, must be odd number for maze to look right
GRID_SIZE = {'test': 11, 'easy': 31, 'normal': 103, 'hard': 303}
CELL_SIZE = 20  # pixels (h and w) per each grid cell
MAZE_SIZE = 820  # pixel size (h and w) of maze portion of screen

CENTER = MAZE_SIZE // 2 // CELL_SIZE  # h and w of center grid square (20, 20)

VIEW_RANGE = 40  # (20 cells to left and right of center)

PLAYER_DRAW_POSITION = (CENTER * CELL_SIZE + CELL_SIZE // 2, CENTER * CELL_SIZE + CELL_SIZE // 2)
PLAYER_RADIUS = CELL_SIZE // 2
PLAYER_COLOR = (100, 200, 0)

WALL_COLOR = pygame.Color(100, 50, 0)
FLOOR_COLOR = pygame.Color(230, 230, 200)
FINISH_COLOR = pygame.Color(100, 100, 200)
SHADOW_COLOR = pygame.Color(30, 30, 30)

START_SIGHT_RANGE = 1  # see clearly for 1 space, fade out after that
MAX_SIGHT_RANGE = 10   # not sure if this is a good max value or not

# for use in creation of maze and as keys in cells dictionary
WALL = '#'
HALL = '.'

FINISH = 'F'


# --------------------------


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    

# ----------------------------
    
class Maze:
    
    def __init__(self, difficulty):
        self.cells = {}
        self.sight_range = START_SIGHT_RANGE
                
        self.grid_size = GRID_SIZE[difficulty]
        
        self.player_position = (self.grid_size // 2, self.grid_size // 2)
        
        # need a value floor half of grid size because of the way maze is generated
        # (works on two grid cells at a time because of the need of walls between spaces)
        maze_size = self.grid_size // 2 
        
        if maze_size ** 2 > sys.getrecursionlimit():
            sys.setrecursionlimit(maze_size ** 2)
            
        ####
        # generate the maze (needs its own method)
        
        # first initialize lists needed
        # works in squares, first generates all needed walls and spaces,
        # then with 'walk' function, randomly goes around adding connections,
        # keeping track of what has been visited
        # just think of each bit like this:  '##'
        #                                    '#.'
        visited = [[0] * maze_size + [1] for _ in range(maze_size)] + [[1] * (maze_size + 1)]
        even_rows = [[WALL + WALL] * maze_size + [WALL] for _ in range(maze_size + 1)]
        odd_rows = [[WALL + HALL] * maze_size + [WALL] for _ in range(maze_size)] + [[]]
        
        def walk(x, y):
            visited[y][x] = 1
     
            directions = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            r.shuffle(directions)
            
            for (xx, yy) in directions:
                if visited[yy][xx]: 
                    continue
                if xx == x: 
                    even_rows[max(y, yy)][x] = WALL + HALL
                if yy == y: 
                    odd_rows[y][max(x, xx)] = HALL + HALL
                    
                walk(xx, yy)
        
        walk(r.randrange(maze_size), r.randrange(maze_size))
         
        # then combine the even and odd rows
        s = ""
        for (a, b) in zip(even_rows, odd_rows):
            s += ''.join(a + ['\n'] + b + ['\n'])
        
        # and split on newlines to make next bit work
        maze = s.split('\n')
            
        # run through list of strings to read maze into self.cells
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                if x < len(maze[y]) and y < len(maze):
                    self.cells[(x, y)] = maze[y][x]
                    
        # don't forget to add the finish space, place it in one of the 4 corners randomly
        finish_position = (r.choice([1, self.grid_size - 2]), r.choice([1, self.grid_size - 2]))
        self.cells[finish_position] = FINISH

    def draw(self, screen):
        for x in range(-VIEW_RANGE // 2, VIEW_RANGE // 2 + 1):
            for y in range(-VIEW_RANGE // 2, VIEW_RANGE // 2 + 1):
                                
                draw_pos = (CENTER + x, CENTER + y)
                
                # using mod to fake a toroidal look (so player never knows when on edge)
                wrap_maze_pos = ((self.player_position[0] + x) % (self.grid_size - 1), 
                                (self.player_position[1] + y) % (self.grid_size - 1)) 
                wrap_contents = self.cells.get(wrap_maze_pos, WALL)
                
                if wrap_contents == WALL:
                    color = WALL_COLOR
                else:
                    color = FLOOR_COLOR  
                 
                # do again, but non-toroidally, for certain items and finish
                maze_pos = (self.player_position[0] + x, self.player_position[1] + y) 
                contents = self.cells.get(maze_pos)
                if contents == FINISH:
                    color = FINISH_COLOR
                    
                # calculate and apply shadows
                fadeout = int(distance(draw_pos[0], draw_pos[1], CENTER, CENTER) - self.sight_range)
                for i in range(fadeout):
                    color -= SHADOW_COLOR # cuz subtracting multiply of color object didn't work??
                 
                # now draw map!
                size = CELL_SIZE  # just so I had to type less
                pygame.draw.rect(screen, color, (draw_pos[0] * size, draw_pos[1] * size, size, size))
        
        # and after map drawn, draw player!
        pygame.draw.circle(screen, PLAYER_COLOR, PLAYER_DRAW_POSITION, PLAYER_RADIUS)
  
    def move(self, direction):
        target = (self.player_position[0] + direction[0], self.player_position[1] + direction[1])
        if self.cells[target] != WALL:
            self.player_position = target
            
            
            
'''            
    def neighbors(self, current):
        x, y = current
        neighbors = []
        north = (x, y - 1)
        south = (x, y + 1)
        east = (x + 1, y)
        west = (x - 1, y)
        for direction in [north, south, east, west]:
            if self.cells[direction] != WALL:
                neighbors.append(direction)
        
        return neighbors
        


# get total 'manhattan' distance between two points
def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)
'''

