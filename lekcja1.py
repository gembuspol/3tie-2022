import pygame
import random
import waz
import jablko

iloscJablek=5
def main():
    obiektWaz1=waz.Waz()
    obiektJablko=[]
    for nrJablka in range(0,iloscJablek):
        obiektJablko.append(jablko.Jablko())

    
    pygame.init()
    Oknogry=pygame.display.set_mode((300,300),0,32)
    run=True

    
    while(run):
        glowa=obiektWaz1.getHeadPosition()
        glowaWazX=glowa[0]
        glowaWazY=glowa[1]
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
                #sprawdzanie czy waz nie zjada siebie
                
        obiektWaz1.snakeMove()
                
        #rysowanie węża
        obiektWaz1.drawSnake(Oknogry)
            
            #zjedzenie jablka
        #rysowanie jablka
        for nrJablka in obiektJablko[::]:
                
            pozycjaJablka=nrJablka.getPosition()
            if glowaWazX==pozycjaJablka[0]-10 and glowaWazY==pozycjaJablka[1]-10:
                obiektWaz1.snakeEat()
                
                #dlugosc=dlugosc+1
                #losowanie pozycji jablka
                nrJablka.randPosition()
            #rysowanie jabłka
            nrJablka.drawApple(Oknogry)
        
        czcionka=pygame.font.SysFont('comicsans',20)
        tekst=czcionka.render("Punkty {0}".format(obiektWaz1.punkty),1,(255,255,0))
        Oknogry.blit(tekst,(10,10))
       
        pygame.display.update()

main()