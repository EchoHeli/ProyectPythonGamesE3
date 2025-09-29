import juegoppt
import juegoahorcado
import snake
import TictactoeGames

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
                if opt2 == "y":
                    juegoahorcado.pruebas()
                    break
                elif opt2 == "n":
                    juegoahorcado.main()
                    break
                else:
                    print("Opción incorrecta, intente de nuevo\n")
            break
        elif opt == 2:
            juegoppt.mainppt()
            break
        elif opt == 3:
            snake.main()
            break
        elif opt == 4:
            TictactoeGames.jugar()
            break
        else:
            print("Opción incorrecta, intente de nuevo\n")

main()  
