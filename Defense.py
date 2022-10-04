import main



def defence1(staminalost, staminaGained, paidHealth): #In all scenarios defender gains 10 Stamina
    if main.computer_choice < 5 and main.Choice_Player > 4: #If Player is defender, Computer is Attacker
        damage = (int(main.Choice_Computer)) * 10
        if main.Stamina_Player < 40: #Makes sure that Stamina doesn't exceed max
            main.Stamina_Player += 10
        else:
            main.Stamina_Player = 50
            main.HP_Player -= (0.2*damage)
    elif main.Choice_Computer > 4 and main.Choice_Player < 5: #If Computer is defender, Player is Attacker
        damage = (int(main.Choice_Player)) * 10
        if main.Stamina_Computer < 40:
            main.Stamina_Computer += 10
        else:
            main.Stamina_Computer = 50
            main.Stamina_Computer -= (0.2*damage)
    elif main.computer_choice > 4 and main.Choice_Player > 4: #If both defenders
        staminalost = 10
        staminaGained = 10
        paidHealth = 10
        if main.Choice_Computer == 5 and main.Choice_Player == 5: #if both are 5
            main.Stamina_Computer +=10
            main.Stamina_Player += 10
            main.HP_Player -= 10
            main.HP_Player -= 10
        elif main.Choice_Computer == 5 and main.Choice_Player == 6 or main.Choice_Computer == 6 and main.Choice_Player == 5: #if only one is 5
            if main.choice_Computer == 5:
                main.Stamina_Computer -= staminalost
                main.HP_Computer += paidHealth
            elif main.choice_Computer == 6:
                main.Stamina_Player -= staminalost #Only takes out Stamina for player, doesn't do HP since this is defence 1, defence 2 will initiate the HP Removal
                main.HP_Player += paidHealth

def defence2(staminalost, staminagained, paidHealth):
    if main.computer_choice < 5 and main.Choice_Player > 4: #Player is defender, Computer is Attacker
        damage = (int(main.Choice_Computer)) * 10
        if main.Stamina_Player < 30:
            main.Stamina_Player += 20
            main.HP_Player -= damage
        else:
            main.Stamina_Player = 50
            main.HP_Player -= damage
    elif main.Choice_Computer > 4 and main.Choice_Player < 5: #Computer defender, Player Attacker
        damage = (int(main.Choice_Player)) * 10
        if main.Stamina_Computer < 30:
            main.Stamina_Computer += 20
            main.Stamina_Computer-= damage
        else:
            main.Stamina_Computer = 50
            main.Stamina_Computer -= damage
    elif main.computer_choice > 4 and main.Choice_Player > 4: #Both defender
        staminalost = 10
        staminagained = 10
        paidHealth = 10
        if main.Choice_Computer == 6 and main.Choice_Player == 6: #if both defend same
            main.Stamina_Computer +=10
            main.Stamina_Player += 10
            main.HP_Player -= 10
            main.HP_Player -= 10
        elif main.Choice_Computer == 5 and main.Choice_Player == 6 or main.Choice_Computer == 6 and main.Choice_Player == 5:
            if main.choice_Computer == 5:
                main.Stamina_Player += staminagained
                main.HP_Computer += paidHealth
            elif main.choice_Computer == 6:
                main.Stamina_Player -= staminalost
                main.HP_Player += paidHealth




'''
if main.computer_choice < 5 and main.Choice_Player > 4:
    damage = (int(main.Choice_Computer)) * 10


    def defence1(staminalost, staminagained, paidHealth):
        if main.Stamina_Player < 40:
            main.Stamina_Player += 10
        else:
            main.Stamina_Player = 50
            main.HP_Player -= (0.2*damage)
    
    def defence2(defence):
        if main.Stamina_Player < 30:
            main.Stamina_Player += 20
            main.HP_Player -= damage
        else:
            main.Stamina_Player = 50
            main.HP_Player -= damage
elif main.computer_choice > 4 and main.Choice_Player > 4:
    def bothDef(staminalost, staminagained, paidHealth):
        staminalost = 10
        staminagained = 10
        paidHealth = 10
        if main.Choice_Computer == 5 and main.Choice_Player == 5:
            main.Stamina_Computer = main.Choice_Player = 5
        elif main.Choice_Computer == 6 and main.Choice_Player == 6:
            main.Stamina_Computer = main.Choice_Player = 6
        elif main.Choice_Computer == 5 and main.Choice_Player == 6 or main.Choice_Computer == 6 and main.Choice_Player == 5:
            if main.choice_Computer == 5:
                main.Stamina_Computer -= staminalost
                main.Stamina_Player += staminagained
                main.HP_Computer += paidHealth
                main.HP_Player -= paidHealth
            elif main.choice_Computer == 6:
                main.Stamina_Computer += staminagained
                main.Stamina_Player -= staminalost
                main.HP_Computer -= paidHealth
                main.HP_Player += paidHealth

elif main.Choice_Computer > 4 and main.Choice_Player < 5:
    damage = (int(main.Choice_Player)) * 10

    def defence1(staminalost, staminagained, paidHealth):
        if main.Stamina_Computer < 40:
            main.Stamina_Computer += 10
        else:
            main.Stamina_Computer = 50
            main.Stamina_Computer -= (0.2*damage)
    
    def defence2(defence):
        if main.Stamina_Computer < 30:
            main.Stamina_Computer += 20
            main.Stamina_Computer-= damage
        else:
            main.Stamina_Computer = 50
            main.Stamina_Computer -= damage
'''
