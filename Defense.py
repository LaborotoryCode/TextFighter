import main
import Offense


def defence1(defence):
    if main.Stamina_Player < 40:
        main.Stamina_Player += 10
    else:
        main.Stamina_Player = 50
    main.HP_Player -= (0.2*damage)

def defence2(defence):
    if main.Stamina_Player < 30:
        main.Stamina_Player += 20
    else:
        main.Stamina_Player = 50
    main.HP_Player -= (0.1*damage)
    
    
