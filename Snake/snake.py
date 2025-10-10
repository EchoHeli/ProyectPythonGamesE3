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
        os.system("cls") # Para borrrar mi tablero anterior

def mostrar_tablero(ancho, alto, snake, manzana):
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
    dificultad = input("¿Qué nivel te gustaría jugar? (Fácil / Media / Difícil): ").lower()
    if dificultad in ["fácil", "facil"]:
        return (30, 10)
    elif dificultad == "media":
        return (20, 7)
    elif dificultad in ["difícil", "dificil"]:
        return (10, 6)
    else:
        print("Dificultad no válida. Se usará 'Media' por defecto.")
        return (20, 7)

def main():
#Variables
    ancho = 0
    alto = 0
    snake = [[5, 5]]
    direccion = 'd'

    # Modo de dificultad
    dificultad = input("¿Qué nivel te gustaría jugar? (Fácil / Media / Difícil): ")
    alto, ancho = dificultadJuego(dificultad)

    manzana = nueva_manzana(alto, ancho, snake)

    limpiar_pantalla()
    mostrar_tablero(ancho, alto, snake, manzana)

    instructions_snake()

    while True:
        entrada = input("Dirección y pasos (ej. w 3): ").split()

        if len(entrada) != 2 or entrada[0] not in ('w', 'a', 's', 'd') or not entrada[1].isdigit():
            print("Entrada inválida. Usa formato: dirección pasos (ej. d 4)")
            continue

        direccion = entrada[0]
        pasos = int(entrada[1])

        for _ in range(pasos): #Numero de espacios que el usuario quiera moverse
            nueva_cabeza = mover(direccion, snake[0])

            if (nueva_cabeza in snake or #Te comiste a ti mismo
                nueva_cabeza[0] < 0 or nueva_cabeza[0] >= alto or #Te saliste del tablero (arriba y abajo)
                nueva_cabeza[1] < 0 or nueva_cabeza[1] >= ancho): # Te saliste del tablero (izquierda y derecha)
                print("Ups. Tu serpiente ha chocado :(")
                print("Game Over")
                return

            snake.insert(0, nueva_cabeza) #Agrega nuevo valor "-" a la lista de snake

            if nueva_cabeza == manzana: #Cabeza y manzana en la mismas cordenadas
                manzana = nueva_manzana(alto, ancho, snake) # Se aparece nueva manzana y crece la serpientee
            else:
                snake.pop() # Elimina la ultima parte de la lista ... quita el nuevo cuerpo de la serpiente, pq no comió

            limpiar_pantalla()
            mostrar_tablero(ancho, alto, snake, manzana)
            time.sleep(0.1) # Pausa el programa antes de su ejecucción, para que no se confunda el usuario
