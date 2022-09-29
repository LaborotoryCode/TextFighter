import keyboard
import random
import Offense
import Defense
from Offense import *

HP_Player = 100
HP_Computer = 100
Stamina_Player = 50
Stamina_Computer = 50
Choice_Player = 1
Choice_Computer = 1
round = 0

#First we give the player the game instructions:
print("Welcome to our textfighter\nHere are a few instructions to get you started:\nThere are 4 attacks\nPress 1 for attack 1, 2 for attack 2, and so on\nThere are also 2 defences\n Press 5 for defence 1, and 6 for defence 2")

print(round)

#Get computer choice and make sure they have the stamina
def computer_turn() :
    global computer_choice
    if Stamina_Computer >= 40:
        computer_choice = random.randint(1,6)
    elif Stamina_Computer >= 30:
        while computer_choice == 4:
            random.randint(1,6)
    elif Stamina_Computer >= 20:
        while computer_choice == 4 or 3:
            random.randint(1,6)
    elif Stamina_Computer >= 10:
        while computer_choice == 4 or 3 or 2:
            random.randint(1,6)
    else:
        while computer_choice == 4 or 3 or 2 or 1:
            random.randint(1,6)

    
#Get player choices
if keyboard.is_pressed("1"):
    Choice_Player = 1
elif keyboard.is_pressed("2"):
    Choice_Player = 2
elif keyboard.is_pressed("3"):
    Choice_Player = 3
elif keyboard.is_pressed("4"):
    Choice_Player = 4
elif keyboard.is_pressed("5"):
    Choice_Player = 5
elif keyboard.is_pressed("6"):
    Choice_Player = 6


#We can make them fight by calling this function
def Fight() :
    if Choice_Player == 1:
        if Stamina_Player < 10:
            attack1
        else: 
            round -= 1
            return("You do not have enough stamina")
        if computer_choice == 1:
            attack1(1, HP_Player, Stamina_Player)
        elif computer_choice == 2:
            attack2(1, HP_Player, Stamina_Player)
        elif computer_choice == 3:
            attack3(1, HP_Player, Stamina_Player)
        elif computer_choice == 4:
            attack4(1, HP_Player, Stamina_Player)
        elif computer_choice == 5:
            defence1()
        elif computer_choice == 6:
            defence2
    elif Choice_Player == 2:
        if Stamina_Player < 20:
            attack2
        else: 
            round -= 1
            return("You do not have enough stamina")
        if computer_choice == 1:
            attack1(1, HP_Player, Stamina_Player)
        elif computer_choice == 2:
            attack2(1, HP_Player, Stamina_Player)
        elif computer_choice == 3:
            attack3(1, HP_Player, Stamina_Player)
        elif computer_choice == 4:
            attack4(1, HP_Player, Stamina_Player)
        elif computer_choice == 5:
            defence1
        elif computer_choice == 6:
            defence2
    elif Choice_Player == 3:
        if Stamina_Player < 30:
            attack3
        else: 
            round -= 1
            return("You do not have enough stamina")
        if computer_choice == 1:
            attack1(1, HP_Player, Stamina_Player)
        elif computer_choice == 2:
            attack2(1, HP_Player, Stamina_Player)
        elif computer_choice == 3:
            attack3(1, HP_Player, Stamina_Player)
        elif computer_choice == 4:
            attack4(1, HP_Player, Stamina_Player)
        elif computer_choice == 5:
            defence1
        elif computer_choice == 6:
            defence2
    elif Choice_Player == 4:
        if Stamina_Player < 40:
            attack4
        else: 
            round -= 1
            return("You do not have enough stamina")
        if computer_choice == 1:
            attack1(1, HP_Player, Stamina_Player)
        elif computer_choice == 2:
            attack2(1, HP_Player, Stamina_Player)
        elif computer_choice == 3:
            attack3(1, HP_Player, Stamina_Player)
        elif computer_choice == 4:
            attack4(1, HP_Player, Stamina_Player)
        elif computer_choice == 5:
            defence1
        elif computer_choice == 6:
            defence2
    elif Choice_Player == 5:
        defence1
        if computer_choice == 1:
            attack1(1, HP_Player, Stamina_Player)
        elif computer_choice == 2:
            attack2(1, HP_Player, Stamina_Player)
        elif computer_choice == 3:
            attack3(1, HP_Player, Stamina_Player)
        elif computer_choice == 4:
            attack4(1, HP_Player, Stamina_Player)
        elif computer_choice == 5:
            defence1
        elif computer_choice == 6:
            defence2
    elif Choice_Player == 1:
        defence2
        if computer_choice == 1:
            attack1(1, HP_Player, Stamina_Player)
        elif computer_choice == 2:
            attack2(1, HP_Player, Stamina_Player)
        elif computer_choice == 3:
            attack3(1, HP_Player, Stamina_Player)
        elif computer_choice == 4:
            attack4(1, HP_Player, Stamina_Player)
        elif computer_choice == 5:
            defence1
        elif computer_choice == 6:
            defence2
    round += 1

#Now we call the fight function so long as there are still rounds left
while round <= 30 and HP_Player > 0 and HP_Computer > 0:
    Fight()
    print("Your health is: {HP_Player}/100")
    print("Your stamina is: {Stamina_Player}/50")
    print("This is round {round}/30")

if HP_Player > 0:
    print("Congratulations you have won!")
elif HP_Computer > 0:
    print("Unfortunately you have lost")








