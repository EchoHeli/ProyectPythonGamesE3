"""
INICIO

Muestra las instrucciones del juego

Pedir al usuario que escoga la dificultad (Fácil, Media o Difícil)
→ Según la dificultad, definir el tamaño del tablero

Colocamos la serpiente en el centro del tablero
Inicializamos la dirección en la derecha
Inicializamos el puntaje
Generar una manzana en una posición aleatoria en donde no este la serpiente

Limpiar pantalla
Mostrar el tablero con la serpiente, la manzana y los puntos

MIENTRAS el juego no ! == game over:
    Pedir al usuario una dirección y número de pasos (ej. w 3)

    SI la entrada no es válida:
        Mostrar mensaje de error

    Convertir la dirección y pasos a variables

    REPETIR hasta game over:
        Calcular la nueva posición de la cabeza de la serpiente
         Insertar la nueva cabeza al inicio de la lista de la serpiente

        SI la nueva cabeza está en la misma posición que la manzana:
            Aumentar puntos en 1
            Mostrar mensaje de que comió una manzana
            Generar una nueva manzana en una posición libre
        SINO:
            Eliminar la última parte del cuerpo de la serpiente (no crece)

        Limpiar pantalla
        Mostrar el tablero actualizado con la serpiente, la manzana y los puntos obtenidos

        SI la nueva posición está fuera del tablero o choca con el cuerpo:
            Mostrar mensaje de choque
            Mostrar puntaje final
            Terminar el juego


FIN
Slida:
Mensaje de game over y puntaje final
"""
import random
import time
import os
import platform


def instructions_snake():
    instrucciones = open ("snake.txt","r")
    reglas = instrucciones.read()
    print (reglas)
def limpiar_pantalla():
        os.system("cls" if os.name == "nt" else "clear") # Para borrrar mi tablero anterior

def mostrar_tablero(ancho, alto, snake, manzana,puntos):
    print("+" + "-" * ancho + "+")  # Limite de mi tablero superior  # Limite de mi tablero superior #Se imprime de color amarillo
    for i in range(alto):
        fila = "\033[93m|\033[0m" # Limite izquierdo #El borde es color amarillo
        for r in range(ancho):
            if [i, r] == manzana: # Cordenadas de la manzana
                fila += "\033[91m*\033[0m" #Imprime la manzana de color rojo
            elif [i, r] in snake: #Cordenadas de la serpiente
                if [i, r] == snake[0]:
                    fila += "\033[92m+\033[0m"  # Cabeza de color verde
                else:
                    fila += "\033[92m-\033[0m"  # Cuerpo de color verde
            else:
                fila += " " #Casilla vacia (no se dibuja nada)
        fila += "\033[93m|\033[0m" # Limite derecho de color amarillo
        print(fila)
    print("\033[93m+" + "-" * ancho + "+\033[0m")  # borde inferior de color amarillo
    print("\033[95mPuntos: " + str(puntos) + "\033[0m") # Imprime el dialogo de puntos de color morado

def mover(direccion, cabeza):
    if direccion == 'w':  # arriba
        return [cabeza[0] - 1, cabeza[1]]
    elif direccion == 's':  # abajo
        return [cabeza[0] + 1, cabeza[1]]
    elif direccion == 'a':  # izquierda
        return [cabeza[0], cabeza[1] - 1]
    elif direccion == 'd':  # derecha
        return [cabeza[0], cabeza[1] + 1]
    return cabeza

def nueva_manzana(alto, ancho, snake):
    while True:
        manzana = [random.randint(0, alto - 1), random.randint(0, ancho - 1)] # Escoge una fila y columana aleatroria y las hace cordenadas (fila, columna)
        if manzana not in snake: #Si la serpiente no esta en las cordenadas de la manzana
            return manzana #Las cordenadas de la manzan se quedan igual
def seleccionar_dificultad(dificultad):
    dificultad = dificultad.lower()
    if dificultad in ["fácil", "facil"]:
        return (15 , 50)
    elif dificultad in ["media"]:
        return (8, 35)
    elif dificultad in ["difícil", "dificil"]:
        return (5, 25)
    else:
        print("Dificultad no válida. Se usará 'Media' por defecto")
        return (8, 35)


