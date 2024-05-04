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
                    x_inicial = 100
                    y_inicial = 100
                    x_inicial *= i + 1
                    y_inicial *= j + 1

                    texto = j

                    if i == grid_size-1 and j == grid_size-1:
                        cuadro = Cuadro(negro , x_inicial , y_inicial , cuadro_alto , cuadro_ancho , texto)
                        cuadro.dibujar()
                    else:
                        cuadro = Cuadro(blanco , x_inicial , y_inicial , cuadro_alto , cuadro_ancho , texto)
                        cuadro.dibujar()
                        cuadro.renderizar_texto()

            pygame.display.flip()

# Uf la extraño pero es raro XD

if __name__ == "__main__":
    main()