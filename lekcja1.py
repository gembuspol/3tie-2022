import pygame
import random
import waz



def main():
    obiektWaz=waz.Waz()

    #losowanie pozycji jablka
    xApple=random.randint(0,14)*20+10
    yApple=random.randint(0,14)*20+10
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
        pygame.draw.circle(Oknogry,(0,255,0),(xApple,yApple),10)
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
        if glowaWazX==xApple-10 and glowaWazY==yApple-10:
            obiektWaz.snakeEat()
            #dlugosc=dlugosc+1
            #losowanie pozycji jablka
            xApple=random.randint(0,14)*20+10
            yApple=random.randint(0,14)*20+10
            #rysowanie jabłka
            pygame.draw.circle(Oknogry,(255,255,0),(xApple,yApple),10)
        
        czcionka=pygame.font.SysFont('comicsans',20)
        tekst=czcionka.render("Punkty {0}".format(obiektWaz.punkty),1,(255,255,0))
        Oknogry.blit(tekst,(10,10))
       
        pygame.display.update()

main()