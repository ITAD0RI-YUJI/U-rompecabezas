import random

from pantalla import *
from claseCuadro import *
from config import *

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        else:
            pantalla_propiedades()

            #Creando y Desordenando matriz de números
            matriz_inicial = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]
            random.shuffle(matriz_inicial)

            #Creando "cuadrícula" principal del juego
            for i in range(grid_size):
                for j in range(grid_size):
                    x_inicial = 100
                    y_inicial = 100
                    x_inicial *= i + 1
                    y_inicial *= j + 1

                    if i == grid_size-1 and j == grid_size-1:
                        cuadro = Cuadro(negro , x_inicial , y_inicial , cuadro_alto , cuadro_ancho)
                        cuadro.dibujar()
                    else:
                        cuadro = Cuadro(blanco , x_inicial , y_inicial , cuadro_alto , cuadro_ancho)
                        cuadro.dibujar()

            pygame.display.flip()


if __name__ == "__main__":
    main()