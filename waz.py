import pygame
class Waz():
    #konstruktor klasy - uruchamia się podczas utworzenia obiektu
    def __init__(self):
        self.dlugosc=1
        self.pozycja=[(160,160)]
        self.punkty=0
    #zwrócenie pozycji głowy
    def getHeadPosition(self):
        return self.pozycja[-1]
    #dodanie nowej pozycj węża
    def addPosition(self,x,y):
        self.pozycja.append((x,y))
    #wykonanie ruchu przez węża
    def snakeMove(self,x,y):
        #sprawdzanie krawedzi
        noweWspolrzedne=self.checkBorder(x,y)
        #dodanie nowej pozycji
        self.addPosition(noweWspolrzedne[0],noweWspolrzedne[1])
        #jeżeli wąż jest za dlugi, usunięcie pierwszej pozycji
        if len(self.pozycja)>self.dlugosc:
            del self.pozycja[0]
    #zwiększanie paramtrów w momencie zjadania jablka
    def snakeEat(self):
        #self.dlugosc=self.dlugosc+1
        self.dlugosc+=1
    #rysowanie węża
    def drawSnake(self, Oknogry):
        for position in self.pozycja[::-1]:
            kwadrat = pygame.Rect((position[0],position[1]),(20,20))
            pygame.draw.rect(Oknogry,(255,0,0),kwadrat)
    #sprawdzanie krawedzi okna
    def checkBorder(self,zmienna1,zmienna2):
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
        return (zmienna1,zmienna2)
