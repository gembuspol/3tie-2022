import pygame
class Waz():
    #konstruktor klasy - uruchamia się podczas utworzenia obiektu
    def __init__(self):
        self.dlugosc=1
        self.pozycja=[(160,160)]
        self.punkty=0
        self.kierunek=(0,1)
    #ustalenie kierunku węża
    def setDirection(self,direction):
        self.kierunek=direction
    #zwrócenie pozycji głowy
    def getHeadPosition(self):
        return self.pozycja[-1]
    #dodanie nowej pozycj węża
    def addPosition(self,x,y):
        self.pozycja.append((x,y))
    #wykonanie ruchu przez węża
    def snakeMove(self):
        #generowanie nowych pozycji
        #ostatnia pozycja glowy
        ostatniaPozycja=self.pozycja[-1]
        x=ostatniaPozycja[0]+20*self.kierunek[0]
        y=ostatniaPozycja[1]+20*self.kierunek[1]
        #sprawdzanie krawedzi
        noweWspolrzedne=self.checkBorder(x,y)
        #sprawdzenie czy wąż nie zjadł sam siebie
        for czesciCiala in self.pozycja[::]:
            if czesciCiala[0]==noweWspolrzedne[0] and czesciCiala[1]==noweWspolrzedne[1]:
                self.dlugosc=1
                self.punkty=0
            
        #dodanie nowej pozycji
        if self.dlugosc==1:
            self.pozycja=[noweWspolrzedne]
        else:
            self.addPosition(noweWspolrzedne[0],noweWspolrzedne[1])
        #jeżeli wąż jest za dlugi, usunięcie pierwszej pozycji
        if len(self.pozycja)>self.dlugosc:
            del self.pozycja[0]
    #zwiększanie paramtrów w momencie zjadania jablka
    def snakeEat(self):
        #self.dlugosc=self.dlugosc+1
        self.dlugosc+=1
        self.punkty+=1
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
    


