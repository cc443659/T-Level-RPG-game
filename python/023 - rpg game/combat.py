import misc, locations, random

playerHealth = 100

enemies = {
    "mercenary1" : {
        "health" : 100,
        "alive?" : True
    }
}



def attack():
    # enter attack function here
    pass

def run():
    chance = random.randrange(1, 2)

    if chance == 1:
        locations.playerLocation = locations.locationsDict[2]
    pass

def hide():
    # enter hiding/stealth here
    pass

def combatSequence():
    # enter attack menu here
    stage = 1
    print("--- OPTIONS ---")
    print("""run: escape the base
attack: attack the mercenary
hide: bide time for an attack""")

    print("Input action")
    userInput = input("→ ")

    misc.commandFilter(userInput)

# may or may not actually do this