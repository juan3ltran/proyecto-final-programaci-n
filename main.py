
import pygame, sys
from pygame import color
from pygame import time
from pygame.draw import circle
from pygame.image import save
from pygame.locals import *
import math, random
from pygame.mixer import pause
from pygame.time import Clock
pygame.init()
reloj = pygame.time.Clock()
Negro= (0,0,0)

#iniciar juego
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Proyecto final grupo 5")
w=1280
h=720
screen=pygame.display.set_mode((w, h))
#cargar imagenes
#imagenes menú
fondomenu = pygame.transform.scale(pygame.image.load(("images/fondomenu.jpg")),(1280,720)).convert()
#imagenes dificultad
fondodif=pygame.transform.scale(pygame.image.load(("images/fondodificultad.jpg")),(1280,720)).convert()
palmera1=pygame.transform.scale(pygame.image.load("images/palmera1.png"),(500,700))
bola=pygame.transform.scale(pygame.image.load("images/bola.png"),(150,150))
#imagenes display juego
fondo = pygame.image.load("images/fondo.png")
roca = pygame.image.load("images/roca.png")
cañon = pygame.transform.scale(pygame.image.load(("images/base cañon.png")),(250,150))
cañon2 = pygame.transform.scale(pygame.image.load(("images/cañon 2.png")),(250,150))
moneda_oro = pygame.transform.scale(pygame.image.load(("images/moneda de oro.png")),(25,25))
escudo222 = pygame.transform.scale(pygame.image.load(("images/escudo.png")),(40,40))
cofre = pygame.transform.scale(pygame.image.load(("images/cofre.png")),(40,40))
#imagenes tienda
fondo_tienda = pygame.transform.scale(pygame.image.load(("images/paredmadera.png")),(700,700))
pocion = pygame.transform.scale(pygame.image.load(("images/Aumento_Glacial_runa.png")),(50,50))
vidaimagen1 = pygame.transform.scale(pygame.image.load(("images/vida.png")),(50,50))
imagendaño = pygame.transform.scale(pygame.image.load(("images/daño.png")),(50,50))
tamañobala = pygame.transform.scale(pygame.image.load(("images/ult.png")),(50,50))
pocion50 = pygame.transform.scale(pygame.image.load(("images/pocion50.png")),(50,50))
fondo_preguntas = pygame.image.load("images/fondo preguntas.jpg")
#imagenes derrota
fondoderr=pygame.transform.scale(pygame.image.load(("images/fondoderrota.jpg")),(1280,720)).convert()
botonr = pygame.transform.scale(pygame.image.load(("images/botr.png")),(100,100))

sound_canon = pygame.mixer.Sound("sound/canon.wav")
sound_explosion = pygame.mixer.Sound("sound/explosion.wav")


#variables
difficult=2
vida=100
oro = 0
puntuación=0
multiplo_de_diez = 10
multiplo_de_diez2 = 13
escudo = 0
fuente = pygame.font.SysFont("Constantia",17)

#clases
class Enemigos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(("images/barco.png")),(120,120)).convert_alpha()
        self.rect= self.image.get_rect()
        self.rect.right= random.randrange(h)
        self.rect.y = random.randint(300,540)
        self.rect.x = 1100
    def update(self):
        self.rect.x -=3
        if self.rect.right < 0:
            self.rect.left = w

class bala(object):
    def __init__(self, x, y, radio, color):
        self.x=x
        self.y=y
        self.radio=radio
        self.color=color
    def draw(self,screen):
        pygame.draw.circle(screen,(200,0,0),(self.x,self.y),self.radio)
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radio-1)

    def balatray(startx, starty, power, ang, tiempo):
        angle = ang
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        distX = velx * tiempo
        distY = (vely *tiempo) + ((-4.9 * (tiempo ** 2)) / 2)

        newx = round(distX + startx)
        newy = round(starty - distY)
        return(newx,newy)

#variables bala
cañonx=110
cañony=570
radiob=12
balatest=bala(cañonx, cañony, radiob, (0,0,0))
bx=0
by=0
tiempob=0
power=0   
angle= 0
tiempo=0
shoot=False


#funcion anglo
def findAngle(pos):
    sX = balatest.x
    sY = balatest.y
    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        angle = math.pi / 2

    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) - angle

    return angle

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

    #grupo sprites
    sprites = pygame.sprite.Group()

    enemigos= Enemigos()
    sprites.add(enemigos)
    enemigos1=Enemigos()
    sprites.add(enemigos1)
    enemigos2=Enemigos()
    sprites.add(enemigos2)

    global balatest
    global bola
    global multiplo_de_diez
    global oro
    global vida
    global puntuación
    global radiob
    global shoot
    global bx
    global by
    global power
    global angle
    global tiempob
    global multiplo_de_diez2
    global tiempo
    

    running=True
    while running: 
        
        tiempo = int((pygame.time.get_ticks())/1000)
        mx, my = pygame.mouse.get_pos()
        
        #contador
        if tiempo == multiplo_de_diez:
            oro = oro + 200
            multiplo_de_diez = multiplo_de_diez + 2
        if difficult==1:
         puntuación=10*tiempo
        if difficult==2:
         puntuación=15*tiempo
        if difficult==3:
         puntuación=20*tiempo
        
    
        #variables
        tvida=str(vida)
        toro=str(oro)
        tpuntuación=str(puntuación)
        tescudo=str(escudo)
        #escenario        
        screen.blit(fondo,(0,0))
        sprites.draw(screen)
        screen.blit(roca,(-200,450))
        screen.blit(moneda_oro,(30,50))
        tienda1 = pygame.Rect(1100,10,150,50)
        tienda2 = pygame.Rect(1096,6,158,58)     
        pygame.draw.rect(screen, (255,233,0),tienda2,border_radius=50)
        pygame.draw.rect(screen, (75,54,33),tienda1,border_radius=50)
        screen.blit(cofre,(1155,15))
        screen.blit(escudo222,(230,45))
        
        #animacion boton de tienda
        
        if tienda1.collidepoint((mx,my)):
          pygame.draw.rect(screen, (255,233,0),tienda2,border_radius=50)
          pygame.draw.rect(screen, (238,208,157),tienda1,border_radius=50)
          screen.blit(cofre,(1155,15))
          escribir("TIENDA", f3, (0, 0 , 0), screen, 1120, 70)
          if event.type == MOUSEBUTTONDOWN:
              tienda()
              escribir(tescudo,f3, (255, 255 , 255), screen, 266, 50)

        #balas 
        balatest.draw(screen)
        line=[(balatest.x,balatest.y),(mx,my)]


        pygame.draw.line(screen, (0,0,0), line[0], line[1])
        
        #animación cañon
        if mx>110:
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
        escribir(toro,f3, (255, 255 , 255), screen, 65, 50)
        escribir(tpuntuación,f3, (0,0,0), screen, 125, 85)
        escribir("Puntaje:",f3, (0,0,0), screen, 10, 85)
        escribir(tescudo,f3, (255, 255 , 255), screen, 266, 50)
        
        if enemigos.rect.left <= 0:
           vida = vida-10
           sprites.remove(enemigos)
           del enemigos
           enemigos = Enemigos()
           sprites.add(enemigos)
        

        if enemigos1.rect.left <= 0:
           vida = vida-10
           sprites.remove(enemigos1)
           del enemigos1
           enemigos1 = Enemigos()
           sprites.add(enemigos1)
          

        if enemigos2.rect.left <= 0:
           vida = vida-10
           sprites.remove(enemigos2)
           del enemigos2
           enemigos2 = Enemigos()
           sprites.add(enemigos2)
           
        
        if difficult==1:
            enemigos.rect.x -= 3
            enemigos1.rect.x-=5
            if enemigos.rect.left <= 0:
             vida = vida-15
             sprites.remove(enemigos)
             del enemigos
             enemigos = Enemigos()
             sprites.add(enemigos)
            

            if enemigos1.rect.left <= 0:
             vida = vida-12
             sprites.remove(enemigos1)
             del enemigos1
             enemigos1 = Enemigos()
             sprites.add(enemigos1)
            

            if enemigos2.rect.left <= 0:
             vida = vida-10
             sprites.remove(enemigos2)
             del enemigos2
             enemigos2 = Enemigos()
             sprites.add(enemigos2)
          

        if difficult==2:
            enemigos.rect.x -= 5
            enemigos1.rect.x-=7
            if enemigos.rect.left <= 0:
             vida = vida-22
             sprites.remove(enemigos)
             del enemigos
             enemigos = Enemigos()
             sprites.add(enemigos)
           

            if enemigos1.rect.left <= 0:
             vida = vida-19
             sprites.remove(enemigos1)
             del enemigos1
             enemigos1 = Enemigos()
             sprites.add(enemigos1)
             

            if enemigos2.rect.left <= 0:
             vida = vida-17
             sprites.remove(enemigos2)
             del enemigos2
             enemigos2 = Enemigos()
             sprites.add(enemigos2)
             

        if difficult==3:
            enemigos.rect.x-= 8
            enemigos1.rect.x-=10
            if enemigos.rect.left <= 0:
             vida = vida-25
             sprites.remove(enemigos)
             del enemigos
             enemigos = Enemigos()
             sprites.add(enemigos)
             

            if enemigos1.rect.left <= 0:
             vida = vida-22
             sprites.remove(enemigos1)
             del enemigos1
             enemigos1 = Enemigos()
             sprites.add(enemigos1)
             

            if enemigos2.rect.left <= 0:
             vida = vida-20
             sprites.remove(enemigos2)
             del enemigos2
             enemigos2 = Enemigos()
             sprites.add(enemigos2)
             



        #generacion de preguntas
        tiempomonda = int((pygame.time.get_ticks())/1000)
        if tiempomonda == multiplo_de_diez2:
            preguntas ()
            multiplo_de_diez2 = multiplo_de_diez2 + 15
            
            


        #usos de los sprites
        sprites.update()
        pygame.display.flip()
        
        
        #bala
        if shoot:
            if balatest.y<h-balatest.radio:
                tiempob+=0.4
                po = bala.balatray(bx, by, power, angle, tiempob)
                balatest.x= po[0]
                balatest.y= po[1]
            else:
                shoot=False
                balatest.x=cañonx 
                balatest.y=cañony

        # Colision bala - enemigo
        if shoot==True:
         if enemigos.rect.collidepoint((balatest.x, balatest.y)):
             pygame.mixer.Sound.play(sound_explosion)
             sprites.remove(enemigos)
             del enemigos
             enemigos = Enemigos()
             sprites.add(enemigos)
             shoot = False
             balatest.x=cañonx 
             balatest.y=cañony

         if enemigos1.rect.collidepoint((balatest.x, balatest.y)):
             sprites.remove(enemigos1)
             del enemigos1
             enemigos1 = Enemigos()
             sprites.add(enemigos1)
             shoot = False
             balatest.x=cañonx
             balatest.y=cañony
        
         if enemigos2.rect.collidepoint((balatest.x, balatest.y)):
             sprites.remove(enemigos2)
             del enemigos2
             enemigos2 = Enemigos()
             sprites.add(enemigos2)
             shoot = False
             balatest.x=cañonx
             balatest.y=cañony
  

        
        
        



            
        #controles
        for event in pygame.event.get(): 
            if event.type == MOUSEBUTTONDOWN:
                if shoot == False:
                    pygame.mixer.Sound.play(sound_canon)
                    shoot=True  
                    by=balatest.y
                    bx=balatest.x
                    tiempob=0
                    power= math.sqrt((line[1][1]-line[0][1])**2+(line[1][0]-line[0][0])**2)/8
                    angle =findAngle((mx,my))
            if balatest.x > 1000 or balatest.x < 0:
                balatest.x = cañonx
                balatest.y = cañony
            if balatest.y > 400:
                balatest.x = cañonx
                balatest.y = cañony

            if event.type==pygame.QUIT:
                pygame.quit() 
                exit(0) 
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running=False
        if vida <= 0:
            reinicio()
        


        reloj.tick(60)
        pygame.display.update()

#función de reinicio       
def reinicio():
    global tiempo
    global vida
    global oro
    global escudo
    global puntuación
    tpuntuación=str(puntuación)
    running=True
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.blit(fondoderr,(0,0))
        escribir("Su puntuación fue:",f3, (255,255,255), screen, w/2-250, (h/2)+200)
        escribir(tpuntuación,f3, (255,255,255), screen, (w/2)+50, (h/2)+200)
        botrb=circle(screen,(255,233,0),(w/2,(h/2)+100),65)
        botr=circle(screen,(75,54,33),(w/2,(h/2)+100),60)
        screen.blit(botonr,((w/2)-50,(h/2)+50))
        if botr.collidepoint((mx,my)):
          botrb=circle(screen,(255,233,0),(w/2,(h/2)+100),65)
          botr=circle(screen,(238,208,157),(w/2,(h/2)+100),60)
          screen.blit(botonr,((w/2)-50,(h/2)+50))
          if event.type == MOUSEBUTTONDOWN:
             tiempo=0
             vida=100
             oro=0
             escudo = 0
             puntuación = 0
             running = False
             game()              
        

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
    global vida
    global oro
    global puntuación
    global escudo
    global tiempo
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
             tiempo=0
             vida=100
             oro=0
             escudo = 0
             puntuación = 0
             running = False
             game()

             
        if bot2.collidepoint((mx,my)):
            pygame.draw.rect(screen, (255,255,255),bot2b,border_radius=50)
            pygame.draw.rect(screen, (178,130,91),bot2,border_radius=50)
            escribir("Normal", f2, (255, 255 , 255), screen, 560, 423)            
            if event.type == MOUSEBUTTONDOWN:
             difficult = 2
             tiempo=0
             vida=100
             oro=0
             escudo = 0
             puntuación = 0
             running = False
             game()
             
             
        if bot3.collidepoint((mx,my)):
            pygame.draw.rect(screen, (255,255,255),bot3b,border_radius=50)
            pygame.draw.rect(screen, (178,130,91),bot3,border_radius=50) 
            escribir("Dificil", f2, (255, 255 , 255), screen, 570, 623)
            if event.type == MOUSEBUTTONDOWN:
             difficult = 3
             tiempo=0
             vida=100
             oro=0
             escudo = 0
             puntuación = 0
             running = False
             game()
             
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:            
                pygame.quit() 
                exit(0) 
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running=False
        reloj.tick(60)
        pygame.display.update()

def tienda():
    fosforo=True 
    
    global balatest
    global escudo
    global vida
    global bola
    global oro

    while fosforo:
        mx ,my = pygame.mouse.get_pos()
        
        screen.blit(fondo_tienda,(330,10))
        

        bbb1=circle(screen,(255,255,255),(575,125),25)
        bbb2=circle(screen,(255,255,255),(575,490),25)
        bbb3=circle(screen,(255,255,255),(580,330),15)
        bbb4=circle(screen,(255,255,255),(580,230),15)
        bbb5=circle(screen,(255,255,255),(580,610),15)
        
        screen.blit(tamañobala,(550,590))
        screen.blit(imagendaño,(550,470))
        screen.blit(vidaimagen1,(550,300))
        screen.blit(pocion,(550,100))
        screen.blit(pocion50,(550,210))
       
        escribir("MEJORAS DE VIDA:", f3, (0, 0 , 0), screen, 550, 60)
        escribir("MEJORAS DE ATAQUE:", f3, (0, 0 , 0), screen, 550, 400)
        escribir("Mejora de escudo", f3, (0, 0 , 0), screen, 620, 110)
        escribir("Curación de vida pequeña", f3, (0, 0 , 0), screen, 620, 310)
        escribir("500 de oro", f3, (0, 0 , 0), screen, 620, 140)
        escribir("1000 de oro", f3, (0, 0 , 0), screen, 620, 240)
        escribir("500 de oro", f3, (0, 0 , 0), screen, 620, 340)
        escribir("500 de oro", f3, (0, 0 , 0), screen, 620, 640)
        escribir("500 de oro", f3, (0, 0 , 0), screen, 620, 520)
        escribir("Mejora de daño", f3, (0, 0 , 0), screen, 620, 480)
        escribir("Tamaño de bala", f3, (0, 0 , 0), screen, 620, 600)
        escribir("Poción de vida grande", f3, (0, 0 , 0), screen, 620, 210)
        
        if bbb3.collidepoint((mx,my)):
            if oro >= 500 and vida <= 50:
               if event.type == MOUSEBUTTONDOWN:
                    vida=vida+10
                    oro = oro-500  
           

        if bbb5.collidepoint((mx,my)):
           if oro >= 500:
               if event.type == MOUSEBUTTONDOWN:
                    balatest=bala(cañonx, cañony, 30, (130,130,130))
                    oro=oro-500

          

        if bbb4.collidepoint((mx,my)):
           if oro >= 1000 and vida <= 20:
               if event.type == MOUSEBUTTONDOWN:
                  vida=vida+20 
                  oro = oro-1000 

        if bbb1.collidepoint((mx,my)):
           circle(screen,(155,155,155),(575,125),25),screen.blit(pocion,(550,100))
           if oro >= 500:
                if event.type == MOUSEBUTTONDOWN:
                   escudo=escudo+10
                   tescudo=str(escudo)
                   oro = oro-500

        if bbb2.collidepoint((mx,my)):
           circle(screen,(155,155,155),(575,490),25)
           screen.blit(imagendaño,(550,470))
           #if event.type == MOUSEBUTTONDOWN:
        
        for event in pygame.event.get():
             
           if event.type==pygame.QUIT:            
               pygame.quit() 
               exit(0) 

           if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                  fosforo=False
        
        #print(mx,my)
        reloj.tick(60)
        pygame.display.update()


def preguntas():
    global oro
    global vida
    mx ,my = pygame.mouse.get_pos()
    pepino = True
    pregunta = True
    screen.blit(fondo_preguntas,(330,80))
    escribir("¿Lograrás defender el puerto?", f3, (0,0,0), screen, 350, 90)
    global multiplo_de_diez2
    
    bbb8=circle(screen,(255,255,255),(395,255),13)
    bbb9=circle(screen,(255,255,255),(395,305),13)
    bbb10=circle(screen,(255,255,255),(395,355),13)

    while pepino:
        mx ,my = pygame.mouse.get_pos()

        #escenario 

        lista_pregunt = [("La ciencia física es una ciencia fundamental, esto quiere decir que para explicarla:",["A. No necesita de otras ciencias naturales.",
        "B. Necesita y se fundamenta en otras ciencias naturales.","C. Sus conceptos deben ser particulares y limitados en el tiempo"],
        "A. No necesita de otras ciencias naturales."),("En el diagrama de cuerpo libre:",["A. Se deben tomar en cuenta las fuerzas internas.",
        "B. No se deben tomar en cuenta las fuerzas internas.","C. Ninguna respuesta anterior es correcta."],
        "C. Ninguna respuesta anterior es correcta."),("La energía potencial gravitatoria de una partícula se incrementa cuando:",["A. Una fuerza externa no realiza trabajo activo.",
        "B. Una fuerza externa realiza trabajo resistente.","C. El peso de la partícula realiza trabajo resistente."],
        "C. El peso de la partícula realiza trabajo resistente.")]

        if bbb8.collidepoint((mx,my)):
           if event.type == MOUSEBUTTONDOWN:
             circle(screen,(155,155,155),(395,255),13)
             vida-=25
             pepino = False
    
        if bbb9.collidepoint((mx,my)):
           if event.type == MOUSEBUTTONDOWN:
             circle(screen,(155,155,155),(395,305),13)
             vida-=25
             pepino = False

        if bbb10.collidepoint((mx,my)):
           if event.type == MOUSEBUTTONDOWN:
             circle(screen,(155,155,155),(395,355),13)
             oro+=250
             pepino = False

        
        while pregunta:
        
          indice = random.randint(0, len(lista_pregunt)-1)

          texto = fuente.render(lista_pregunt[indice][0],True,(0,0,0))
          screen.blit(texto,(390,200))
          
          for i in range (0,3):
               opciones = fuente.render(lista_pregunt[indice][1][i],True,(0,0,0))
               screen.blit(opciones,(390,200+(50*(i+1))))
          
          pregunta = False

        for event in pygame.event.get():
             
            if event.type==pygame.QUIT:            
               pygame.quit() 
               exit(0) 

        
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

#5.1 El alcance de un tiro parabólico depende de:
#A. velocidad inicial y ángulo de tiro
#B. masa del cuerpo
#C. fuerza aplicada
#D. tiempo de vuelo

#6.1 El trabajo se mide en:
#A. Vatios
#B. Amperios
#C. Joules
#D. m/s^2

#7.1 El alcance máximo se obtiene usando un ángulo de:
#A. para cualquier ángulo el alcance es igual
#B. 30°
#C. 75°
#D. 45°

#8.1 La segunda ley de Newton afirma que:
#A. para cualquier acción hay una reacción equivalente
#B. la suma de las fuerzas es proporcional al producto de las masas y la aceleración del sistema
#C. la fuerza de gravedad es proporcional al cociente del producto de las masas y la constante de gravedad universal, sobre la distancia entre los cuerpos
#D. un cuerpo que se encuentra en reposo o en movimiento rectilíneo uniforme sólo cambiará su estado si se le aplica una fuerza
