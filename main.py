
import pygame, sys
from pygame.locals import *
import math
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
#imagens dificultad
fondodif=pygame.transform.scale(pygame.image.load(("images/fondodificultad.jpg")),(1280,720)).convert()
palmera1=pygame.transform.scale(pygame.image.load("images/palmera1.png"),(500,700))
bola=pygame.transform.scale(pygame.image.load("images/bola.png"),(150,150))
#imagenes display juego
fondo = pygame.image.load("images/fondo.png")
roca = pygame.image.load("images/roca.png")
cañon = pygame.transform.scale(pygame.image.load(("images/base cañon.png")),(250,150))
cañon2 = pygame.transform.scale(pygame.image.load(("images/cañon 2.png")),(250,150))
#variables
vida=70
difficult = 2

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
            pygame.draw.rect(screen, (255,255,255),bot1b,border_radius=50)
            pygame.draw.rect(screen, (90,207,66),bot1,border_radius=50)
            escribir("Jugar", f2, (255, 255 , 255), screen, 572, 323)
            if event.type == MOUSEBUTTONDOWN:
             game()
        if bot2.collidepoint((mx,my)):
            pygame.draw.rect(screen, (255,255,255),bot2b,border_radius=50)
            pygame.draw.rect(screen, (90,207,66),bot2,border_radius=50)
            escribir("Dificultad", f2, (255, 255 , 255), screen, 530, 523)
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
        
        mx, my = pygame.mouse.get_pos()
        
        #variables
        tvida=str(vida)
        #escenario        
        screen.blit(fondo,(0,0))
        screen.blit(roca,(-200,450))
        
        
        
        #animación cañon
        if mx!=110:
            alpha =(570-my)/(mx-110)
        angulo =(math.atan(alpha)*180/math.pi)-20
        
       
        anim=pygame.transform.rotate(cañon2,angulo)
        anim_rect=anim.get_rect()
        anim_rect.center=(110,570)
        screen.blit(anim,anim_rect)
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
    global difficult
    running=True
    while running: 
        mx ,my = pygame.mouse.get_pos()


        screen.blit(fondodif,(0,0)) 
        screen.blit(palmera1,(0,0)) 
        screen.blit(bola,(800,500))
        #botones   
        bot1 = pygame.Rect(515,200,250,100)
        bot2 = pygame.Rect(515,400,250,100)
        bot3 = pygame.Rect(515,600,250,100)
        bot1b = pygame.Rect(511,196,258,108)
        bot2b = pygame.Rect(511,396,258,108)
        bot3b = pygame.Rect(511,596,258,108)
        pygame.draw.rect(screen, (0,0,0),bot1b,border_radius=50)
        pygame.draw.rect(screen, (0,0,0),bot2b,border_radius=50)
        pygame.draw.rect(screen, (0,0,0),bot3b,border_radius=50)
        pygame.draw.rect(screen, (178,130,91),bot1,border_radius=50)
        pygame.draw.rect(screen, (178,130,91),bot2,border_radius=50)
        pygame.draw.rect(screen, (178,130,91),bot3,border_radius=50)
        escribir("Fácil", f2, (255, 255 , 255), screen, 583, 223)
        escribir("Normal", f2, (255, 255 , 255), screen, 560, 423)
        escribir("Dificil", f2, (255, 255 , 255), screen, 570, 623)
        recuadrob= pygame.Rect(383,91,526,88)
        recuadro= pygame.Rect(387,95,518,80)
        pygame.draw.rect(screen, (0,0,0),recuadrob)
        pygame.draw.rect(screen, (35,133,32),recuadro)
        escribir("Selecciona una", f1, (255, 255 , 255), screen, 385, 100)       
        
        #cuadro de dificultad seleccionada
        rect1 = pygame.Rect(950,96,250,250)
        rect1b = pygame.Rect(946,92,258,258)
        pygame.draw.rect(screen, (0,0,0),rect1b)
        pygame.draw.rect(screen, (189,189,208),rect1)
        if difficult == 1:
            escribir("Fácil", f2, (255, 255 , 255), screen, 950, 96)
        if difficult == 2:
            escribir("Normal", f2, (255, 255 , 255), screen, 950, 96)
        if difficult == 3:
            escribir("Díficil", f2, (255, 255 , 255), screen, 950, 96)
        

        #código botones
        if bot1.collidepoint((mx,my)):
            pygame.draw.rect(screen, (255,255,255),bot1b,border_radius=50)
            pygame.draw.rect(screen, (178,130,91),bot1,border_radius=50)
            escribir("Fácil", f2, (255, 255 , 255), screen, 583, 223)
            if event.type == MOUSEBUTTONDOWN:
             
             difficult = 1
        if bot2.collidepoint((mx,my)):
            pygame.draw.rect(screen, (255,255,255),bot2b,border_radius=50)
            pygame.draw.rect(screen, (178,130,91),bot2,border_radius=50)
            escribir("Normal", f2, (255, 255 , 255), screen, 560, 423)            
            if event.type == MOUSEBUTTONDOWN:
             
             difficult = 2
        if bot3.collidepoint((mx,my)):
            pygame.draw.rect(screen, (255,255,255),bot3b,border_radius=50)
            pygame.draw.rect(screen, (178,130,91),bot3,border_radius=50) 
            escribir("Dificil", f2, (255, 255 , 255), screen, 570, 623)
            if event.type == MOUSEBUTTONDOWN:
            
             difficult = 3
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

#preguntas sobre fisica:
#1.1. La ciencia física es una ciencia fundamental, esto quiere decir que para explicarla:

#A. No necesita de otras ciencias naturales. (Respuesta correcta)
#B. Necesita y se fundamenta en otras ciencias naturales.
#C. Sus conceptos deben ser particulares y limitados en el tiempo
#D. Ninguna respuesta anterior es correcta.

#2.1 En el diagrama de cuerpo libre:

#A. Se deben tomar en cuenta las fuerzas internas.
#B. No se deben tomar en cuenta las fuerzas internas.
#C. Se deben tomar en cuenta las fuerzas externas e internas.
#D. Ninguna respuesta anterior es correcta. (Respuesta correcta)

#3.1.  Para poder utilizar la ecuación: torque neto igual al momento de inercia del cuerpo
#por la aceleración angular, es necesario y suficiente que:

#A. La masa del cuerpo sea constante.
#B. El momento de inercia del cuerpo no sea constante.
#C. El eje de rotación permanezca fijo. (El eje de rotacion permanezca fijo)
#D. Ninguna respuesta anterior es correcta.

#4.1.La energía potencial gravitatoria de una partícula se incrementa cuando:

#A. Una fuerza externa no realiza trabajo activo.
#B. Una fuerza externa realiza trabajo resistente.
#C. El peso de la partícula realiza trabajo resistente. (Respuesta correcta)
#D. Ninguna respuesta anterior es correcta.