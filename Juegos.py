from Piedra_Papel_Tijera import juegoppt
import Juegoahorcado
import Snake
import Tic_Tac_Toe

def menu():
    print("""Elige que juego quieres jugar:
1. Ahorcado
2. Piedra Papel Tijera
3. Snake
4. Tic Tac Toe""")
    
def main():
    while True:
        menu()
        opt = int(input(""))
        if opt == 1:
            opt2 = input("Caso de prueba? (y/n): ")
            opt2 = opt2.lower()
            while True:
                if opt2 == "n":
                    Juegoahorcado.main()
                    
                    loop = input("¿Desea volver al menu principal? (y/n): ")
                    loop = lopp.lower()
                    if loop =="y":
                        continue
                    else:
                        print("Gracias por jugar!")
                        break
                else:
                    print("Opción incorrecta, intente de nuevo\n")
                    break
        elif opt == 2:
            juegoppt.menuppt()
            opt = int(input(""))
            while True:
                if opt == 1:
                        n = int(input("Ingrese cuantos juegos quiere jugar en la serie (Impar): "))
                        if n % 2 != 0:
                                juegoppt.ppt(n)
                                break
                        else: 
                                print("El numero de juegos en la serie debe de ser impar, intente de nuevo\n")
                elif opt == 2:
                        n = int(input("Ingrese cuantos juegos quiere jugar en la serie (Impar): "))
                        if n % 2 != 0:
                                juegoppt.pptdificil(n)
                                break
                        else: 
                                print("El numero de juegos en la serie debe de ser impar, intente de nuevo\n") 
                elif opt == 3:
                        n = int(input("Ingrese cuantos juegos quiere jugar en la serie (Impar): "))
                        if n % 2 != 0:
                                juegoppt.pptls(n)
                                break
                        else: 
                                print("El numero de juegos en la serie debe de ser impar, intente de nuevo\n") 
                else:
                        print("Opción invalida, intente de nuevo")
            break
        elif opt == 3:
                instructions_snake()
            
                # Modo de dificultad
                dificultad = input("¿Qué nivel te gustaría jugar? (Fácil / Media / Difícil): ")
                dificultad = dificultad.lower ()
                alto, ancho = seleccionar_dificultad(dificultad)
            
                snake = [[alto // 2, ancho // 2]]
                direccion = 'd'
                puntos = 0
                manzana = nueva_manzana(alto, ancho, snake)
            
                limpiar_pantalla()
                mostrar_tablero(ancho, alto, snake, manzana, puntos)
            
                while True:
                    entrada = input("Dirección y pasos (ej. w 3): ").split()
            
                    if len(entrada) != 2 or entrada[0] not in ('w', 'a', 's', 'd') or not entrada[1].isdigit():
                        print("Entrada inválida. Usa formato: dirección pasos (ej. d 4)")
                        continue
            
                    direccion = entrada[0]
                    pasos = int(entrada[1])
            
                    for _ in range(pasos):  # Numero de espacios que el usuario quiera moverse
                        nueva_cabeza = mover(direccion, snake[0])
            
                        if (nueva_cabeza in snake or  # Te comiste a ti mismo
                                nueva_cabeza[0] < 0 or nueva_cabeza[0] >= alto or  # Te saliste del tablero (arriba y abajo)
                                nueva_cabeza[1] < 0 or nueva_cabeza[1] >= ancho):  # Te saliste del tablero (izquierda y derecha)
                            print("Ups. Tu serpiente ha chocado :(")
                            print(f"Puntaje final: {puntos}")
                            print("Game Over")
                            return
            
                        snake.insert(0, nueva_cabeza)  # Agrega nuevo valor "-" a la lista de snake
            
                        if nueva_cabeza == manzana:  # Cabeza y manzana en la mismas cordenadas
                            puntos += 1
                            print("Ñomi, has comido una manzana :P ")
                            print("¡Ganaste un punto!")
                            time.sleep(2)
                            manzana = nueva_manzana(alto, ancho, snake)  # Se aparece nueva manzana y crece la serpientee
                        else:
                            snake.pop()  # Elimina la ultima parte de la lista ... quita el nuevo cuerpo de la serpiente, pq no comió
                    if len(snake) == alto * ancho:
                        print("¡Felicidades! Has llenado todo el tablero :D")
                        print("¡Winer!")
                        print(f"Puntaje final: {puntos}")
                        return
                    limpiar_pantalla()
                    mostrar_tablero(ancho, alto, snake, manzana, puntos)
                    time.sleep(0.1)  # Pausa el programa antes de su ejecucción, para que no se confunda el usuario         
                
        elif opt == 4:
            Tic_Tac_Toe.jugar()
            break
        else:
            print("Opción incorrecta, intente de nuevo\n")

main()  
