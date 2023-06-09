import random
import time
import math

print("Game started.\nChapter 1: The Beginning\n")
getgold = 0
getxp = 0

#################### - Stats - #####################################################################

Stats = {
    "xp": 0,
    "gold": 0,
    "maxhp": 10,
    "hp": 10,
    "power": 1,
    "hploss": 0,
    "strength": 10,
}

#################### - Inventory - #################################################################

Items = {

    "woodendaggeramount": 0,
    "woodenswordamount": 0,
    "catswordamount": 0,
    "copperswordamount": 0,

    "leatherarmoramount": 0,
    "copperarmoramount": 0,
    "catarmoramount": 0,

    "revivepotionamount": 0,
    "healthpotionamount": 0,
}

#################### - Functions - #################################################################

def choiceAdventure(Stats, Items):

    enemytypeint = random.randint(1, 4)

    if enemytypeint == 1:
        enemytype = "Wolf"
    if enemytypeint == 2:
        enemytype = "Slime"
    if enemytypeint == 3:
        enemytype = "Bear"
    if enemytypeint == 4:
        enemytype = "Goblin"

    enemylvl = random.randint(Stats["xp"] * 0.5, Stats["xp"] + 15)

    if enemytype == "Wolf":
        enemydamage = int(enemylvl*0.5)
        enemyhp = int(enemylvl*0.5)

    print(enemydamage, enemyhp)

    print("\n\n\nYou have encountered a", enemytype, "( lvl:", enemylvl, ")")
    print("\nWhat do you want to do?")
    print("\n1 - Attack\n2 - Run\n")
    
    attackChoice = input("")

    if attackChoice == 1:
        enemyhp = enemyhp - Stats["strength"]
        if enemyhp <= 0:
            getxp = enemylvl * 0.3
            getgold = random.randint(enemylvl * random.randint(0.05, 0.2))
            Stats["gold"] += getgold
            Stats["xp"] += getxp
            print("You won!")
            print("\n( +)", getgold, "Gold )")
            print("\n( +)", getxp, "XP )")
        else:
            Stats["hp"] = Stats["hp"] - enemydamage

def die():
    print("You died.\nGame over.")

def choiceStats():
    print("")
    print("XP -", Stats["xp"])
    print("Gold -", Stats["gold"])
    print("HP -", Stats["hp"], "/", Stats["maxhp"])
    print("Strenght -", Stats["strength"], "( Power:", Stats["power"], ")")

#################### - Loop - ######################################################################

while True:
    Stats["strength"] = Stats["hp"] * Stats["power"]

    time.sleep(1.5)
    print('\nOptions: \n1 - Adventure \n2 - Stats \n3 - Inventory \n4 - Shop \n5 - Help \n6 - Item list \n7 - Gamble')
    choice=input('Choice: ')

    if choice == "1":
        choiceAdventure(Stats, Items)

    if choice == "2":
        choiceStats()

    if choice == "stop":
        break