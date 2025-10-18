    print("Bienvenido al juego de Memorama!")

# archivo: Memorama/memorama.py
# -------------------------------------------------------------
# Juego de Memorama en Python
# Este módulo contiene todas las funciones necesarias para jugar
# al memorama.


import random
import time

def crear_tablero(num_pares=8):
    """
    Crea una lista de cartas con pares y las mezcla aleatoriamente.
    num_pares: cantidad de pares que quieres en el juego (por defecto 8).
    Retorna la lista de cartas mezcladas.
    """
    cartas_base = [chr(65 + i) for i in range(num_pares)]  # A, B, C...
    cartas = cartas_base * 2  # duplicamos para tener pares
    random.shuffle(cartas)
    return cartas


def mostrar_tablero(tablero, descubiertas):
    """
    Muestra el tablero actual mostrando solo las cartas descubiertas.
    tablero: lista de cartas
    descubiertas: lista de índices que ya se han descubierto
    """
    for i in range(len(tablero)):
        if i in descubiertas:
            print(f"[{tablero[i]}]", end=" ")
        else:
            print("[ ]", end=" ")
        if (i + 1) % 4 == 0:  # salto de línea cada 4 cartas
            print()
    print()


def jugar_turno(tablero, descubiertas):
    """
    Solicita al jugador elegir dos cartas y actualiza la lista de descubiertas.
    Retorna True si el jugador encontró un par, False si no.
    """
    try:
        a = int(input(f"Elige la primera carta (0-{len(tablero)-1}): "))
        b = int(input(f"Elige la segunda carta (0-{len(tablero)-1}): "))
    except ValueError:
        print("Entrada inválida. Ingresa números válidos.")
        return False

    if a == b or a not in range(len(tablero)) or b not in range(len(tablero)):
        print("Selección inválida.")
        return False

    if tablero[a] == tablero[b]:
        print("¡Par encontrado! ")
        descubiertas.extend([a, b])
        return True
    else:
        print("No coinciden. Intenta de nuevo.")
        return False


def jugar_memorama():
    """
    Función principal del juego.
    Llama a otras funciones para crear el tablero y manejar los turnos.
    """
    tablero = crear_tablero()
    descubiertas = []
    intentos = 0

    while len(descubiertas) < len(tablero):
        mostrar_tablero(tablero, descubiertas)
        jugar_turno(tablero, descubiertas)
        intentos += 1
        time.sleep(1)

    print(f"¡Felicidades! Terminaste el juego en {intentos} intentos.")


def pruebas():
    """
    Función de pruebas para cada función del módulo.
    Verifica que las funciones principales funcionen correctamente.
    """
    print("Prueba de crear_tablero()")
    tablero = crear_tablero(4)
    print(tablero)
    assert len(tablero) == 8, "Error: El tablero no tiene el tamaño correcto."

    print("Prueba de mostrar_tablero()")
    mostrar_tablero(tablero, [])
    mostrar_tablero(tablero, [0, 1])
    print("Pruebas de mostrar_tablero() completadas")

    print("Prueba de jugar_turno()")
    descubiertas = []
    # Simulamos dos cartas iguales para probar
    tablero = ["A", "A", "B", "B"]
    # Se puede llamar manualmente la función para testear
    # Nota: Para pruebas automatizadas, habría que simular input
    print("Pruebas completas (simulación manual necesaria para jugar_turno)")



