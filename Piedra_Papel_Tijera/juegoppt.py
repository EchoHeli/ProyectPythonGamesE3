import random 
def comparacion(valorPlayer,valorComputer): # 1 piedra 2 papel 3 tijera 4 lagarto 5 spock, Se realiza la comparación entre el valor del jugador y el de la computadora
    if valorComputer == 1:
        if valorPlayer == "piedra":
                print("Usted escogió piedra, la computadora también, empate.\n")
                return(11)
        elif valorPlayer == "papel":
                print("Usted escogió papel, la computadora escogió piedra, victoria.\n")
                return(12)
        elif valorPlayer == "tijera":
                print("Usted escogió tijera, la computadora escogió piedra, derrota.\n")
                return(13)
        elif valorPlayer == "lagarto":
                print("Usted escogió lagarto, la computadora escogió piedra, derrota.\n")
                return(14)
        elif valorPlayer == "spock":
                print("Usted escogió spock, la computadora escogió piedra, victoria.\n")
                return(15)
    elif valorComputer == 2:
        if valorPlayer == "piedra":
                print("Usted escogió piedra, la computadora escogió papel, derrota.\n")
                return(21)
        elif valorPlayer == "papel":
                print("Usted escogió papel, la computadora tambien, empate.\n")
                return(22)
        elif valorPlayer == "tijera":
                print("Usted escogió tijera, la computadora escogió papel, victoria.\n")
                return(23)
        elif valorPlayer == "lagarto":
                print("Usted escogió lagarto, la computadora escogió papel, victoria\n")
                return(24)
        elif valorPlayer == "spock":
                print("Usted escogió spock, la computadora escogió papel, derrota\n")
                return(25)
    elif valorComputer == 3:
        if valorPlayer == "piedra":
                print("Usted escogió piedra, la computadora escogió tijera, victoria.\n")
                return(31)
        elif valorPlayer == "papel":
                print("Usted escogió papel, la computadora escogió tijera, derrota.\n")
                return(32)
        elif valorPlayer == "tijera":
                print("Usted escogió tijera, la computadora tambien, empate.\n")
                return(33)
        elif valorPlayer == "lagarto":
                print("Usted escogio lagarto, la computadora tijera, derrota.\n")
                return(34)
        elif valorPlayer == "spock":
                print("Usted escogió spock, la computadora tijera, victoria.\n")
                return(35)
    elif valorComputer == 4:
        if valorPlayer == "piedra":
                print("Usted escogió piedra, la computadora lagarto, victoria\n")
                return(41)
        elif valorPlayer == "papel":
                print("Usted escogió papel, la computadora lagarto, derrota.\n")
                return(42)
        elif valorPlayer == "tijera":
                print("Usted escogió tijera, la computadora lagarto, victoria.\n")
                return(43)
        elif valorPlayer == "lagarto":
                print("Usted escogió lagarto, la computadora tambien, empate.\n")
                return(44)
        elif valorPlayer == "spock":
                print("Usted escogió spock, la computadora lagarto, derrota.\n")
                return(45)
    elif valorComputer == 5:
            if valorPlayer == "piedra":
                print("Usted escogió piedra, la computadora spock, derrota.\n")
                return(51)
            elif valorPlayer == "papel":
                print("Usted escogió papel, la computadora spock, victoria.\n")
                return(52)
            elif valorPlayer == "tijera":
                print("Usted escogió tijera, la computadora spock, derrota.\n")
                return(53)
            elif valorPlayer == "lagarto":
                print("Usted escogió lagarto, la computadora spock, victoria.\n")
                return(54)
            elif valorPlayer == "spock":
                print("Usted escogió spock, la computadora tambien, empate.\n")
                return(55)
victoria = [12,23,31,15,24,35,41,43,52,54]
derrota = [21,32,13,14,25,34,42,45,51,53]
empate = [11,22,33,44,55]                
def comp2(result): # Función para la dificultad dificil que elige la jugada de la computadora en base a la jugada anterior del jugador
        if result in (12,21):
                        return 3
        elif result in (13,31):
                        return 2
        elif result in (23,32):
                        return 1
        elif result in (11,22,33):
                rand = random.randint(1,3)
                return rand
def vp(): # Función para pedir el valor al jugador
        valorPlayer = str(input("Elige Piedra, Papel, o Tijera: "))
        valorPlayer = valorPlayer.lower()
        valorPlayer = valorPlayer.replace(" ","")
        return(valorPlayer)

def vppptls(): # Función para pedir el valor al jugador en el modo lagarto spock
        valorPlayer = input("Elige Piedra, Papel, Tijera, Lagarto, Spock: ") 
        valorPlayer = valorPlayer.lower()
        valorPlayer = valorPlayer.replace(" ","")
        return(valorPlayer)

def resultSerie(player,computer,tie): # Función para mostrar el resultado final de la serie
        if player > computer:
                print(f"Usted ganó {player} juegos mientras que la computadora ganó {computer} juegos, ganó la serie!")
        elif computer > player:
                print(f"Usted ganó {player} juegos mientras que la computadora ganó {computer} juegos, perdió la serie!")
        elif player == computer:
                print(f"Usted y la computadora ganaron {player} juegos cada uno y empataron {tie} juegos de {tie+computer+player} juegos, empate!")
        else:
                print(f"Usted y la computadora empataron todos los juegos ({tie}) en la serie, empate!")

def ppt(n): # Función para el modo normal de piedra papel tijera
    computer = 0
    player = 0
    tie = 0
    for i in range (n):
        valorPlayer = ""
        computerRandom = random.randint(1,3)
        while valorPlayer not in ("piedra","papel","tijera"):
                valorPlayer = vp()
        result = comparacion(valorPlayer,computerRandom)
        if result in victoria:
                player += 1
        elif result in derrota:
                computer += 1
        elif result in empate:
                tie += 1
    resultSerie(player,computer,tie)

def pptdificil(n): # Función para el modo dificil de piedra papel tijera
        computer = 0
        player = 0
        tie = 0
        cont = 0
        computerRandom = random.randint(1,3)
        while player != 1 and computer != 1  and cont <= n:
                valorPlayer = ""
                while valorPlayer not in ("piedra","papel","tijera"):
                        valorPlayer = vp()
                        if valorPlayer in ("piedra","papel","tijera"):
                                break
                        else:
                                print("Opción incorrecta, intente de nuevo")
                result = comparacion(valorPlayer,computerRandom)
                if result in victoria:
                        player += 1
                        cont += 1
                elif result in derrota:
                        computer += 1
                        cont += 1
                elif result in empate:
                        tie += 1
                        cont += 1
        res = comp2(result)
        for i in range (cont,n):
                valorPlayer = ""
                while valorPlayer not in ("piedra","papel","tijera"):
                        valorPlayer = vp()
                        if valorPlayer in ("piedra","papel","tijera"):
                                break
                        else:
                                print("Opción incorrecta, intente de nuevo")
                resultdificil = comparacion(valorPlayer,res) 
                if resultdificil in victoria:
                       player += 1
                elif resultdificil in derrota:
                        computer += 1 
                elif resultdificil in empate: 
                        tie += 1
                res = comp2(resultdificil)
        resultSerie(player,computer,tie)

def pptls(n): # Función para el modo lagarto spock de piedra papel tijera
        computer = 0
        player = 0
        tie = 0
        for i in range (n):
                computerRandom = random.randint(1,5)
                valorPlayer = ""
                while valorPlayer not in ("piedra","papel","tijera","lagarto","spock"):
                        valorPlayer = vppptls()
                        if valorPlayer in ("piedra","papel","tijera","lagarto","spock"):
                                break
                        else:
                                print("Opción incorrecta, intente de nuevo")
                result = comparacion(valorPlayer,computerRandom) 
                if result in victoria:
                        player += 1
                elif result in derrota:
                        computer += 1
                elif result in empate:
                        tie += 1
        resultSerie(player,computer,tie)
file = open("Menuppt.txt","a")
file.write("Elige una opción:\n1. Piedra Papel Tijera\n2. Piedra Papel Tijera (Dificil)\n3. Piedra Papel Tijera Lagarto Spock\n")
file.close()
def menuppt(): # Menú del juego
        file = open("Menuppt.txt","r")
        print(file.read()) 
        file.close()     

