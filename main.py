import random

from pantalla import *
from claseCuadro import *
from config import *

def main():
    numeros = list(range(1, (grid_size * grid_size)))
    random.shuffle(numeros)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        else:
            pantalla_propiedades()

            #Creando lista números

            cuadros_blancos = []
            cuadros_negros = []
            indice_numero = 0

            for i in range(grid_size):
                for j in range(grid_size):
                  
                    numero = numeros[indice_numero - 1]

                    if i == grid_size-1 and j == grid_size-1:
                        cuadro_blanco = Cuadro_blanco(negro , i , j , cuadro_alto , cuadro_ancho , numero , screen)
                        cuadros_negros.append(cuadro_blanco)
                        indice_numero += 1                       
                    else:
                        cuadro_blanco = Cuadro_blanco(blanco , i , j , cuadro_alto , cuadro_ancho , numero , screen)
                        cuadros_blancos.append(cuadro_blanco)
                        indice_numero += 1


            for cuadro in cuadros_blancos:
                cuadro.dibujar()
                cuadro.texto()
            
            for cuadro in cuadros_negros:
                cuadro.dibujar()
            
            pygame.display.flip()


if __name__ == "__main__":
    main()