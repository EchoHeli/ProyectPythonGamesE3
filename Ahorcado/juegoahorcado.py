import random

def seleccionar_palabra():
    
    "Selecciona y devuelve una palabra secreta al azar de una lista."

    palabras = ["python", "programacion", "ahorcado", "juego", "computadora" , "comer"]
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta, letras_adivinadas):

    "Devuelve la palabra secreta con guiones bajos en lugar de las letras que aún no han sido adivinadas"
    progreso = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            progreso += letra + " "
        else:
            progreso += "_ "
    return progreso.strip()


def main():
    
    "Controla el flujo principal del juego del ahorcado."

    palabra = seleccionar_palabra()
    letras_adivinadas = []
    intentos_restantes = 6
    print("Bienvenido al juego del Ahorcado")

    while intentos_restantes > 0:
        print("\nPalabra:", mostrar_progreso(palabra, letras_adivinadas))
        print("Intentos restantes:", intentos_restantes)
        letra = input("Ingresa una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Entrada no válida. Ingresa solo una letra.")
            continue

        if letra in letras_adivinadas:
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


def pruebas():
    "Ejecuta pruebas de las funciones con casos límite."
    
    palabra = seleccionar_palabra()
    assert palabra in ["python", "programacion", "ahorcado", "juego", "computadora", "comer"]

    
    resultado = mostrar_progreso("python", [])
    assert resultado == "_ _ _ _ _ _"

    
    resultado = mostrar_progreso("python", ["p", "o"])
    assert resultado == "p _ _ _ o _"

    
    resultado = mostrar_progreso("juego", ["j", "u", "e", "g", "o"])
    assert resultado == "j u e g o"

    print("Todas las pruebas pasaron correctamente.")
