import pygame
import random as r

class Sounds:

    def __init__(self):
        pygame.mixer.music.load('mainmusicloop.ogg')
        pygame.mixer.music.play(-1)
        
        secondary_music = pygame.mixer.Sound('secondarymusicloop.ogg')
        secondary_music.set_volume(0.5)
        secondary_music.play(-1)
                
        leftfoot1 = pygame.mixer.Sound('leftfoot1.ogg')
        leftfoot2 = pygame.mixer.Sound('leftfoot2.ogg')
        leftfoot3 = pygame.mixer.Sound('leftfoot3.ogg')
        rightfoot1 = pygame.mixer.Sound('rightfoot1.ogg')
        rightfoot2 = pygame.mixer.Sound('rightfoot2.ogg')
        rightfoot3 = pygame.mixer.Sound('rightfoot3.ogg')
     
        self.leftfeet = [leftfoot1, leftfoot2, leftfoot3]
        self.rightfeet = [rightfoot1, rightfoot2, rightfoot3]
        
        for sound in self.leftfeet + self.rightfeet:
            sound.set_volume(0.3)
        
        self.left = True
        self.step_timer = pygame.time.get_ticks()
    
    def play_step(self):
        current = pygame.time.get_ticks()
        if self.left and current - self.step_timer >= 500:
            r.choice(self.leftfeet).play()
            self.left = not self.left
            self.step_timer = current
        elif not self.left and current - self.step_timer >= 500:
            r.choice(self.rightfeet).play()
            self.left = not self.left
            self.step_timer = current
    
