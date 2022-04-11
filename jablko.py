import random
import pygame
import lekcja1
class Jablko():
    #konstruktor klasy
    def __init__(self):
        self.applePosition=(20,20)
        self.randPosition()
    def setPosition(self,x,y):
        self.applePosition=(x,y)
    def getPosition(self):
        return self.applePosition
    def drawApple(self,Oknogry):
        pygame.draw.circle(Oknogry,(128,0,0),(self.applePosition[0], self.applePosition[1]),10)
    def randPosition(self):
        rozmiar=lekcja1.rozdzielczosc//20-1
        xApple=random.randint(0,rozmiar)*20+10
        yApple=random.randint(0,rozmiar)*20+10
        self.setPosition(xApple,yApple)