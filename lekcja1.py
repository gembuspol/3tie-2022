import pygame

def main():
    pygame.init()
    Oknogry=pygame.display.set_mode((300,300),0,32)
    run=True
    zmienna1=150
    zmienna2=150
    while(run):
        Oknogry.fill((0,0,0))
        pygame.time.delay(100)
        kwadrat = pygame.Rect((zmienna1,zmienna2),(20,20))
        pygame.draw.rect(Oknogry,(255,0,0),kwadrat)
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
        #zmienna1=zmienna1+20
        if zmienna1>300:
            zmienna1=0
        #zmienna2=zmienna2+40
        if zmienna2>300:
            zmienna2=0
        pygame.display.update()

main()