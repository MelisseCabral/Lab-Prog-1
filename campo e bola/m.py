# -*- coding: latin-1 -*-
bola = 'bola.gif'
campo = 'campo.jpg'

import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1024,768),0,0)

background = pygame.image.load(back).convert()
mouse_c=pygame.image.load(bola).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    screen.blit(background, (0,0))
    
    x,y = pygame.mouse.get_pos()
    x -= mouse_c.get_width()/2
    y -= mouse_c.get_height()/2
    
    screen.blit(mouse_c, (x,y))
    
    pygame.display.update()
