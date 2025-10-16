El videojuego *Snake* es uno de los primeros juegos desarrollados para teléfonos móviles y ha existido desde hace poco más de 50 años. El juego es simple: el jugador controla una serpiente que se desplaza por un cuadrado y esta debe comer manzanas para crecer, pero no puede chocar contra las paredes del cuadrado o contra sí misma. Ganas cuando la serpiente abarque todo el cuadrado.

Escogimos el proyecto de los videojuegos porque representa una oportunidad para aplicar nuestros conocimientos de programación y aprender a pasar de la parte teórica a algo más práctico. Pudiendo desarrollar algo que sea más visual e interactivo para el usuario.

En particular, seleccioné *Snake* porque es un juego clásico que ha marcado la historia de los videojuegos Además, desarrollarlo me permitirá practicar temas como bucles, condicionales y toma de decisiones.Esto me ayudará a mejorar mi entendimiento en Python y el desarrollo de videojuegos en este.

Como se mencionó previamente, este proyecto se desarrollará utilizando Python



**Algoritmo**

INICIO

Muestra las instrucciones del juego

Pedir al usuario que escoga la dificultad (Fácil, Media o Difícil)
→ Según la dificultad, definir el tamaño del tablero

Colocamos la serpiente en el centro del tablero
Inicializamos la dirección en la derecha
Inicializamos el puntaje
Generar una manzana en una posición aleatoria en donde no este la serpiente

Limpiar pantalla
Mostrar el tablero con la serpiente, la manzana y los puntos

MIENTRAS el juego no ! == game over:
    Pedir al usuario una dirección y número de pasos (ej. w 3)

    SI la entrada no es válida:
        Mostrar mensaje de error

    Convertir la dirección y pasos a variables

    REPETIR hasta game over:
        Calcular la nueva posición de la cabeza de la serpiente
         Insertar la nueva cabeza al inicio de la lista de la serpiente

        SI la nueva cabeza está en la misma posición que la manzana:
            Aumentar puntos en 1
            Mostrar mensaje de que comió una manzana
            Generar una nueva manzana en una posición libre
        SINO:
            Eliminar la última parte del cuerpo de la serpiente (no crece)

        Limpiar pantalla
        Mostrar el tablero actualizado con la serpiente, la manzana y los puntos obtenidos

        SI la nueva posición está fuera del tablero o choca con el cuerpo:
            Mostrar mensaje de choque
            Mostrar puntaje final
            Terminar el juego

FIN
Slida:
Mensaje de game over y puntaje final


