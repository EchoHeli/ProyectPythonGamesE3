Proyecto: Juego de Memorama

Para este proyecto, decidí realizar un juego de Memorama en Python, donde el usuario puede descubrir pares de cartas iguales dentro de un tablero aleatorio. El objetivo del juego es encontrar todos los pares en el menor número de intentos posibles, poniendo a prueba la memoria y concentración del jugador.

El programa permite al usuario ingresar su nombre, seleccionar el nivel de dificultad (definido por la cantidad de pares) y jugar de manera interactiva desde consola. Además, guarda automáticamente los resultados de cada partida en un archivo de texto, para que el jugador pueda revisar su progreso en futuras sesiones.

El juego genera una matriz de cartas (por ejemplo, 4x4 o 5x4 según el nivel) donde cada par está representado por letras iguales (A, B, C...). El jugador selecciona dos posiciones por turno (indicadas con números) para intentar encontrar un par igual.

Si las cartas coinciden, permanecen descubiertas. Si no coinciden, se vuelven a ocultar. El juego continúa hasta que todos los pares se han encontrado. Al finalizar, el programa muestra un resumen con el nombre del jugador, el número de intentos y el tiempo total que tardó. Finalmente, los resultados se guardan en el archivo resultados_memorama.txt.

El programa imprime un mensaje de bienvenida y pide el nombre del jugador.

Muestra un menú con cuatro opciones principales:

Jugar

Ver resultados anteriores

Ejecutar pruebas automáticas

Salir del programa

Si el usuario elige Jugar:
a) Se le pide elegir la cantidad de pares (entre 4 y 10).
b) Se genera aleatoriamente una matriz de cartas con esos pares.
c) Se inicializa una matriz paralela de visibilidad, que indica si las cartas están ocultas o descubiertas.
d) El programa muestra el tablero con las posiciones numeradas.
e) El jugador elige dos posiciones:

Si las cartas son iguales, se descubren de forma permanente.

Si no son iguales, se ocultan después de una breve pausa.
f) Se incrementa el contador de intentos.
g) El ciclo continúa hasta que todos los pares han sido descubiertos.

Cuando el jugador termina:

El programa muestra el número total de intentos y el tiempo transcurrido.

Los datos se guardan en el archivo resultados_memorama.txt con el formato: nombre, pares, intentos, tiempo.

Si el usuario elige Ver resultados, se leen y muestran todas las partidas anteriores desde el archivo de texto.

Si el usuario selecciona Ejecutar pruebas, se llama a la función pruebas(), que valida automáticamente:

La generación correcta del tablero.

La visibilidad inicial de las cartas.

El cálculo de coordenadas.

El guardado exitoso de resultados.

Si el usuario elige Salir, el programa termina con un mensaje de despedida.
