
import pygame, sys
from pygame.locals import *
pygame.init()
reloj = pygame.time.Clock()


#iniciar juego
pygame.init()
pygame.display.set_caption("Proyecto final grupo 5")
w=1280
h=720
screen=pygame.display.set_mode((w, h))
#cargar imagenes
#imagenes menú
fondomenu = pygame.transform.scale(pygame.image.load(("images/fondomenu.jpg")),(1280,720)).convert()
#imagenes display juego
fondo = pygame.image.load("images/fondo.png")
roca = pygame.image.load("images/roca.png")
cañon = pygame.transform.scale(pygame.image.load(("images/cañon.png")),(250,150))
#variables
vida=100


#función para agregar texto dentro
def escribir(texto,fuente,color,pantalla,x,y):
    textobj = fuente.render(texto, 1,color)
    textrect = textobj.get_rect()
    textrect.topleft =(x,y)
    pantalla.blit(textobj,textrect)
#fuentes
f1=pygame.font.SysFont(None,100)
f2=pygame.font.SysFont(None,70)
f3=pygame.font.SysFont(None,40)
#función menú
def menu():
    x= 0
    while 1:
        mx ,my = pygame.mouse.get_pos()


        #fondo en mov     
        x_r = x%fondomenu.get_rect().width
        screen.blit(fondomenu,(x_r- fondomenu.get_rect().width,0))
        x-=0.5
        if x_r<w:
            screen.blit(fondomenu,(x_r,0))

        #botones
        bot1 = pygame.Rect(515,300,250,100)
        bot2 = pygame.Rect(515,500,250,100)
        bot1b = pygame.Rect(511,296,258,108)
        bot2b = pygame.Rect(511,496,258,108)
        pygame.draw.rect(screen, (0,0,0),bot1b,border_radius=50)
        pygame.draw.rect(screen, (0,0,0),bot2b,border_radius=50)
        pygame.draw.rect(screen, (90,207,66),bot1,border_radius=50)
        pygame.draw.rect(screen, (90,207,66),bot2,border_radius=50)
        escribir("Jugar", f2, (255, 255 , 255), screen, 572, 323)
        escribir("Dificultad", f2, (255, 255 , 255), screen, 530, 523)
        recuadrob= pygame.Rect(396,91,508,88)
        recuadro= pygame.Rect(400,95,500,80)
        pygame.draw.rect(screen, (0,0,0),recuadrob)
        pygame.draw.rect(screen, (201,190,69),recuadro)
        escribir("Menú principal", f1, (255, 255 , 255), screen, 400, 100)
        
        #codigo botones
        if bot1.collidepoint((mx,my)):
            if event.type == MOUSEBUTTONDOWN:
             game()
        if bot2.collidepoint((mx,my)):
            if event.type == MOUSEBUTTONDOWN:
             dificultad()   
   



        for event in pygame.event.get():   
            if event.type==pygame.QUIT:            
                pygame.quit() 
                exit(0) 
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()


        pygame.display.update()
        reloj.tick(60)


                    


#función juego
def game():
    
    running=True
    while running: 
        #variables
        tvida=str(vida)
        #escenario        
        screen.blit(fondo,(0,0))
        screen.blit(roca,(-200,450))
        screen.blit(cañon,(0,500))
        pygame.draw.rect(screen, (0,0,0), pygame.Rect((1,2),(510,33)),border_radius=10)
        pygame.draw.rect(screen, (255,0,0), pygame.Rect((6,7),(500,23)),border_radius=10)
        pygame.draw.rect(screen, (0,255,0), pygame.Rect((6,7),(vida*5,23)),border_radius=10)
        escribir(tvida,f3, (255, 255 , 255), screen, 235, 7)
        

        #controles
        for event in pygame.event.get():         
            if event.type==pygame.QUIT:            
                pygame.quit() 
                exit(0) 
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running=False
        reloj.tick(60)
        pygame.display.update()

#funcion de dificultades
def dificultad():
    running=True
    while running:  
    
        screen.fill((0,0,0))        
        for event in pygame.event.get():         
            if event.type==pygame.QUIT:            
                pygame.quit() 
                exit(0) 
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running=False
        reloj.tick(60)
        pygame.display.update()
menu()