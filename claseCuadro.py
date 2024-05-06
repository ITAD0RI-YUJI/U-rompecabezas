from pantalla import screen
from config import fuente

import pygame
pygame.init()


class Cuadro():
    def __init__(self , color , x_inicial , y_inicial , cuadro_alto , cuadro_ancho):
        self.color = color
        self.rect = None
        self.x = x_inicial
        self.y = y_inicial
        self.alto = cuadro_alto
        self.ancho = cuadro_ancho


    def dibujar(self):
        pygame.draw.rect(screen, self.color , (self.x , self.y , self.ancho, self.alto))
        # pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.ancho, self.alto)) -> EL orden, es que se me olvida XD
