from pantalla import SCREEN
from config import fuente

import pygame
pygame.init()


class Cuadro():
    def __init__(self , color , x_inicial , y_inicial , cuadro_alto , cuadro_ancho , texto):
        self.color = color
        self.rect = None
        self.x = x_inicial
        self.y = y_inicial
        self.alto = cuadro_alto
        self.ancho = cuadro_ancho
        self.texto = texto

    def dibujar(self):
        pygame.draw.rect(SCREEN, self.color , (self.x , self.y , self.ancho, self.alto) , border_radius = 6)
        # pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.ancho, self.alto)) -> EL orden, es que se me olvida XD

    def renderizar_texto(self):
        texto = str(self.texto)
        renderizado = fuente.render(texto , True , (0,0,0))
    
        return renderizado 