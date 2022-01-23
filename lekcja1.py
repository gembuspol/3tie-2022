import pygame

def main():
    pygame.init()
    pygame.display.set_mode((300,300),0,32)
    run=True
    while(run):
        pygame.time.delay(100)
        print("Program działa")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

main()