from Piedra_Papel_Tijera import juegoppt
from Ahorcado import jugar_ahorcado
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
                    Ahorcado.main()
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
            snake.main()
            break
        elif opt == 4:
            Tic_Tac_Toe.jugar()
            break
        else:
            print("Opción incorrecta, intente de nuevo\n")

main()  
