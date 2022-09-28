import main
import Defense

def attack1(receiverDefence, receiverHealth, attackerStamina):
    receiverHealth -= int(1*10*receiverDefence)
    attackerStamina -= 1*10
def attack2(receiverDefence, receiverHealth, attackerStamina):
    receiverHealth -= int(2*10*receiverDefence)
    attackerStamina -= 2*10
def attack3(receiverDefence, receiverHealth, attackerStamina):
    receiverHealth -= int(3*10*receiverDefence)
    attackerStamina -= 3*10
def attack4(receiverDefence, receiverHealth, attackerStamina):
    receiverHealth -= int(4*10*receiverDefence)
    attackerStamina -= 4*10