import random

from abc import ABC, abstractmethod
from pantalla import screen

import pygame
pygame.init()

#Creando clase abstracta (es como una plantilla general) para los dos tipos de cuadros

class Cuadro_base(ABC):
    def __init__(self , color , x_inicial , y_inicial , cuadro_alto , cuadro_ancho):
        self.color = color
        self.rect = None
        self.x = x_inicial
        self.y = y_inicial
        self.alto = cuadro_alto
        self.ancho = cuadro_ancho

    @abstractmethod
    def dibujar(self):
        pass

#Definiendo ambos tipos de cuadros

class Cuadro_negro(Cuadro_base):
    def __init__(self , color , x_inicial , y_inicial , cuadro_alto , cuadro_ancho):
        super().__init__(color , x_inicial , y_inicial , cuadro_alto , cuadro_ancho)

    def dibujar(self):
        pygame.draw.rect(screen, self.color , (self.x , self.y , self.ancho, self.alto))
        # pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.ancho, self.alto)) -> EL orden, es que se me olvida XD

    def mover(self):
        pass


class Cuadro_blanco(Cuadro_base):
    def __init__(self , color , x_inicial , y_inicial , cuadro_alto , cuadro_ancho , numero , pantalla):
        super().__init__(color , x_inicial , y_inicial , cuadro_alto , cuadro_ancho)

        self.numero = numero
        self.pantalla = pantalla
        self.x_inicial = x_inicial
        self.y_inicial = y_inicial

    def dibujar(self):
        pygame.draw.rect(self.pantalla, self.color, (self.x_inicial * self.ancho, self.y_inicial * self.alto, self.ancho, self.alto))

    def texto(self):
        font = pygame.font.SysFont(None, 40)
        texto = font.render(str(self.numero), True, (0,0,0))
        texto_rect = texto.get_rect(center=(self.x_inicial * self.ancho + self.ancho // 2, self.y_inicial * self.alto + self.alto // 2))
        self.pantalla.blit(texto, texto_rect)
