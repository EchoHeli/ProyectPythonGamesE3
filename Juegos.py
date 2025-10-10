import Piedra_Papel_Tijera
from ahorcado import jugar_ahorcado
from Snake import snake
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
            Piedra_Papel_Tijera.mainppt()
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
