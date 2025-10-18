
import random
import time

def generar_matriz_cartas(num_pares):
    """
    Genera una matriz (lista de listas) de cartas con pares duplicados y mezclados.
    Cada fila contiene 4 cartas para representar un tablero de 2D.

    """
    letras = [chr(65 + i) for i in range(num_pares)]  # ['A', 'B', 'C', ...]
    cartas = letras * 2
    random.shuffle(cartas)

    filas = (num_pares * 2) // 4
    matriz = []
    for i in range(filas):
        matriz.append(cartas[i * 4:(i + 1) * 4])
    return matriz


def crear_matriz_visibilidad(matriz):
    """
    Crea una matriz booleana de visibilidad del mismo tamaño que la matriz de cartas.
    False = carta oculta, True = carta descubierta.
    """
    return [[False for _ in fila] for fila in matriz]


def mostrar_tablero(matriz_cartas, matriz_visibles):
    """
    Muestra el tablero actual del juego en consola.
    Las cartas ocultas se muestran como números de posición (01, 02...).
    
    """
    print("\nTablero actual:")
    contador = 1
    for i in range(len(matriz_cartas)):
        for j in range(len(matriz_cartas[i])):
            if matriz_visibles[i][j]:
                print(f" {matriz_cartas[i][j]} ", end="")
            else:
                print(f"{contador:02d} ", end="")
            contador += 1
        print()
    print()


def obtener_coordenadas(posicion, matriz):
    """
    Convierte una posición lineal (ej. 5) en coordenadas (fila, columna) dentro de la matriz.
    Ejemplo: posición 5 → (1, 0) en una matriz de 4 columnas.
    """
    columnas = len(matriz[0])
    fila = (posicion - 1) // columnas
    columna = (posicion - 1) % columnas
    return fila, columna


def guardar_resultado(nombre, pares, intentos, tiempo):
    """
    Guarda los resultados del jugador en un archivo de texto.
    Cada línea contiene: nombre, pares, intentos, tiempo.
    """
    with open("resultados_memorama.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{pares},{intentos},{tiempo}\n")
    print(" Resultado guardado en resultados_memorama.txt")


def ver_resultados():
    """
    Muestra los resultados guardados de partidas anteriores.
    Si no existe el archivo, muestra un mensaje de advertencia.
    """
    try:
        with open("resultados_memorama.txt", "r", encoding="utf-8") as archivo:
            print("\n=== HISTORIAL DE PARTIDAS ===")
            for linea in archivo:
                nombre, pares, intentos, tiempo = linea.strip().split(",")
                print(f"Jugador: {nombre} | Pares: {pares} | Intentos: {intentos} | Tiempo: {tiempo}s")
    except FileNotFoundError:
        print("No hay resultados guardados todavía.")


def jugar():
    """
    Función principal del juego.
    Permite al jugador descubrir pares de cartas iguales dentro de una matriz.
    (Demuestra uso de ciclos while, condicionales, listas, matrices y archivos)
    """
    print("\n=== JUEGO DE MEMORIA ===")
    nombre = input("Ingresa tu nombre: ")
# Elección de dificultad
    while True:
        try:
            num_pares = int(input("Elige número de pares (4-10): "))
            if 4 <= num_pares <= 10:
                break
            else:
                print(" Ingresa un número entre 4 y 10.")
        except ValueError:
            print(" Ingresa un número válido.")

    matriz_cartas = generar_matriz_cartas(num_pares)
    matriz_visibles = crear_matriz_visibilidad(matriz_cartas)
    aciertos = 0
    intentos = 0
    inicio = time.time()

    while aciertos < num_pares:
        mostrar_tablero(matriz_cartas, matriz_visibles)

        try:
            pos1 = int(input("Selecciona la primera carta: "))
            pos2 = int(input("Selecciona la segunda carta: "))
            total_cartas = len(matriz_cartas) * len(matriz_cartas[0])

            if pos1 == pos2 or not (1 <= pos1 <= total_cartas) or not (1 <= pos2 <= total_cartas):
                print("Selección no válida.")
                continue

            fila1, col1 = obtener_coordenadas(pos1, matriz_cartas)
            fila2, col2 = obtener_coordenadas(pos2, matriz_cartas)

            if matriz_visibles[fila1][col1] or matriz_visibles[fila2][col2]:
                print(" Una o ambas cartas ya están descubiertas.")
                continue

            matriz_visibles[fila1][col1] = True
            matriz_visibles[fila2][col2] = True
            mostrar_tablero(matriz_cartas, matriz_visibles)
            intentos += 1

            if matriz_cartas[fila1][col1] == matriz_cartas[fila2][col2]:
                print(" ¡Par encontrado!\n")
                aciertos += 1
            else:
                print(" No coinciden.")
                time.sleep(1.2)
                matriz_visibles[fila1][col1] = False
                matriz_visibles[fila2][col2] = False

        except ValueError:
            print(" Ingresa un número válido.")

    fin = time.time()
    duracion = round(fin - inicio, 2)
    print(f"\n ¡Felicidades, {nombre}! Encontraste todos los pares en {intentos} intentos y {duracion} segundos.\n")
    guardar_resultado(nombre, num_pares, intentos, duracion)


def pruebas():
    """
    Ejecuta pruebas para verificar el funcionamiento de las funciones principales.
    Incluye casos límite y validaciones básicas.
    """
    print("\n=== PRUEBAS AUTOMÁTICAS ===")

    # Prueba 1: generar_matriz_cartas
    matriz = generar_matriz_cartas(4)
    assert isinstance(matriz, list), "Error: la matriz debe ser una lista."
    assert len(matriz) > 0, "Error: matriz vacía."
    print(" Prueba 1 (generar_matriz_cartas) exitosa.")

    # Prueba 2: crear_matriz_visibilidad
    visibles = crear_matriz_visibilidad(matriz)
    assert all(not val for fila in visibles for val in fila), "Error: todas las cartas deben empezar ocultas."
    print("Prueba 2 (crear_matriz_visibilidad) exitosa.")

    # Prueba 3: obtener_coordenadas
    f, c = obtener_coordenadas(1, matriz)
    assert (f, c) == (0, 0), "Error: coordenadas incorrectas para posición 1."
    print(" Prueba 3 (obtener_coordenadas) exitosa.")

    # Prueba 4: guardar_resultado
    guardar_resultado("Test", 4, 6, 12.5)
    with open("resultados_memorama.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    assert "Test" in contenido, "Error: el resultado no se guardó correctamente."
    print(" Prueba 4 (guardar_resultado) exitosa.")

    print(" Todas las pruebas fueron exitosas.\n")


def menu():
    """
    Muestra el menú principal y controla el flujo del programa.
    
    """
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Jugar")
        print("2. Ver resultados")
        print("3. Ejecutar pruebas")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            jugar()
        elif opcion == "2":
            ver_resultados()
        elif opcion == "3":
            pruebas()
        elif opcion == "4":
            print(" ¡Gracias por jugar Memorama!")
            break
        else:
            print(" Opción inválida. Intenta de nuevo.")


# Ejecutar programa
if __name__ == "__main__":
    menu()
