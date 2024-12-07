"""
## File summary
File that contains all of the item-related mechanics of the game.
"""

import locations, misc, messages

climbingAxe = "climbing axe"
bow = "bow"

# item variable/s for player
playerInventory = [climbingAxe, bow]

wood = "wood"
leaves = "leaves"
feathers = "feathers"
berries = "berries"

rope = "rope"
cloth = "cloth"

artifact = "artifact"

grapplingHook = "grappling hook"
knife = "knife"

bandages = "bandages"
antiseptic = "antiseptic"

arrows = "arrows"

goldCoins = "gold coins"
skillPoint = "skill point"

allItems = [wood, leaves, feathers, berries, rope, cloth, artifact, grapplingHook, knife, antiseptic, bandages, arrows, goldCoins]
# skillPoint is separate from this list so that skill points can't be 'taken' or 'dropped'

def coinCheat():
    # function for a coin giving cheat code made for testing purposes
    for _ in range(0, 10):
        playerInventory.append(goldCoins)
    print("10 coins have been added to your inventory.")

# items found in the woods
woods1Items = [wood, leaves, leaves]
woods2Items = [wood, leaves, feathers]
woods3Items = [wood, feathers, berries, berries]
woods4Items = [leaves, berries, feathers, feathers]
woods5Items = [wood, wood, leaves, berries]

# items found in crypts
crypt1Items = [goldCoins, artifact, cloth, skillPoint]
crypt2Items = [goldCoins, artifact, skillPoint]

# items found in tombs
tomb1Items = [goldCoins, artifact, cloth, skillPoint]
tomb2Items = [goldCoins, artifact, skillPoint]

# items found in mercenary base
mercenaryBase1Items = [knife, arrows, arrows, cloth, goldCoins, skillPoint]

# inventory mechanics

def takeItem(item, locList):
    global playerInventory
    i = 0

    for value in locList:
        if value == item:
            i += 1
    if i > 1:
        print("Enter the amount you'd like to take")
        i = int(input("→ "))
    elif i < 0:
        print("Item not found")
        pass
    for value in range(0, i):
        try:
            locList.remove(item)
            playerInventory.append(item)
        except ValueError:
            print("Amount exceeds amount of items in the area - max amount of", item, "taken.")
            return

    print("You have taken", item + ".")
    return playerInventory

def dropItem(item, locList):
    global playerInventory
    i = 0
    for value in playerInventory:
        if value == item:
            i += 1
    if i > 1:
        print("Enter the amount you'd like to drop")
        i = int(input("→ "))
    for value in range(0, i):
        try:
            playerInventory.remove(item)
            locList.append(item)
        except ValueError:
            print("Amount exceeds amount of items in the area - max amount of", item, "dropped.")
            return

    print("You have dropped", item + ".")
    return playerInventory


# printing items mechanics

def printInv():
    global playerInventory
    excludeList = [climbingAxe, bow, grapplingHook, artifact, goldCoins, skillPoint]
    (playerInv := list(set(playerInventory)))
    for item in excludeList:
        if item in playerInv:
            playerInv.remove(item)
    for item in playerInv:
        if item is not playerInv[-1]:
            print(item + ":", playerInventory.count(item), end=", ")
        else:
            print(item + ":", playerInventory.count(item))

    tools = []
    for item in playerInventory:
        if any(value in item for value in [climbingAxe, bow, grapplingHook]) == True:
            tools.append(item)
            continue
    print("Tools", end=": ")
    for item in tools:
        if item != tools[-1]:
            print(item, end=", ")
        else:
            print(item)

    i = 0
    for item in playerInventory:
        if item == goldCoins:
            i += 1
            continue
    print("Gold coins:", i)

    i = 0
    for item in playerInventory:
        if item == skillPoint:
            i += 1
            continue
    print("Skill points:", i, "/ 5")

    i = 0
    for item in playerInventory:
        if item == artifact:
            i += 1
            continue
    print("Artifacts:", i, "/ 4")


def printItems(exception = None):
    (locationItemsList := locations.playerLocation["location"]["items"])
    disallowList = ["Crypt", "Tomb", "Supply Shack", "Mercenary Base"]
    if exception != None:
        disallowList.remove(exception)
    if locations.playerLocation["location"]["items"] == []:
        print("You don't seem to see any items in the area.")
        return
    if any(item in locations.playerLocation["location"]["title"] for item in disallowList) == False:
        for item in locationItemsList:
            if item not in allItems:
                locationItemsList.remove(item)
        print("You can see", end=" ")
        if len(set(locationItemsList)) > 1:
            for item in set(locationItemsList):
                if item is not list(set(locationItemsList))[-1]:
                    print(locationItemsList.count(item), item, end=", ")
                else:
                    print("and", locationItemsList.count(item), item)
        else:
            print(locationItemsList.count(item), item + ".")


# crafting functions

craftableItems = {
    grapplingHook : {
        "materials" : [climbingAxe, rope],
        "quantity" : 1
    },

    bandages : {
        "materials" : [cloth, leaves],
        "quantity" : 1
    },

    arrows : {
        "materials" : [wood, feathers, feathers],
        "quantity" : 2
    }
}

def craftItemMenu():
    for item in craftableItems:
        print("---", item, "---")
        for mat in set(craftableItems[item]["materials"]):
            print(mat + ":", playerInventory.count(mat), "/", craftableItems[item]["materials"].count(mat))

    print("Input action")
    userInput = input("→ ")



    misc.commandFilter(userInput)

def craftItem(item):
    if all(item in playerInventory for item in craftableItems[item]["materials"]) == True:
        for mat in craftableItems[item]["materials"]:
            if mat != climbingAxe:
                playerInventory.remove(mat)
            else:
                continue
    quantity = craftableItems[item]["quantity"]
    for _ in range(0, quantity):
        playerInventory.append(item)
    print(item.title(), "successfully crafted.")

def checkArtifactAmount():
    i = 0
    for item in playerInventory:
        if item == artifact:
            i += 1
    if i == 4:
        messages.completeGame()
    else:
        pass

# supply shack functions

supplyShackItems = {
    rope : {
        "stock" : 1,
        "quantity" : 1,
        "price" : 2
    },
    cloth : {
        "stock" : 5,
        "quantity" : 2,
        "price" : 1
    },
    antiseptic : {
        "stock" : 2,
        "quantity" : 1,
        "price" : 3
    }
}

def supplyShackMenu():
    for item in supplyShackItems:
        print("---", item, "---")
        print("Stock:", supplyShackItems[item]["stock"])
        print("Price for", str(supplyShackItems[item]["quantity"]) + ":", supplyShackItems[item]["price"])

    i = 0
    for item in playerInventory:
        if item == goldCoins:
            i += 1
            continue
    print("Gold coins:", i)

    print("Input action")
    userInput = input("→ ")



    misc.commandFilter(userInput)

def buyItem(item, quantity):
    for _ in range(0, (supplyShackItems[item]["quantity"] * quantity)):
        playerInventory.append(item)
    for _ in range(0, (supplyShackItems[item]["price"] * quantity)):
        playerInventory.remove(goldCoins)

    supplyShackItems[item]["stock"] -= quantity

    print(item.title(), "purchased successfully.")

# item usage

def itemFilter(item):
    if any(value in item for value in [bandages, antiseptic, berries]):
        return "heal"
    elif any(value in item for value in [climbingAxe, bow, grapplingHook, knife]):
        return "tool"