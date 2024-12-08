"""
## File summary
File that contains all of the location info and navigation mechanics for the game.
"""

import items, combat, puzzles


# inidividual location attributes

baseCamp = {
    1 : {
        "title" : "Base Camp 1",
        "desc" : "This is a base camp. Here, you can craft items, unlock skills with skill points, and fast travel once you unlock it.",
        "crafting" : True,
        "skillUnlock" : True,
        # not in use due to skill unlock not being implemented
        "fastTravel" : False
        # turns to true once player has been to base camp 2
    },

    2 : {
        "title" : "Base Camp 2",
        "desc" : "You have found the second base camp. Here, you can craft items, unlock skills with skill points, and fast travel - fast travel will now also be unlocked at the first base camp.",
        "crafting" : True,
        "skillUnlock" : True,
        "fastTravel" : True
    }
}

mercenaryBase = {
    1 : {
        "title" : "Mercenary Base 1",
        "desc" : "This is a mercenary base. Within it lie resources, but you will have to fight enemie/s to get to them.",
        "items" : items.mercenaryBase1Items,
        "enemies" : combat.enemies["mercenary1"]
        # not in use currently due to combat system not being implemented
    }
}

supplyShack = {
    1 : {
        "title" : "Supply Shack",
        "desc" : "This is a supply shack. Here, you can buy items to help you along the course of the game.",
        "stock" : items.supplyShackItems
    }
}

woods = {
    1 : {
        "title" : "Woods 1",
        "desc" : "This is the woods. Within the woods, you will find resources to collect and animals to hunt.",
        "items" : items.woods1Items
    },

    2 : {
        "title" : "Woods 2",
        "desc" : "You are a little further into the woods.",
        "items" : items.woods2Items
    },

    3 : {
        "title" : "Woods 3",
        "desc" : "You have ventured further in to the woods.",
        "items" : items.woods3Items
    },

    4 : {
        "title" : "Woods 4",
        "desc" : "You have ventured even further into the woods.",
        "items" : items.woods4Items
    },

    5 : {
        "title" : "Woods 5",
        "desc" : "You have made it quite far into the woods.",
        "items" : items.woods5Items
    }
}

crypt = {
    1 : {
        "title" : "Crypt 1",
        "desc" : "This is a crypt. Here, you may find gold coins and you can gain a skill point.",
        "items" : items.crypt1Items,
        "puzzle" : False
    },

    2 : {
        "title" : "Crypt 2",
        "desc" : "You have found another crypt. To enter, you need a skill point.",
        "items" : items.crypt2Items,
        "puzzle" : False
    }
}

tomb = {
    1 : {
        "title" : "Tomb 1",
        "desc" : "This is a tomb. In here, you will be able to find treasure such as artifacts and/or gold coins. To find them, you'll have to explore the tomb.",
        "items" : items.tomb1Items,
        "puzzle" : False
    },

    2 : {
        "title" : "Tomb 2",
        "desc" : "You have found another tomb.",
        "items" : items.tomb2Items,
        "puzzle" : False
    }
}


# location index assigment

locationsDict = {
    0 : {
        "location" : baseCamp[1],
        "exits" : {
            "N" : 1,
            "E" : 2,
            "W" : 3,
            "S" : 4
        }
    },

    1 : {
        "location" : crypt[1],
        "exits" : {
            "N" : False,
            "E" : False,
            "W" : False,
            "S" : 0
        }
    },

    2 : {
        "location" : woods[1],
        "exits" : {
            "N" : 5,
            "E" : 6,
            "W" : 0,
            "S" : 7
        }
    },

    3 : {
        "location" : tomb[1],
        "exits" : {
            "N" : False,
            "E" : 0,
            "W" : False,
            "S" : False
        }
    },

    4 : {
        "location" : woods[2],
        "exits" : {
            "N" : 0,
            "E" : 7,
            "W" : False,
            "S" : False
        }
    },

    5 : {
        "location" : mercenaryBase[1],
        "exits" : {
            "N" : False,
            "E" : False,
            "W" : False,
            "S" : 2
        }
    },

    6 : {
        "location" : tomb[2],
        "exits" : {
            "N" : False,
            "E" : False,
            "W" : 2,
            "S" : False
        },
        "requires" : items.skillPoint
    },

    7 : {
        "location" : woods[3],
        "exits" : {
            "N" : 2,
            "E" : 8,
            "W" : 4,
            "S" : 9
        }
    },

    8 : {
        "location" : woods[4],
        "exits" : {
            "N" : False,
            "E" : False,
            "W" : 7,
            "S" : 10
        }
    },

    9 : {
        "location" : crypt[2],
        "exits" : {
            "N" : 7,
            "E" : 10,
            "W" : False,
            "S" : False
        },
        "requires" : items.skillPoint
    },

    10 : {
        "location" : woods[5],
        "exits" : {
            "N" : 8,
            "E" : 11,
            "W" : 9,
            "S" : False
        }
    },

    11 : {
        "location" : baseCamp[2],
        "exits" : {
            "N" : False,
            "E" : False,
            "W" : 10,
            "S" : 12,
        }
    },

    12 : {
        "location" : supplyShack[1],
        "exits" : {
            "N" : 11,
            "E" : False,
            "W" : False,
            "S" : False
        }
    }
}

# location variable/s for player
playerLocation = locationsDict[0]
ftUnlock = False

# navigation functions

def checkRequirements(exitDirection):
    # function for checking if the player meets the requirements to enter a location
    # exitDirection == the direction of the desired location
    global playerLocation
    confirmation = ""
    if "requires" in locationsDict[playerLocation["exits"][exitDirection]].keys():
        # if the location has a requirement, then...
        if locationsDict[playerLocation["exits"][exitDirection]]["requires"] in items.playerInventory:
            # if the required item is in the player's inventory, then...
            confirmation = True
            # they are allowed in this location
        else:
            print("Entering this location requires:", locationsDict[playerLocation["exits"][exitDirection]]["requires"])
            print("You remain in your current location.")
            confirmation = False
            # they are not allowed in this location
    else:
        confirmation = True

    return confirmation

def goTo(userInput):
    # function for going to a location
    # userInput == the direction of the player [compass-based]

    global ftUnlock
    # fast travel unlock declared as global

    if userInput.upper() == "N" or userInput.upper() == "NORTH":
        # if the direction is north, then...
        if checkRequirements("N") == True:
            # if the user meets the location's requirements, then...
            goNorth()
            # execute the function for going north
        else:
            return
            # stops the function so it doesn't loop over

    if userInput.upper() == "E" or userInput.upper() == "EAST":
        if checkRequirements("E") == True:
            goEast()
        else:
            return

    if userInput.upper() == "W" or userInput.upper() == "WEST":
        if checkRequirements("W") == True:
            goWest()
        else:
            return

    if userInput.upper() == "S" or userInput.upper() == "SOUTH":
        if checkRequirements("S") == True:
            goSouth()
        else:
            return

    if playerLocation["location"]["title"] == "Base Camp 2":
        # if the player has reached the second base camp, then...
        ftUnlock = True
        # fast travel is unlocked


def goNorth():
    global playerLocation
    # declares player location as global
    if playerLocation["exits"]["N"] == False and type(playerLocation["exits"]["N"]) == type(False):
        # if there is not an exit towards the north, then...
        print("Can't go that way. You remain in your current location.")
    else:
        playerLocation = locationsDict[playerLocation["exits"]["N"]]
        # player location = locations dictionary [index of the northern exit]
        print(playerLocation["location"]["desc"])
        # prints the description of the location
        if "items" in playerLocation["location"].keys():
            # if there are items in the area, then...
            items.printItems()
            # print the items in the area
        if any(item in playerLocation["location"]["title"] for item in ["Crypt", "Tomb"]) == True:
            # if the location is a Crypt or Tomb, then...
            puzzles.goToPuzzle()
            # run puzzle mechanics

def goEast():
    global playerLocation
    if playerLocation["exits"]["E"] == False and type(playerLocation["exits"]["E"]) == type(False):
        print("Can't go that way. You remain in your current location.")
    else:
        playerLocation = locationsDict[playerLocation["exits"]["E"]]
        print(playerLocation["location"]["desc"])
        if "items" in playerLocation["location"].keys():
            items.printItems()
        if any(item in playerLocation["location"]["title"] for item in ["Crypt", "Tomb"]) == True:
            puzzles.goToPuzzle()

def goWest():
    global playerLocation
    if playerLocation["exits"]["W"] == False and type(playerLocation["exits"]["W"]) == type(False):
        print("Can't go that way. You remain in your current location.")
    else:
        playerLocation = locationsDict[playerLocation["exits"]["W"]]
        print(playerLocation["location"]["desc"])
        if "items" in playerLocation["location"].keys():
            items.printItems()
        if any(item in playerLocation["location"]["title"] for item in ["Crypt", "Tomb"]) == True:
            puzzles.goToPuzzle()

def goSouth():
    global playerLocation
    if playerLocation["exits"]["S"] == False and type(playerLocation["exits"]["S"]) == type(False):
        print("Can't go that way. You remain in your current location.")
    else:
        playerLocation = locationsDict[playerLocation["exits"]["S"]]
        print(playerLocation["location"]["desc"])
        if "items" in playerLocation["location"].keys():
            items.printItems()
        if any(item in playerLocation["location"]["title"] for item in ["Crypt", "Tomb"]) == True:
            puzzles.goToPuzzle()


# fast travel function



def fastTravel(target):
    # function for fast travel
    global playerLocation

    if playerLocation["location"]["title"] == "Base Camp 2" and target == "1":
        # if you're at the second base camp and you're travelling to the first, then...
        playerLocation = locationsDict[0]
        # change location to base camp 1
        print(playerLocation["location"]["desc"])
        # print the description of the base camp so the player is aware they have fast travelled

    elif playerLocation["location"]["title"] == "Base Camp 1" and target == "2":
        # if you're at the first base camp and you're travelling to the second, then...
        if ftUnlock == False:
            # if the player has not unlocked fast travel, then...
            print("Command has not been unlocked yet.")
            pass
        else:
            # if they player has unlocked fast travel, then...
            playerLocation = locationsDict[11]
            # change location to base camp 2
            print(playerLocation["location"]["desc"])
    else:
        # if you're not at any base camp, or you're trying to fast travel to the base camp you're currently at, then...
        print("Command can only be used at base camps, and you cannot fast travel to the base camp you are currently at.")

