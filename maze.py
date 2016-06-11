import random as r
import pygame
import sys



GRID_SIZE = {'easy': 31, 'normal': 101, 'hard': 301}
CELL_SIZE = 20
MAZE_SIZE = 820

CENTER = MAZE_SIZE // 2 // CELL_SIZE

VIEW_RANGE = 40 # (20 cells to left and right of center)

PLAYER_DRAW_POSITION = (CENTER * CELL_SIZE + CELL_SIZE // 2, CENTER * CELL_SIZE + CELL_SIZE // 2)
PLAYER_RADIUS = CELL_SIZE // 2
PLAYER_COLOR = (100, 200, 0)

WALL_COLOR = pygame.Color(100, 50, 0)
FLOOR_COLOR = pygame.Color(230, 230, 230)
START_COLOR = pygame.Color(100, 200, 100)
FINISH_COLOR = pygame.Color(200, 100, 100)
SHADOW_COLOR = pygame.Color(30, 30, 30)


START_POSITION = (1, 1) #temp
FINISH_POSITION = (1, 1) #temp

START_SIGHT_RANGE = 1  # see clearly for 1 space, fade out after that
MAX_SIGHT_RANGE = 10   # not sure if this is a good max value or not

WALL = '#'
HALL = '.'
START = 'S'
FINISH = 'F'


# --------------------------


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    

# ----------------------------
    
class Maze:
    
    def __init__(self, difficulty):
        self.cells = {}
        self.player_position = START_POSITION
        self.sight_range = START_SIGHT_RANGE
        #self.finish_position = 
        
        
        self.grid_size = GRID_SIZE[difficulty]
        maze_size = self.grid_size // 2
        
        sys.setrecursionlimit(maze_size ** 2)
        
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
         
        
        s = ""
        for (a, b) in zip(even_rows, odd_rows):
            s += ''.join(a + ['\n'] + b + ['\n'])
        maze = s.split('\n')
            
        
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                if x < len(maze[y]) and y < len(maze):
                    self.cells[(x, y)] = maze[y][x]
                    

    def draw(self, screen):
        for x in range(-VIEW_RANGE // 2, VIEW_RANGE // 2 + 1):
            for y in range(-VIEW_RANGE // 2, VIEW_RANGE // 2 + 1):
                                
                color = WALL_COLOR
                    
                draw_pos = (CENTER + x, CENTER + y)
                # using mod to fake a toroidal look (so never know when on edge)
                maze_pos = ((self.player_position[0] + x) % (self.grid_size - 1) , (self.player_position[1] + y) % (self.grid_size - 1)) 
                
                contents = self.cells.get(maze_pos, WALL)
                
                if contents == WALL:
                    color = WALL_COLOR
                else:
                    color = FLOOR_COLOR  
                    
                # calculate and apply shadows
                fadeout = int(distance(draw_pos[0], draw_pos[1], CENTER, CENTER) - self.sight_range)
                for i in range(fadeout):
                    color -= SHADOW_COLOR # cuz subtracting multiply of color object didn't work??
                        
                size = CELL_SIZE
                pygame.draw.rect(screen, color, (draw_pos[0] * size, draw_pos[1] * size, size, size))
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

