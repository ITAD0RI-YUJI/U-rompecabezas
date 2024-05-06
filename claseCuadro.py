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


class Cuadro_blanco(Cuadro_base):
    def __init__(self , color , x_inicial , y_inicial , cuadro_alto , cuadro_ancho , fuente , grid_size):
        super().__init__(color , x_inicial , y_inicial , cuadro_alto , cuadro_ancho)

        self.matriz_inicial = [["1" , "2" , "3"], ["4" , "5" , "6"], ["7" , "8"]]
        self.fuente = fuente
        self.grid_size = grid_size #Tamaño del juego

    def dibujar(self):
        pygame.draw.rect(screen, self.color , (self.x , self.y , self.ancho, self.alto))

    def texto(self):
        random.shuffle(self.matriz_inicial) #Desordenando matriz original

        #Recorriendo matriz 
        for i in range(self.grid_size-1):
            for j in range(self.grid_size-1):
                self.texto = self.matriz_inicial[i][j]
                finalText = self.fuente.render(self.texto, True, (150, 100, 20))

        #Dibujando texto dentro del cuadro
        screen.blit(finalText , (self.x , self.y))