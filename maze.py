import random as r
import pygame
import sys
import magic_paint as mp

# grid size is # of cells, must be odd number for maze to look right
GRID_SIZE = {'test': 11, 'easy': 51, 'normal': 203, 'hard': 303}
CELL_SIZE = 20  # pixels (h and w) per each grid cell
MAZE_SIZE = 820  # pixel size (h and w) of maze portion of screen

CENTER = MAZE_SIZE // 2 // CELL_SIZE  # h and w of center grid square (20, 20)

VIEW_RANGE = 40  # (20 cells to left and right of center)

PLAYER_DRAW_POSITION = (CENTER * CELL_SIZE + CELL_SIZE // 2, CENTER * CELL_SIZE + CELL_SIZE // 2)
PLAYER_RADIUS = CELL_SIZE // 2
PLAYER_COLOR = (100, 200, 0)

WALL_COLOR = pygame.Color(100, 50, 0)
OUTER_WALL_COLOR = pygame.Color(50, 25, 0)
FLOOR_COLOR = pygame.Color(200, 200, 150)
FINISH_COLOR = pygame.Color(100, 100, 200)
PAINTED_COLOR = pygame.Color(255, 180, 180)
MAGIC_PATH_COLOR = pygame.Color(200, 255, 230)
SHADOW_COLOR = pygame.Color(30, 30, 30)

PAINTCAN_COLOR = pygame.Color(250, 150, 150)
FUEL_COLOR = pygame.Color(50, 150, 50)
MAGIC_PAINTCAN_COLOR = MAGIC_PATH_COLOR
PICKAXE_COLOR = WALL_COLOR

OUTLINE_COLOR = (0, 0, 0)

ITEM_SIZE = 7

START_SIGHT_RANGE = 1  # see clearly for 1 space, fade out after that
MAX_FUEL_LEVEL = 15

# for use in creation of maze and as keys in cells dictionary
WALL = '#'
HALL = '.'

PAINT = 1
FUEL = 2
MAGIC_PAINT = 3
PICKAXE = 4

FINISH = 5
PAINTED = 6
MAGIC_PATH = 7

OUTER_WALL = 0


# --------------------------


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    

# ----------------------------
    
class Maze:
    
    def __init__(self, difficulty, inventory):
        self.cells = {}
        self.inventory = inventory
        self.sight_range = START_SIGHT_RANGE
                
        self.grid_size = GRID_SIZE[difficulty]
        self.facing = None
        
        self.player_position = (self.grid_size // 2, self.grid_size // 2)
        self.facing = None
        
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
        self.finish_position = (r.choice([1, self.grid_size - 2]), r.choice([1, self.grid_size - 2]))
        self.cells[self.finish_position] = FINISH
        
        # populate maze with items:  (temp numbers fornow)
        for x in range(500):
            x_pos = r.randrange(self.grid_size) 
            y_pos = r.randrange(self.grid_size)
            if (x_pos, y_pos) == self.finish_position or self.cells[(x_pos, y_pos)] == WALL: 
                continue
            self.cells[(x_pos, y_pos)] = r.choice([PAINT, FUEL, MAGIC_PAINT, PICKAXE])

    def draw(self, screen):
        for x in range(-VIEW_RANGE // 2, VIEW_RANGE // 2 + 1):
            for y in range(-VIEW_RANGE // 2, VIEW_RANGE // 2 + 1):
                                
                draw_pos = (CENTER + x, CENTER + y)
                
                # note: removed toroidal drawing of maze
                
                maze_pos = (self.player_position[0] + x, self.player_position[1] + y) 
                contents = self.cells.get(maze_pos, OUTER_WALL)
                if contents == WALL:
                    color = WALL_COLOR
                elif contents == OUTER_WALL:
                    color = OUTER_WALL_COLOR
                elif contents == FINISH:
                    color = FINISH_COLOR
                elif contents == PAINTED:
                    color = PAINTED_COLOR
                elif contents == MAGIC_PATH:
                    color = MAGIC_PATH_COLOR
                else:
                    color = FLOOR_COLOR
                    
                # calculate and apply shadows
                fadeout = int(distance(draw_pos[0], draw_pos[1], CENTER, CENTER) - self.sight_range)
                for i in range(fadeout):
                    color -= SHADOW_COLOR # cuz subtracting multiply of color object didn't work??
                 
                # now draw the cell!
                size = CELL_SIZE  # just so I had to type less
                pygame.draw.rect(screen, color, (draw_pos[0] * size, draw_pos[1] * size, size, size))
        
                item = False
                # draw items same way
                if contents == PAINT:
                    item_color = PAINTCAN_COLOR
                    item = True
                elif contents == FUEL:
                    item_color = FUEL_COLOR   
                    item = True                 
                elif contents == MAGIC_PAINT:
                    item_color = MAGIC_PAINTCAN_COLOR
                    item = True
                elif contents == PICKAXE:
                    item_color = PICKAXE_COLOR
                    item = True
                
                if item:    
                    for i in range(fadeout * 2):
                        item_color -= SHADOW_COLOR
                    pygame.draw.circle(screen, item_color, (draw_pos[0] * size + size // 2, 
                                        draw_pos[1] * size + size // 2), ITEM_SIZE)
                    pygame.draw.circle(screen, OUTLINE_COLOR, (draw_pos[0] * size + size // 2, 
                                        draw_pos[1] * size + size // 2), ITEM_SIZE, 1)
        
        
        # and after map drawn, draw player!
        pygame.draw.circle(screen, PLAYER_COLOR, PLAYER_DRAW_POSITION, PLAYER_RADIUS)
        pygame.draw.circle(screen, OUTLINE_COLOR, PLAYER_DRAW_POSITION, PLAYER_RADIUS, 1)
  
  
    def move(self, direction, sound_obj):
        self.facing = direction # save direction for pickaxe use
        target = (self.player_position[0] + direction[0], self.player_position[1] + direction[1])
        if self.cells[target] != WALL:
            self.player_position = target
            sound_obj.play_step()
        
        if self.cells[target] == FUEL:
            self.cells[target] = HALL
            self.inventory.get_fuel()
            self.sight_range = min(self.sight_range + 1, MAX_FUEL_LEVEL)
        elif self.cells[target] == PAINT:
            self.cells[target] = HALL
            self.inventory.get_paint()
        elif self.cells[target] == MAGIC_PAINT:
            self.cells[target] = HALL
            self.inventory.get_magic_paint()
        elif self.cells[target] == PICKAXE:
            self.cells[target] = HALL
            self.inventory.get_pickaxe()
            
            
    def paint(self):
        contents = self.cells[self.player_position]
        if self.inventory.paint < 1 or contents == PAINTED or contents == FINISH:
            return
        self.inventory.paint -= 1
        self.cells[self.player_position] = PAINTED
    
    
    def magic_paint(self):
        magic = self.inventory.magic_paint
        if magic < 1:
            return
        a_star_result = mp.a_star_search(self, self.player_position, self.finish_position)
        path = mp.reconstruct_path(a_star_result, self.player_position, self.finish_position)
        for cell in path[1:magic + 1]:
            if self.cells[cell] == HALL:
                self.cells[cell] = MAGIC_PATH
                self.inventory.magic_paint -= 1
            else: # exits paint loop if hits an item/finish
                return
    
    def pickaxe(self):
        if self.inventory.pickaxes == 0:
            return
        target = (self.player_position[0] + self.facing[0], self.player_position[1] + self.facing[1])
        if 0 < target[0] < self.grid_size - 1 and 0 < target[1] < self.grid_size - 1 and self.cells[target] == WALL:
            self.cells[target] = HALL
            self.inventory.pickaxes -= 1    
        
        
        
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
        
            
