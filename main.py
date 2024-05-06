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

            for i in range(grid_size):
                for j in range(grid_size):
                    x_inicial = 110
                    y_inicial = 110
                    x_inicial *= i + 1
                    y_inicial *= j + 1

                    if i == grid_size-1 and j == grid_size-1:
                        cuadro_negro = Cuadro_negro(negro , x_inicial , y_inicial , cuadro_alto , cuadro_ancho)
                        cuadro_negro.dibujar()
                    else:
                        cuadro_blanco = Cuadro_blanco(blanco , x_inicial , y_inicial , cuadro_alto , cuadro_ancho , fuente , grid_size)
                        cuadro_blanco.dibujar()
                        cuadro_blanco.texto()

            pygame.display.flip()


if __name__ == "__main__":
    main()