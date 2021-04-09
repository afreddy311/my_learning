def eleccion_aleatorio():
    import random
    import pandas as pd
    pc = random.choice(['papel','tijera','piedra'])
    print(pc)
    player = input("tu turno\n")
    if player == pc :
        print("empate")
    elif player == "tijera" and pc == "piedra" :
        print("perdiste")
    elif  player == "papel" and pc == "piedra" :
        print("ganaste")
    else :
        print("juega de nuevo")
    
