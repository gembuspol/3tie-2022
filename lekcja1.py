import pygame
import random
import waz
import jablko


def main():
    obiektWaz=waz.Waz()
    obiektJablko=jablko.Jablko()

    
    pygame.init()
    Oknogry=pygame.display.set_mode((300,300),0,32)
    run=True

    
    while(run):
        glowa=obiektWaz.getHeadPosition()
        glowaWazX=glowa[0]
        glowaWazY=glowa[1]
        Oknogry.fill((0,0,0))
        pygame.time.delay(100)
        
        #rysowanie jablka
        obiektJablko.drawApple(Oknogry)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #sterowanie weża
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    obiektWaz.setDirection((-1,0))
                elif event.key == pygame.K_RIGHT:
                    obiektWaz.setDirection((1,0))
                elif event.key == pygame.K_UP:
                    obiektWaz.setDirection((0,-1))
                elif event.key == pygame.K_DOWN:
                    obiektWaz.setDirection((0,1))
                #sprawdzanie czy waz nie zjada siebie
                
        obiektWaz.snakeMove()
                
        #rysowanie węża
        obiektWaz.drawSnake(Oknogry)
            
            #zjedzenie jablka
        pozycjaJablka=obiektJablko.getPosition()
        if glowaWazX==pozycjaJablka[0]-10 and glowaWazY==pozycjaJablka[1]-10:
            obiektWaz.snakeEat()
            #dlugosc=dlugosc+1
            #losowanie pozycji jablka
            obiektJablko.randPosition()
            #rysowanie jabłka
            obiektJablko.drawApple(Oknogry)
        
        czcionka=pygame.font.SysFont('comicsans',20)
        tekst=czcionka.render("Punkty {0}".format(obiektWaz.punkty),1,(255,255,0))
        Oknogry.blit(tekst,(10,10))
       
        pygame.display.update()

main()