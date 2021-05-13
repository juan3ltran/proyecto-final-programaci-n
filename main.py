
import pygame
from pygame.locals import *

#iniciar juego
pygame.init()
width, height = 1280, 800
screen=pygame.display.set_mode((width, height))

#cargar imagenes
fondo = pygame.image.load("images/fondo.jpg")


while 1:  
    screen.blit(fondo,(0,0))
    pygame.display.flip()
    for event in pygame.event.get():         
        if event.type==pygame.QUIT:            
            pygame.quit() 
            exit(0) 