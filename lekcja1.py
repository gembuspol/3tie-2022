import pygame
import random
import waz
import jablko
rozdzielczosc=500
obiektWaz1=waz.Waz()
obiektWaz2=waz.Waz()
def zmienKolorWaz1(kolor):
    obiektWaz1.setColor(kolor)


iloscJablek=5
def main():
    
    obiektJablko=[]
    for nrJablka in range(0,iloscJablek):
        obiektJablko.append(jablko.Jablko())

    
    pygame.init()
    Oknogry=pygame.display.set_mode((rozdzielczosc,rozdzielczosc),0,32)
    run=True

    
    while(run):
        glowa=obiektWaz1.getHeadPosition()
        glowaWaz1X=glowa[0]
        glowaWaz1Y=glowa[1]
        glowa2=obiektWaz2.getHeadPosition()
        glowaWaz2X=glowa2[0]
        glowaWaz2Y=glowa2[1]
        Oknogry.fill((0,0,0))
        pygame.time.delay(100)
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #sterowanie weża
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    obiektWaz1.setDirection((-1,0))
                elif event.key == pygame.K_RIGHT:
                    obiektWaz1.setDirection((1,0))
                elif event.key == pygame.K_UP:
                    obiektWaz1.setDirection((0,-1))
                elif event.key == pygame.K_DOWN:
                    obiektWaz1.setDirection((0,1))
                elif event.key == pygame.K_a:
                    obiektWaz2.setDirection((-1,0))
                elif event.key == pygame.K_d:
                    obiektWaz2.setDirection((1,0))
                elif event.key == pygame.K_w:
                    obiektWaz2.setDirection((0,-1))
                elif event.key == pygame.K_s:
                    obiektWaz2.setDirection((0,1))
                #sprawdzanie czy waz nie zjada siebie
                
        obiektWaz1.snakeMove()
        obiektWaz2.snakeMove()        
        #rysowanie węża
        obiektWaz1.drawSnake(Oknogry)
        obiektWaz2.drawSnake(Oknogry)    
            #zjedzenie jablka
        #rysowanie jablka
        for nrJablka in obiektJablko[::]:
                
            pozycjaJablka=nrJablka.getPosition()
            if glowaWaz1X==pozycjaJablka[0]-10 and glowaWaz1Y==pozycjaJablka[1]-10:
                obiektWaz1.snakeEat()
                
                #dlugosc=dlugosc+1
                #losowanie pozycji jablka
                nrJablka.randPosition()
            if glowaWaz2X==pozycjaJablka[0]-10 and glowaWaz2Y==pozycjaJablka[1]-10:
                obiektWaz2.snakeEat()
                
                #dlugosc=dlugosc+1
                #losowanie pozycji jablka
                nrJablka.randPosition()
            #rysowanie jabłka
            nrJablka.drawApple(Oknogry)
        obiektWaz1.bitMe(glowa2)
        obiektWaz2.bitMe(glowa)
        czcionka=pygame.font.SysFont('comicsans',20)
        tekst=czcionka.render("Punkty {0}".format(obiektWaz1.punkty),1,(255,255,0))
        tekst2=czcionka.render("Punkty {0}".format(obiektWaz2.punkty),1,(255,255,0))
        Oknogry.blit(tekst,(10,10))
        Oknogry.blit(tekst2,(10,30))
       
        pygame.display.update()

