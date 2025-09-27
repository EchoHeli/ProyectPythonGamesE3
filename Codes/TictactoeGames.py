# tictactoe_3d.py
import itertools

# Crear tablero 3D vacío
def crear_tablero():
    return [[[" " for _ in range(3)] for _ in range(3)] for _ in range(3)]

# Imprimir los 3 niveles
def mostrar_tablero(tablero):
    for z in range(3):
        print(f"\nNivel {z}:")
        for y in range(3):
            fila = " | ".join(tablero[z][y])
            print(" " + fila)
            if y < 2:
                print("---+---+---")

# Todas las posibles combinaciones ganadoras (3 en línea en 3D)
def lineas_ganadoras():
    lineas = []

    # Filas y columnas en cada nivel
    for z in range(3):
        for y in range(3):
            lineas.append([(z, y, x) for x in range(3)])  # filas
        for x in range(3):
            lineas.append([(z, y, x) for y in range(3)])  # columnas
        # Diagonales en cada nivel
        lineas.append([(z, i, i) for i in range(3)])
        lineas.append([(z, i, 2-i) for i in range(3)])

    # Verticales entre niveles
    for y in range(3):
        for x in range(3):
            lineas.append([(z, y, x) for z in range(3)])

    # Diagonales a través de niveles (en cada fila/columna)
    for i in range(3):
        lineas.append([(z, i, z) for z in range(3)])
        lineas.append([(z, i, 2-z) for z in range(3)])
        lineas.append([(z, z, i) for z in range(3)])
        lineas.append([(z, 2-z, i) for z in range(3)])

    # Diagonales principales del cubo
    lineas.append([(i, i, i) for i in range(3)])
    lineas.append([(i, i, 2-i) for i in range(3)])
    lineas.append([(i, 2-i, i) for i in range(3)])
    lineas.append([(i, 2-i, 2-i) for i in range(3)])

    return lineas

GANADORAS = lineas_ganadoras()

def hay_ganador(tablero):
    for linea in GANADORAS:
        valores = [tablero[z][y][x] for z,y,x in linea]
        if valores[0] != " " and all(v == valores[0] for v in valores):
            return valores[0]
    return None

def tablero_lleno(tablero):
    return all(tablero[z][y][x] != " " for z,y,x in itertools.product(range(3), repeat=3))

def jugar():
    tablero = crear_tablero()
    jugador = "X"

    while True:
        mostrar_tablero(tablero)
        print(f"\nTurno de {jugador}")
        try:
            z = int(input("Nivel (0-2): "))
            y = int(input("Fila (0-2): "))
            x = int(input("Columna (0-2): "))
        except ValueError:
            print("Entrada inválida, intenta otra vez.")
            continue

        if not (0 <= z < 3 and 0 <= y < 3 and 0 <= x < 3):
            print("Coordenadas fuera de rango.")
            continue

        if tablero[z][y][x] != " ":
            print("Casilla ocupada, intenta otra vez.")
            continue

        tablero[z][y][x] = jugador

        ganador = hay_ganador(tablero)
        if ganador:
            mostrar_tablero(tablero)
            print(f"\n¡Gana {ganador}!")
            break
        if tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("\nEmpate.")
            break
jugar()