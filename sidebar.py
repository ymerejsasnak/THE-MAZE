import pygame


SCR_HEIGHT = SIDEBAR_POSITION = 820
SIDEBAR_WIDTH = 400
FADE_WIDTH = 4

BG_COLOR = pygame.Color(200, 200, 200)
FADE = pygame.Color(1, 1, 1)

BOX_COLOR = pygame.Color(150, 150, 150)
FONT_COLOR = BOX_OUTLINE_COLOR = pygame.Color(0, 0, 0)
BOX_WIDTH = SIDEBAR_WIDTH // 4 * 3
BOX_HEIGHT = 40
BOX_SPACING = 120
BOX_OUTLINE_WIDTH = 2
BOX_X_POSITION = SIDEBAR_WIDTH // 8 + SIDEBAR_POSITION

   



class Sidebar:    

    def draw(self, screen, items):
        fuel, paint, magic_paint, pickaxes = items
        # background
        color = BG_COLOR
        for x in range(0, SIDEBAR_WIDTH, FADE_WIDTH):
            pygame.draw.rect(screen, color, (SIDEBAR_POSITION + x, 0, FADE_WIDTH, SCR_HEIGHT))
            color -= FADE
        self.draw_box(screen, BOX_SPACING, text='Lantern Fuel:           ' + str(fuel))
        self.draw_box(screen, BOX_HEIGHT + BOX_SPACING * 2, text='Paint:                        ' + str(paint))
        self.draw_box(screen, BOX_HEIGHT * 2 + BOX_SPACING * 3, text='Magic Paint:             ' + str(magic_paint))
        self.draw_box(screen, BOX_HEIGHT * 3 + BOX_SPACING * 4, text='Pickaxes:                ' + str(pickaxes)) 
            
    
    def draw_box(self, screen, y_pos, text=''):
        pygame.draw.rect(screen, BOX_COLOR, (BOX_X_POSITION, y_pos, BOX_WIDTH, BOX_HEIGHT))
        pygame.draw.rect(screen, BOX_OUTLINE_COLOR, (BOX_X_POSITION, y_pos, BOX_WIDTH, BOX_HEIGHT), BOX_OUTLINE_WIDTH)
        
        font = pygame.font.Font(None, 35)
        rendered = font.render(text, 1, FONT_COLOR)
        screen.blit(rendered, (BOX_X_POSITION + 15, y_pos + 10))


        
        
