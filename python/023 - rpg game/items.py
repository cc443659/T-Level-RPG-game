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
    # function for taking an item from an environment
    # item == the item the player is taking
    # locList == the list relative to the current location that the item is taken from
    global playerInventory
    # delcares playerInventory as global so it can be accessed

    i = 0
    # the count of said item that is in the location

    for value in locList:
        # for every item in the local location list...
        if value == item:
            # if the item is the item to be taken, then...
            i += 1
            # count incremented
    if i > 1:
        # if there is more than one of the item in the environment, then...
        print("Enter the amount you'd like to take")
        i = int(input("→ "))
        # defines an amount to take
    elif i == 0:
        # if the item is not in the environment, then...
        print("Item not found")
        pass
    for _ in range(0, i):
        # for <count> times...
        try:
            # if possible...
            locList.remove(item)
            # remove the item from the local location list
            playerInventory.append(item)
            # add the item to the player's inventory
        except ValueError:
            # if the item is not in the location list [amount selected > count] then...
            print("Amount exceeds amount of items in the area - max amount of", item, "taken.")
            return
            # exit function

    print("You have taken", item + ".")
    return playerInventory
    # update the player inventory

def dropItem(item, locList):
    # function for dropping items
    # parameters == `takeItem()` parameters
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
            # inverse of taking an item
        except ValueError:
            print("Amount exceeds amount of items in the area - max amount of", item, "dropped.")
            return

    print("You have dropped", item + ".")
    return playerInventory


# printing items mechanics

def printInv():
    global playerInventory

    excludeList = [climbingAxe, knife, bow, grapplingHook, artifact, goldCoins, skillPoint]
    # items to be printed later
    (playerInv := list(set(playerInventory)))
    # walrus operator used for temporary variable assignment
    # declares a list of unique items in the player inventory
    for item in excludeList:
        # for each item in the exclude list...
        if item in playerInv:
            # if the item is in the player's inventory, then...
            playerInv.remove(item)
            # remove the item from the declared instance of the inventory
    for item in playerInv:
        # for each item in the player's inventory that is unique and not in the exclude list, then...
        if item is not playerInv[-1]:
            # if the item isn't the last to be printed, then...
            print(item + ":", playerInventory.count(item), end=", ")
            # print the item and its count, alongside a comma
        else:
            # if the item is the last to be printed, then...
            print(item + ":", playerInventory.count(item))
            # print the item and its count

    tools = []
    # list of tools to be printed
    for item in playerInventory:
        # for every item in the player's inventory...
        if any(value in item for value in [climbingAxe, bow, grapplingHook, knife]) == True:
            # any function used to check if any elements in a list of values are in a string
            # if the item is either a climbing axe, bow, grappling hook or knife, then...
            tools.append(item)
            # add the item to the tools list
            continue
            # continue to the next item in the list
    print("Tools", end=": ")
    # `end=": "` makes the print statements of the following for loop appear on the same line
    for item in tools:
        # for each item in the tools list...
        if item is not tools[-1]:
            print(item, end=", ")
        else:
            print(item)

    print("Gold coins:", playerInventory.count(goldCoins))
    print("Skill points:", playerInventory.count(skillPoint), "/ 5")
    print("Artifacts:", playerInventory.count(artifact), "/ 4")
    # prints the item and then the count of each item, respectively
    # done separately from the rest of the items to make them stand out more, improving accessibility


def printItems(exception = None):
    # function for printing the items currently in the environment
    (locationItemsList := locations.playerLocation["location"]["items"])
    # declares the `items` values of the current location as a variable for easier access throughout the function
    excludeList = ["Crypt", "Tomb", "Supply Shack", "Mercenary Base"]
    # list of locations to not automatically print the items of
    if exception != None:
        # if an exception is given, then...
        excludeList.remove(exception)
        # remove the exception from the exclude list
    if locationItemsList == []:
        # if there aren't any items in the area, then...
        print("You don't seem to see any items in the area.")
        return
    if any(item in locations.playerLocation["location"]["title"] for item in excludeList) == False:
        # if the title matches any value in the exclude list, then...
        for item in locationItemsList:
            # for every item in the location...
            if item not in allItems:
                # if the item is a skill point, then...
                locationItemsList.remove(item)
                # remove the item from the printing list
        print("You can see", end=" ")
        if len(set(locationItemsList)) > 1:
            # if there are more than 1 items in the area, then...
            for item in set(locationItemsList):
                # list cast as a set to make the for loop iterate across unique values
                # for every item in the area's items...
                if item is not list(set(locationItemsList))[-1]:
                    # cast back to a list so it can be indexed
                    print(locationItemsList.count(item), item, end=", ")
                else:
                    print("and", locationItemsList.count(item), item)
        else:
            # if there's only 1 item in the area, then...
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