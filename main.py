import random
def attack(attackIndex, receiverDefence, receiverHealth, attackerStamina):
    print("akhdsgfjsdhvflkahsdf"+str(int(attackIndex*10*receiverDefence)))
    receiverHealth -= int(attackIndex*10*receiverDefence)
    attackerStamina -= attackIndex*10


# import Defence

HP_Player = 100
HP_Computer = 100
Stamina_Player = 50
Stamina_Computer = 50
Choice_Player = 0
Choice_Computer = 0
round = 0

#First we give the player the game instructions:
print("Welcome to our textfighter\nHere are a few instructions to get you started:\nThere are 4 attacks\nPress 1 for attack 1, 2 for attack 2, and so on\nThere are also 2 defences\n Press 5 for defence 1, and 6 for defence 2")

print(round)

#Get player's choice
def PlayersTurn():
    Choice_Player = input(print("Choose an option between 1-6 by typing that number: "))
    while not (Choice_Player.isdigit() and 1<= int(Choice_Player) <=6):
        Choice_Player = input("Invalid choice, please re-enter: ")
    #cast after the choice is correct
    Choice_Player = int(Choice_Player)

#Get computer choice and make sure they have the stamina
def ComputerTurn(computerStamina): #need to fix this up
    if computerStamina >= 40:
        return random.randint(1,4) if random.randint(1,2) == 1 else random.randint(4,6)
    elif computerStamina >= 30:
        return random.randint(1,4) if random.randint(1,2) == 1 else random.randint(4,6)
    elif computerStamina >= 20:
        return random.randint(1,4) if random.randint(1,2) == 1 else random.randint(4,6)
    elif computerStamina >= 10:
        return random.randint(1,4) if random.randint(1,2) == 1 else random.randint(4,6)
    else:
        return random.randint(5,6)


def getDefence(choice, stamina):
    stamina += choice*10
    return 0.2 if choice == 1 else 0.1

#We can make them fight by calling this function
def Fight(playerChoice, computerChoice, round):
    #ADD STAMINA
    playerDefence = getDefence(playerChoice, Stamina_Player) if playerChoice >= 5 else 1
    computerDefence = getDefence(computerChoice, Stamina_Computer) if computerChoice >= 5 else 1
    
    if playerDefence == 0:
        attack(playerChoice, computerDefence, HP_Computer, Stamina_Player)
    if computerDefence == 0:
        attack(computerChoice, playerDefence, HP_Player, Stamina_Computer)
    round += 1

#Now we call the fight function so long as there are still rounds left
while round <= 30 and HP_Player > 0 and HP_Computer > 0:
    Choice_Computer = ComputerTurn(Stamina_Computer)
    PlayersTurn()
    Fight(Choice_Player, Choice_Computer, round)
    print("The computer chose:", Choice_Computer)
    print("Your health is: "+ str(HP_Player) + "/100")
    print("Your stamina is: " + str(Stamina_Player) + "/50")
    print("This is round: " + str(round) + "/30")

if HP_Player > 0:
    print("Congratulations you have won!")
elif HP_Computer > 0:
    print("Unfortunately you have lost")
