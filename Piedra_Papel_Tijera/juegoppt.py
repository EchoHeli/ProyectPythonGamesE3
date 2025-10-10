import random 
def comparacion(valorPlayer,valorComputer):
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
                
def comp2(result):
        if result in (12,21):
                        return 3
        elif result in (13,31):
                        return 2
        elif result in (23,32):
                        return 1
        elif result in (11,22,33):
                rand = random.randint(1,3)
                return rand
def vp():
        valorPlayer = str(input("Elije Piedra, Papel, o Tijera: "))
        valorPlayer = valorPlayer.lower()
        valorPlayer = valorPlayer.replace(" ","")
        return(valorPlayer)

def vppptls():
        valorPlayer = input("Elije Piedra, Papel, Tijera, Lagarto, Spock: ") 
        valorPlayer = valorPlayer.lower()
        valorPlayer = valorPlayer.replace(" ","")
        return(valorPlayer)

def resultSerie(player,computer,tie):
        if player > computer:
                print(f"Usted ganó {player} juegos mientras que la computadora ganó {computer} juegos, ganó la serie!")
        elif computer > player:
                print(f"Usted ganó {player} juegos mientras que la computadora ganó {computer} juegos, perdió la serie!")
        elif player == computer:
                print(f"Usted y la computadora ganaron {player} juegos cada uno y empataron {tie} juegos de {tie+computer+player} juegos, empate!")
        else:
                print(f"Usted y la computadora empataron todos los juegos ({tie}) en la serie, empate!")

def ppt(n):
    computer = 0
    player = 0
    tie = 0
    for i in range (n):
        valorPlayer = ""
        computerRandom = random.randint(1,3)
        while valorPlayer not in ("piedra","papel","tijera"):
                valorPlayer = vp()
        result = comparacion(valorPlayer,computerRandom)
        if result in (31,23,12):
                player += 1
        elif result in (32,21,13):
                computer += 1
        else:
                tie += 1
    resultSerie(player,computer,tie)

def pptdificil(n):
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
                if result in (31,23,12):
                        player += 1
                        cont += 1
                elif result in (32,21,13):
                        computer += 1
                        cont += 1
                elif result in (11,22,33):
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
                if resultdificil in (31,23,12):
                       player += 1
                elif resultdificil in (32,21,13):
                        computer += 1
                elif resultdificil in (11,22,33):
                        tie += 1
                res = comp2(resultdificil)
        resultSerie(player,computer,tie)

def pptls(n):
        computer = 0
        player = 0
        tie = 0
        for i in range (n):
                computerRandom = random.randint(1,5)
                valorPlayer = ""
                while valorPlayer not in ("piedra","papel","tijera","lagarto","spock"):
                        valorPlayer = vp()
                        if valorPlayer in ("piedra","papel","tijera","lagarto","spock"):
                                break
                        else:
                                print("Opción incorrecta, intente de nuevo")
                result = comparacion(valorPlayer,computerRandom)
                if result in (31,23,12,15,24,35,41,43,52,54):
                        player += 1
                elif result in (13,14,21,25,32,34,42,45,51,53):
                        computer += 1
                else:
                        tie += 1
        resultSerie(player,computer,tie)

def menuppt():
        print("""Elige una opción:
1. Piedra Papel Tijera
2. Piedra Papel Tijera (Dificil)
3. Piedra Papel Tijera Lagarto Spock""")

