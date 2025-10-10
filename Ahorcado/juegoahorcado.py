import random

# Función para seleccionar una palabra secreta de manera aleatoria
def seleccionar_palabra():
    """
    Selecciona y devuelve una palabra secreta al azar de una lista ampliada.
    """
    palabras = [
        "python", "programacion", "ahorcado", "juego", "computadora",
        "comer", "teclado", "raton", "monitor", "internet",
        "variable", "funcion", "algoritmo", "desarrollador", "software"
    ]
    return random.choice(palabras)

# Función para mostrar el progreso del jugador
def mostrar_progreso(palabra_secreta, letras_adivinadas):
    """
    Devuelve la palabra secreta con guiones bajos en lugar de las letras
    que aún no han sido adivinadas.
    """
    progreso = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            progreso += letra + " "
        else:
            progreso += "_ "
    return progreso.strip()

# Función para validar la entrada del usuario
def validar_entrada(letra, letras_adivinadas):
    """
    Valida que la letra ingresada sea correcta:
    - Solo una letra
    - No repetida
    - Letra del alfabeto
    """
    if len(letra) != 1 or not letra.isalpha():
        return "no_valida"
    elif letra in letras_adivinadas:
        return "repetida"
    else:
        return "valida"

# Función principal del juego
def jugar_ahorcado():
    """
    Controla el flujo principal del juego del ahorcado.
    """
    palabra = seleccionar_palabra()
    letras_adivinadas = []
    intentos_restantes = 6
    print("Bienvenido al juego del Ahorcado")

    while intentos_restantes > 0:
        print("\nPalabra:", mostrar_progreso(palabra, letras_adivinadas))
        print("Intentos restantes:", intentos_restantes)
        letra = input("Ingresa una letra: ").lower()
        estado = validar_entrada(letra, letras_adivinadas)

        if estado == "no_valida":
            print("Entrada no válida. Ingresa solo una letra.")
            continue
        elif estado == "repetida":
            print("Ya intentaste con esa letra. Intenta otra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            print("¡Bien! La letra está en la palabra.")
            if all(l in letras_adivinadas for l in palabra):
                print("\n¡Felicidades! Adivinaste la palabra:", palabra)
                return
        else:
            intentos_restantes -= 1
            print("La letra no está en la palabra.")

    print("\nTe quedaste sin intentos. La palabra era:", palabra)

# Función de pruebas para verificar cada función del juego
def pruebas():
    """
    Realiza pruebas de las funciones para verificar su correcto funcionamiento.
    """
    print("Pruebas de seleccionar_palabra():")
    palabra = seleccionar_palabra()
    assert palabra in [
        "python", "programacion", "ahorcado", "juego", "computadora",
        "comer", "teclado", "raton", "monitor", "internet",
        "variable", "funcion", "algoritmo", "desarrollador", "software"
    ], "Error: palabra no válida"
    print("✓ seleccionar_palabra funciona correctamente.")

    print("\nPruebas de mostrar_progreso():")
    assert mostrar_progreso("python", ["p", "y"]) == "p y _ _ _ _", "Error en mostrar_progreso"
    assert mostrar_progreso("juego", []) == "_ _ _ _ _", "Error en mostrar_progreso"
    print("✓ mostrar_progreso funciona correctamente.")

    print("\nPruebas de validar_entrada():")
    assert validar_entrada("a", []) == "valida", "Error en validar_entrada"
    assert validar_entrada("aa", []) == "no_valida", "Error en validar_entrada"
    assert validar_entrada("1", []) == "no_valida", "Error en validar_entrada"
    assert validar_entrada("a", ["a"]) == "repetida", "Error en validar_entrada"
    print("✓ validar_entrada funciona correctamente.")

# Ejecutar pruebas (descomentar la siguiente línea para probar)
# pruebas()

# Ejecutar el juego
if __name__ == "__main__":
    jugar_ahorcado()
