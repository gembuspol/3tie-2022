import pygame_menu
import  pygame
import lekcja1

def startGra():
    lekcja1.main()
    
def main():
    pygame.init()
    OknoMenu=pygame.display.set_mode((500,500))
    pygame.display.set_caption("Menu Snake")
    menu=pygame_menu.Menu("Snake 3TIE",500,500,theme=pygame_menu.themes.THEME_SOLARIZED)
    menu.add.button("Start gry",startGra,background_color=(255,255,0))

    menu.mainloop(OknoMenu)

main()