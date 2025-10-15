import random

# --- Datos del juego ---
PALABRAS = {
    "facil": ["sol", "luna", "casa", "gato", "perro", "arbol"],
    "medio": ["python", "computadora", "monitor", "raton", "teclado"],
    "dificil": ["programacion", "algoritmo", "desarrollador", "software", "inteligencia"]
}

# --- Funciones auxiliares ---
def seleccionar_palabra(nivel):
    """
    Selecciona una palabra al azar según el nivel de dificultad.
    """
    return random.choice(PALABRAS[nivel])

def mostrar_progreso(palabra, letras_adivinadas):
    """
    Muestra las letras adivinadas y guiones bajos para las letras restantes.
    """
    return " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

def validar_entrada(letra, letras_adivinadas, letras_incorrectas):
    """
    Valida la letra ingresada por el usuario.
    Retorna:
        "valida" si es una letra nueva
        "repetida" si ya fue intentada
        "no_valida" si no es una letra
    """
    if len(letra) != 1 or not letra.isalpha():
        return "no_valida"
    elif letra in letras_adivinadas or letra in letras_incorrectas:
        return "repetida"
    else:
        return "valida"

def obtener_letra():
    """
    Solicita al usuario ingresar una letra.
    """
    return input("Ingresa una letra: ").strip().lower()

def seleccionar_nivel():
    """
    Permite al usuario seleccionar el nivel de dificultad.
    """
    while True:
        nivel = input("Selecciona nivel (facil/medio/dificil): ").strip().lower()
        if nivel in PALABRAS:
            return nivel
        else:
            print("Nivel inválido. Intenta de nuevo.")

# --- Función principal del juego ---
def jugar_ahorcado():
    print("¡Bienvenido al Ahorcado Avanzado!")
    nivel = seleccionar_nivel()

    # Definir intentos según nivel
    intentos_restantes = {"facil": 8, "medio": 6, "dificil": 4}[nivel]

    palabra = seleccionar_palabra(nivel)
    letras_adivinadas = []
    letras_incorrectas = []

    while intentos_restantes > 0:
        print("\nPalabra:", mostrar_progreso(palabra, letras_adivinadas))
        print("Intentos restantes:", intentos_restantes)

        if letras_incorrectas:
            print("Letras incorrectas:", ", ".join(letras_incorrectas))

        letra = obtener_letra()
        estado = validar_entrada(letra, letras_adivinadas, letras_incorrectas)

        if estado == "no_valida":
            print("Entrada no válida. Ingresa solo una letra.")
            continue
        elif estado == "repetida":
            print("Ya intentaste con esa letra. Intenta otra.")
            continue

        if letra in palabra:
            letras_adivinadas.append(letra)
            print("¡Bien! La letra está en la palabra.")
            if all(l in letras_adivinadas for l in palabra):
                print("\n¡Felicidades! Adivinaste la palabra:", palabra)
                return
        else:
            letras_incorrectas.append(letra)
            intentos_restantes -= 1
            print("La letra no está en la palabra.")

    print("\nTe quedaste sin intentos. La palabra era:", palabra)

# --- Función main() definida solo para llamar desde el main general ---
def main():
    jugar_ahorcado()
