import pygame

def main():
    pygame.init()
    Oknogry=pygame.display.set_mode((300,300),0,32)
    run=True
    while(run):
        pygame.time.delay(100)
        kwadrat = pygame.Rect((150,150),(20,20))
        pygame.draw.rect(Oknogry,(255,0,0),kwadrat)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

main()