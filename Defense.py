import main
import Offense
from main import *

if main.computer_choice < 5:
    damage = (int(main.computer_choice)) * 10


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
elif main.computer_choice > 4:
    
    def bothdefence(staminalost, staminagained, paidHealth):
        if main.Choice_Computer == 5 and main.Choice_Player == 5:
            main.Stamina_Computer = main.Choice_Player = 5
        elif main.Choice_Computer == 6 and main.Choice_Player == 6:
            main.Stamina_Computer = main.Choice_Player = 6
        elif main.Choice_Computer == 5 and main.Choice_Player == 6 or main.Choice_Computer == 6 and main.Choice_Player == 5:
            staminalost = 10
            staminagained = 10
            paidHealth = 10
            if main.choice_Computer == 5:
                main.Stamina_Computer -= 10
                main.Stamina_Player += 10
                main.HP_Computer += 10
                main.HP_Player -= 10
            elif main.choice_Computer == 6:
                main.Stamina_Computer += 10
                main.Stamina_Player -= 10
                main.HP_Computer -= 10
                main.HP_Player += 10
