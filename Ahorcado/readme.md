Proyecto: Juego del Ahorcado

Para este proyecto, decidí realizar un juego del Ahorcado en Python, donde el usuario puede seleccionar entre tres niveles de dificultad: fácil, medio y difícil.
Dependiendo del nivel elegido, el programa seleccionará una palabra secreta diferente y determinará la cantidad de intentos permitidos para adivinarla.

En el nivel fácil, las palabras son cortas y el jugador cuenta con más intentos para ganar.
En el nivel medio, las palabras son más largas y se reducen los intentos.
En el nivel difícil, las palabras son más complejas y los intentos son mucho más limitados.

El juego consiste en que el jugador debe ir adivinando las letras de una palabra oculta. En cada turno, el programa muestra el progreso de la palabra (revelando las letras adivinadas y reemplazando las demás con guiones bajos). Si el jugador ingresa una letra correcta, esta se muestra en su posición correspondiente. Si no, el número de intentos restantes disminuye.

El jugador gana si logra adivinar todas las letras antes de quedarse sin intentos. En caso contrario, pierde y el programa muestra la palabra completa.
Este proyecto es interesante porque permite aplicar estructuras de control, listas, validaciones y modularización del código, al mismo tiempo que resulta divertido y sencillo de extender dentro de un main general que contenga otros juegos.

Algoritmo general:

El programa imprime un mensaje de bienvenida y muestra las opciones de dificultad disponibles (fácil, medio o difícil).

El usuario selecciona el nivel de dificultad:
2.1 Si elige fácil, las palabras serán cortas y tendrá 8 intentos.
2.2 Si elige medio, las palabras tendrán una longitud media y dispondrá de 6 intentos.
2.3 Si elige difícil, las palabras serán largas o complejas y contará con 4 intentos.

El programa selecciona una palabra secreta al azar de la lista correspondiente al nivel elegido.

Se inicializan dos listas vacías:

Una para las letras adivinadas.

Otra para las letras incorrectas.

Mientras queden intentos:
5.1 El programa muestra el progreso de la palabra con guiones para las letras faltantes.
5.2 Indica cuántos intentos le quedan al jugador.
5.3 Si hay letras incorrectas, las muestra para que el usuario no las repita.
5.4 El usuario ingresa una letra.
5.5 El programa valida la entrada:
- Si no es una letra, muestra un mensaje de error.
- Si la letra ya fue usada, avisa que es repetida.
5.6 Si la letra está en la palabra secreta:
- Se añade a la lista de letras adivinadas.
- Se muestra el mensaje “¡Bien! La letra está en la palabra.”
- Si ya se adivinaron todas las letras, el jugador gana y el juego termina.
5.7 Si la letra no está en la palabra:
- Se añade a la lista de letras incorrectas.
- Se descuenta un intento.
- Se muestra el mensaje “La letra no está en la palabra.”

Si el jugador se queda sin intentos, el juego termina mostrando el mensaje:
“Te quedaste sin intentos. La palabra era: [palabra secreta]”.
