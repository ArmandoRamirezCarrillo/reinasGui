#libreria para visualizar la interfaz
import pygame
 
# Colores del tablero de ajedrez
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
CAFE = (128,64,0)
REINA = (234,190,63)

# Tamaño de la celda
LARGO  = 20
ALTO = 20
 
# Margen entre las celdas.
MARGEN = 5

grid = []
for fila in range(8):
    grid.append([])
    for columna in range(8):
        grid[fila].append(0)

def analizandolados(grid,fila,columna):
    tamaño = len(grid)

    #izquierda
    for i in range(columna):
        if(grid[fila][i] == 1):
            return False

    #derecha
    for i in range(columna,tamaño,1):
        if(grid[fila][i] == 1):
            return False

    #diagonal superior izquierda
    for f,c in zip(range(fila,-1,-1), range(columna,-1,-1)):
        if(grid[f][c] == 1):
            return False
        
    #diagonal superior derecha
    for f,c in zip(range(fila,-1,-1), range(columna,tamaño,1)):
        if(grid[f][c] == 1):
            return False

    #diagonal inferior izquierda
    for f,c in zip(range(fila,tamaño,1), range(columna,-1,-1)):
        if(grid[f][c] == 1):
            return False

    #diagonal inferior derecha
    for f,c in zip(range(fila,-1,-1), range(columna,tamaño,1)):
        if(grid[f][c] == 1):
            return False

    return True

#Verifica si la columna ya tiene o no una Reina
def columnaLlena(grid,columna):
    tamaño = len(grid)
    for i in range(tamaño):
        if(grid[i][columna] == 1):
            return True
    return False

def acomodandoReinas(grid, columna):
    tamaño = len(grid)
    if(columna >= tamaño):
        return True
    
    if(columnaLlena(grid,columna) == True):
        if(acomodandoReinas(grid, columna + 1) == True):
            return True
        
    for i in range(tamaño):
        if(analizandolados(grid,i,columna)):
            grid[i][columna] = 1
            if(acomodandoReinas(grid,columna + 1) == True):
                return True
            grid[i][columna] = 0
        grid[i][columna] = 0
    return False

# Colocando la primera reina
grid[0][0] = 1

acomodandoReinas(grid,0)

# Inicializamos pygame
pygame.init()
  
# Dimenciones de la ventana
DIMENSION_VENTANA = [215, 215]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
 
# Título de la pantalla.
pygame.display.set_caption("8 Reinas")

 
# Como se visualiza la pantalla
reloj = pygame.time.Clock()

def main():
    # Bandera de salida
    hecho = False
    while not hecho:
        for evento in pygame.event.get(): 
            if evento.type == pygame.QUIT: 
                hecho = True
    
        # Fondo de pantalla.
        pantalla.fill(CAFE)
    
        # Dibujando el tablero de ajedrez
        for fila in range(8):
            for columna in range(8):
                # if(grid[fila][columna] == 2):
                #     color = NEGRO
                color = BLANCO
                if grid[fila][columna] == 1:
                    color = REINA
                pygame.draw.rect(pantalla,
                                color,
                                [(MARGEN+LARGO) * columna + MARGEN,
                                (MARGEN+ALTO) * fila + MARGEN,
                                LARGO,
                                ALTO])
        
        # 60 fotogramas por segundo.
        reloj.tick(60)
    
        # Muestra la pantalla con lo que se haya dibujado.
        pygame.display.flip()

    pygame.quit()

main()

# 664 655 2242