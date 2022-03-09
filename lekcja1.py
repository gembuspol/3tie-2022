import pygame
import random



def main():
    
    #losowanie pozycji jablka
    xApple=random.randint(0,14)*20+10
    yApple=random.randint(0,14)*20+10
    pygame.init()
    Oknogry=pygame.display.set_mode((300,300),0,32)
    run=True
    zmienna1=160
    zmienna2=160
    #lista pozycji
    wazPozycje=[(zmienna1,zmienna2)]
    #liczba punktów
    punkty=0
    #dlugosc weze
    dlugosc=1
    while(run):
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
                    zmienna1=zmienna1-20
                elif event.key == pygame.K_RIGHT:
                    zmienna1=zmienna1+20 
                elif event.key == pygame.K_UP:
                    zmienna2=zmienna2-20
                elif event.key == pygame.K_DOWN:
                    zmienna2=zmienna2+20 
                #sprawdzanie czy waz nie zjada siebie
                
                for czesciCiala in wazPozycje[::]:
                    if czesciCiala[0]==zmienna1 and czesciCiala[1]==zmienna2:
                        wazPozycje=[(zmienna1,zmienna2)]
                        dlugosc=1
                        punkty=0
                wazPozycje.append((zmienna1,zmienna2))
                if len(wazPozycje)>dlugosc:
                    del wazPozycje[0]  
                
        #rysowanie węża
        for position in wazPozycje[::-1]:
            kwadrat = pygame.Rect((position[0],position[1]),(20,20))
            pygame.draw.rect(Oknogry,(255,0,0),kwadrat)
            
            #zjedzenie jablka
        if zmienna1==xApple-10 and zmienna2==yApple-10:
            dlugosc+=1
            punkty+=1
            #dlugosc=dlugosc+1
            #losowanie pozycji jablka
            xApple=random.randint(0,14)*20+10
            yApple=random.randint(0,14)*20+10
            #rysowanie jabłka
            pygame.draw.circle(Oknogry,(255,255,0),(xApple,yApple),10)
        
        czcionka=pygame.font.SysFont('comicsans',20)
        tekst=czcionka.render("Punkty {0}".format(punkty),1,(255,255,0))
        Oknogry.blit(tekst,(10,10))
        #przejscie prawa
        if zmienna1>300:
            zmienna1=0
        #przejscie dol
        if zmienna2>300:
            zmienna2=0
        #przejscie lewa
        if zmienna1<0:
            zmienna1=300
        #przejscie gora
        if zmienna2<0:
            zmienna2=300
        pygame.display.update()

main()