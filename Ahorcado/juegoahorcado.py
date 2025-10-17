import random

#Datos del juego
PALABRAS = {
    "facil": ["sol", "luna", "casa", "gato", "perro", "arbol"],
    "medio": ["python", "computadora", "monitor", "raton", "teclado"],
    "dificil": ["programacion", "algoritmo", "desarrollador", "software", "inteligencia"]
}

# Funciones auxiliares
def seleccionar_palabra(nivel):
    return random.choice(PALABRAS[nivel])

def mostrar_progreso(palabra, letras_adivinadas):
    return " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

def validar_entrada(letra, letras_adivinadas, letras_incorrectas):
    if len(letra) != 1 or not letra.isalpha():
        return "no_valida"
    elif letra in letras_adivinadas or letra in letras_incorrectas:
        return "repetida"
    else:
        return "valida"

def obtener_letra():
    return input("Ingresa una letra: ").strip().lower()

def seleccionar_nivel():
    while True:
        nivel = input("Selecciona nivel (facil/medio/dificil): ").strip().lower()
        if nivel in PALABRAS:
            return nivel
        else:
            print("Nivel inválido. Intenta de nuevo.")

#Funciones con archivos
def mostrar_registro():
    """
    Muestra el contenido del archivo registro.txt (si tiene información).
    """
    archivo = open("registro.txt", "r")   # Abre el archivo en modo lectura
    contenido = archivo.read()
    if len(contenido) > 0:
        print("Palabras no adivinadas anteriormente:")
        print(contenido)
    else:
        print("El archivo de registro está vacío.")
    archivo.close()

def guardar_palabra_no_adivinada(palabra):
    """
    Guarda la palabra no adivinada en un archivo de texto.
    """
    archivo = open("registro.txt", "a")   # Abre en modo agregar
    archivo.write(palabra + "\n")
    archivo.close()

# Función principal del juego
def jugar_ahorcado():
    print("¡Bienvenido al Ahorcado con archivo de registro!")

    # Mostrar registro (si ya existe)
    print("\nIntentando abrir el archivo 'registro.txt'...\n")
    archivo = open("registro.txt", "a+")  # Modo lectura y escritura (crea si no existe)
    archivo.seek(0)                      
    contenido = archivo.read()
    if len(contenido) > 0:
        print("Palabras no adivinadas anteriormente:")
        print(contenido)
    else:
        print("No hay palabras registradas aún.")
    archivo.close()

    # Lógica del juego 
    nivel = seleccionar_nivel()
    intentos_restantes = {"facil": 8, "medio": 6, "dificil": 4}[nivel]
    palabra = seleccionar_palabra(nivel)
    letras_adivinadas = []
    letras_incorrectas = []

    while intentos_restantes > 0:
        print("\nPalabra:", mostrar_progreso(palabra, letras_adivinadas))
        print("Intentos restantes:", intentos_restantes)

        if len(letras_incorrectas) > 0:
            print("Letras incorrectas:", end=" ")
            for letra in letras_incorrectas:
                print(letra, end=" ")
            print()  # salto de línea al final

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
                print("¡Felicidades! Adivinaste la palabra:", palabra)
                return
        else:
            letras_incorrectas.append(letra)
            intentos_restantes -= 1
            print("La letra no está en la palabra.")

    print(" Te quedaste sin intentos. La palabra era:", palabra)
    print("Guardando palabra en registro.txt...")
    guardar_palabra_no_adivinada(palabra)
    print("Palabra guardada exitosamente.")

# Función main()
def main():
    jugar_ahorcado()
