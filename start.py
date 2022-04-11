import pygame_menu
import  pygame
import lekcja1

def startGra():
    lekcja1.main()
def zmienRozdzielczosc(value,roz):
    lekcja1.rozdzielczosc=roz
def iloscJablek(value,ilosc):
    lekcja1.iloscJablek=ilosc
def main():
    pygame.init()
    OknoMenu=pygame.display.set_mode((500,500))
    pygame.display.set_caption("Menu Snake")
    menu=pygame_menu.Menu("Snake 3TIE",500,500,theme=pygame_menu.themes.THEME_SOLARIZED)
    menu.add.button("Start gry",startGra,background_color=(255,255,0))
    menu.add.selector("Rozmiar ekranu",[('500x500',500),('600x600',600),('800x800',800)],onchange=zmienRozdzielczosc)
    menu.add.selector("Ilość jabłek",[("1",1),("2",2),("3",3),("5",5),("10",10),("100",100),],onchange=iloscJablek)
    menu.mainloop(OknoMenu)

main()