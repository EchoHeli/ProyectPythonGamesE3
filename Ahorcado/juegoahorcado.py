import random

# Función para seleccionar una palabra secreta
def seleccionar_palabra():
    palabras = [
        "python", "programacion", "ahorcado", "juego", "computadora",
        "comer", "teclado", "raton", "monitor", "internet",
        "variable", "funcion", "algoritmo", "desarrollador", "software"
    ]
    return random.choice(palabras)

# Función para mostrar el progreso del jugador
def mostrar_progreso(palabra_secreta, letras_adivinadas):
    progreso = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            progreso += letra + " "
        else:
            progreso += "_ "
    return progreso.strip()

# Función para validar la entrada del usuario
def validar_entrada(letra, letras_adivinadas):
    if len(letra) != 1 or not letra.isalpha():
        return "no_valida"
    elif letra in letras_adivinadas:
        return "repetida"
    else:
        return "valida"

# Función principal del juego del ahorcado
def jugar_ahorcado():
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
