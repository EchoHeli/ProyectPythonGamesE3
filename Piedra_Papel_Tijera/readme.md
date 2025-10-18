Para este proyecto, decidí realizar un juego de piedra papel o tijera en python que le diera la opción al usuario de jugar 2 modos de juego:

- Modo normal: El programa le pediría al usuario entre piedra papel o tijera, después el programa elegiría una de las 3 opciones aleatoriamente y se elegirá el ganador en base a las respuestas. El usuario tendría la opción de elegir cuantas veces quisiera jugar (Con que sea número impar para que solo hubiera un ganador) y el que gane más partidas ganaría la serie (Si solo hay empates, la serie se clasifica como empate), después se le preguntaría si quiere jugar otra vez o no.
- Modo difícil: En este modo, el programa pondría a prueba la teoría de que si un jugador gana una partida, es muy probable que seleccione la misma opción, y que si uno pierde, cambie a la siguiente opción de piedra papel tijera (Ejemplo: Si un jugador gana con piedra, es probable que juegue piedra otra vez y si un jugador pierde con piedra, es más probable que juegue papel la siguiente ronda según el orden de piedra papel tijera.) El programa analizará la jugada anterior que hizo su oponente y ajustará su estrategia basado en esto. El usuario tendría la opción de elegir cuantas veces quisiera jugar (3 o más porque debe de haber repeticiones contra el mismo jugador para que la teoría aplique, número impar) y el que gane más partidas ganaría la serie (Si solo hay empates, la serie se clasifica como empate), después se le preguntaría si quiere jugar otra vez o no.
-PPTLS: La otra opción es un modo con 5 opciones en vez de 3 llamado "Piedra Papel Tijera Lagarto Spock" donde hay más interacciones que considerar entre los jugadores.
El usuario no puede tener conocimiento previo sobre cómo funciona el programa ya que fácilmente puede ganar sabiendo que va a seleccionar el programa. Creo que es sumamente interesante realizar este programa porque nos puede decir si en realidad esta teoría funciona o no.

Algoritmo general:
1. El código imprime el menú con las opciones y pregunta qué modo quiere jugar
2. Si el jugador quiere jugar piedra papel o tijera normal:
    2.1 El código pregunta cuantos juegos quiere jugar en la serie (Impar)
    2.2 Para todos los juegos de la serie:
       2.2.1 Le pide al usuario que elija Piedra, Papel o Tijera
       2.2.2 La computadora elige una opción aleatoriamente
       2.2.3 Se comparan las opciones y muestra si ganaste, perdiste, o empataron
    2.3 Se cuentan cuantos juegos ganaste, perdiste, y empataste y muestra el resultado de la serie
3. Si el jugador quiere jugar piedra papel o tijera difícil:
    3.1 El código pregunta cuantos juegos quiere jugar en la serie (Impar)
    3.2 Para el primer juego de la serie:
       3.2.1 Le pide al usuario que elija Piedra, Papel o Tijera
       3.2.2 La computadora elige una opción aleatoriamente
       3.2.3 Se comparan las opciones y muestra si ganaste, perdiste, o empataron
    3.3 Para todos los demás juegos:
        3.3.1 Le pide al usuario que elija Piedra, Papel o Tijera
        3.3.2 La computadora elige su opción basada en la predicción usando la teoría
        3.3.3 Se comparan las opciones y muestra si ganaste, perdiste, o empataron
    3.4 Se cuentan cuantos juegos ganaste, perdiste, y empataste y muestra el resultado de la serie
4. Si el jugador quiere jugar piedra papel tijera lagarto o spock:
    4.1 El código pregunta cuantos juegos quiere jugar en la serie (Impar)
    4.2 Para todos los juegos de la serie:
       4.2.1 Le pide al usuario que elija Piedra, Papel, Tijera, Lagarto, Spock
       4.2.2 La computadora elige una opción aleatoriamente
       4.2.3 Se comparan las opciones y muestra si ganaste, perdiste, o empataron
    4.3 Se cuentan cuantos juegos ganaste, perdiste, y empataste y muestra el resultado de la serie


