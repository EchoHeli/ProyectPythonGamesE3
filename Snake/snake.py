import random
import time
import os
import platform


def instructions_snake():
    print (""" REGLAS DEL JUEGO
    Para moverte usa w,s,a,d de tu teclado:
    w - Ariba
    s - Abajo
    a - Izquierda
    d - Derecha
    Usa solo minusculas
    Para moverte escribe (Letra) (numero de espacios que deseas moverte)
    Ej. s 4, w 3, a 6, d 1
    Come el * para que tu serpiente cresca
    + es la cabeza de tu serpiente y cuando comas un * tu serpiente gana un -
    Tienes que crecer hasta llenar el tablero
    NO puedes chocar con el limite, ni contra ti mismo
    ¡MUCHA SUERTE!

    """)

def limpiar_pantalla():
        os.system("cls" if os.name == "nt" else "clear") # Para borrrar mi tablero anterior

def mostrar_tablero(ancho, alto, snake, manzana,puntos):
    print("+" + "-" * ancho + "+")  # Limite de mi tablero superior
    for i in range(alto):
        fila = "|" # Limite izquierdo
        for r in range(ancho):
            if [i, r] == manzana: # Cordenadas de la manzana
                fila += "*" #Imprime la manzana
            elif [i, r] in snake: #Cordenadas de la serpiente
                fila += "-" if [i, r] != snake[0] else "+" # La cabeza es un "+", el resto del cuerpo sera "-"
            else:
                fila += " " #Casilla vacia (no se dibuja nada)
        fila += "|" # Limite derecho
        print(fila)
    print("+" + "-" * ancho + "+")  # borde inferior
    print(f"Puntos: {puntos}")

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
    if dificultad in ["fácil", "facil","Fácil","Facil","FÁCIL","FACIL"]:
        return (15 , 50)
    elif dificultad in ["media","Media","MEDIA"]:
        return (8, 35)
    elif dificultad in ["difícil", "dificil","DIFICIL","DIFÍCIL"]:
        return (5, 25)
    else:
        print("Dificultad no válida. Se usará 'Media' por defecto")
        return (8, 35)


