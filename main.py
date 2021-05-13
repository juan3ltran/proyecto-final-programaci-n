
import pygame
from pygame.locals import *

#iniciar juego
pygame.init()
width, height = 1280, 720
screen=pygame.display.set_mode((width, height))
#cargar imagenes
fondo = pygame.image.load("images/fondo.png")
roca = pygame.image.load("images/roca.png")
cañon = pygame.transform.scale(pygame.image.load(("images/cañon.png")),(250,150))
#variables
vida=70

while 1:  
    screen.blit(fondo,(0,0))
    screen.blit(roca,(-200,450))
    screen.blit(cañon,(0,500))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect((1,2),(510,33)),border_radius=10)
    pygame.draw.rect(screen, (255,0,0), pygame.Rect((6,7),(500,23)),border_radius=10)
    pygame.draw.rect(screen, (0,255,0), pygame.Rect((6,7),(vida*5,23)),border_radius=10)
    
    pygame.display.flip()
    for event in pygame.event.get():         
        if event.type==pygame.QUIT:            
            pygame.quit() 
            exit(0) 