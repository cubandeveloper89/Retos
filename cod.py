### Juego y gano mientras tabako ande puesto ###

def juego_cod(tiempo, tabako: bool):
    wins = 0
    if tabako:
        for i in range(1,tiempo + 1):
            if i % 20 == 0:
                wins += 1
    return wins 
            
print(juego_cod(60,True))  