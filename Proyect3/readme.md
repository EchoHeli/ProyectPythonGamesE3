El juego del ahorcado es un clásico de los juegos de palabras. Consiste en adivinar una palabra oculta, letra por letra, antes de que se complete el dibujo del ahorcado. Este proyecto es interesante porque:

Permite practicar estructuras básicas de programación en Python como condicionales, bucles, listas y cadenas.
Desarrolla la lógica de control de flujo al manejar intentos, letras correctas e incorrectas.
Se presta para añadir mejoras creativas.

Algoritmo del proyecto:

1.-Seleccionar una palabra secreta de una lista de palabras predefinida.

2.-Inicializar las variables:    

-Lista de letras adivinadas.

-Número máximo de intentos.

3.-Mostrar al usuario la palabra oculta con guiones bajos por cada letra no adivinada.

4.-Mientras queden intentos y no se haya adivinado la palabra:

-Pedir al usuario que ingrese una letra.

-Verificar si la letra está en la palabra secreta.

Si está, mostrarla en su posición correspondiente.

Si no está, reducir el número de intentos restantes y actualizar el dibujo del ahorcado.

Mostrar las letras ya utilizadas y los intentos restantes.

5.-Si el usuario adivinó la palabra completa antes de quedarse sin intentos:

-Mostrar mensaje de “¡Ganaste!”.

6.-Si el usuario se queda sin intentos:

-Mostrar mensaje de “¡Perdiste!” y revelar la palabra.


