﻿Para este proyecto, decidí realizar un juego de piedra papel o tijera en python que le diera la opción al usuario de jugar 2 modos de juego:

- Modo normal: El programa le pediría al usuario entre piedra papel o tijera, después el programa elegiría una de las 3 opciones aleatoriamente y se elegirá el ganador en base a las respuestas. El usuario tendría la opción de elegir cuantas veces quisiera jugar (Con que sea número impar para que solo hubiera un ganador) y el que gane más partidas ganaría la serie (Si solo hay empates, la serie se clasifica como empate), después se le preguntaría si quiere jugar otra vez o no.
- Modo difícil: En este modo, el programa pondría a prueba la teoría de que si un jugador gana una partida, es muy probable que seleccione la misma opción, y que si uno pierde, cambie a la siguiente opción de piedra papel tijera (Ejemplo: Si un jugador gana con piedra, es probable que juegue piedra otra vez y si un jugador pierde con piedra, es más probable que juegue papel la siguiente ronda según el orden de piedra papel tijera.) El programa analizará la jugada anterior que hizo su oponente y ajustará su estrategia basado en esto. El usuario tendría la opción de elegir cuantas veces quisiera jugar (3 o más porque debe de haber repeticiones contra el mismo jugador para que la teoría aplique, número impar) y el que gane más partidas ganaría la serie (Si solo hay empates, la serie se clasifica como empate), después se le preguntaría si quiere jugar otra vez o no.

El usuario no puede tener conocimiento previo sobre cómo funciona el programa ya que fácilmente puede ganar sabiendo que va a seleccionar el programa. Creo que es sumamente interesante realizar este programa porque nos puede decir si en realidad esta teoría funciona o no.

La otra opción es un modo con 5 opciónes en vez de 3 llamado "Piedra Papel Tijera Lagarto Spock" donde hay más interacciónes que considerar entre los jugadores.

Algoritmo general:
1. El codigo imprime el menu con las opciones y pregunta que modo quiere jugar
2. Si el jugador quiere jugar piedra papel tijera normal:
    2.1 El codigo pregunta cuantos juegos quiere jugar en la serie (Impar)
    2.2 El codigo 
