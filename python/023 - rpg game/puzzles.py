"""
## File summary
File that [in future] contains the puzzle systems for the game.
"""

import locations, items, misc

def crypt1():
    print("You can see some gold coins further into the crypt. Go north to proceed and go south to exit.")
    print("Input action")
    userInput = input("→ ")

    if userInput != "go n":
        misc.commandFilter(userInput)

    if locations.playerLocation["location"]["title"] != "Crypt 1":
        return

    locations.playerLocation["location"]["puzzle"] = False

    if items.grapplingHook in items.playerInventory:
        print("You walk forward and don't realise there is a trap until it is too late. You have fallen into a hole.")
        print("To get out, you use your grappling hook and climb out of the trap.")
        items.printItems("Crypt")
        exitAllowed = True
        locations.playerLocation["location"]["puzzle"] = True
        items.playerInventory.append(items.skillPoint)
    elif items.skillPoint in items.playerInventory:
        print("You were about to walk forward, but then you realised there is a trap in front of you.")
        print("You avoid the trap and can now access the crypt's treasures.")
        items.printItems("Crypt")
        exitAllowed = True
        locations.playerLocation["location"]["puzzle"] = True
        items.playerInventory.append(items.skillPoint)

    else:
        print("You walk forward and don't realise there is a trap in front of you until it it's too late. You have now fallen into a hole in the ground.")
        print("Use the help command to see new commands.")

        exitAllowed = False

    while locations.playerLocation["location"]["puzzle"] == False:
        print("Input action")
        userInput = input("→ ")

        if userInput == "go s" and exitAllowed == False:
            print("Cannot exit at this time")
        elif userInput == "SKIP!":
            print("You skip the puzzle, escape the trap and are now able to claim the crypt's rewards.")
            items.printItems("Crypt")
            exitAllowed = True
            locations.playerLocation["location"]["puzzle"] = True
            items.playerInventory.append(items.skillPoint)
            items.checkArtifactAmount()
        else:
            misc.commandFilter(userInput)



def crypt2():
    print("Puzzle not implemented yet. Might be in an update")
    print("For now, you can collect the items within to continue with the story.")
    items.printItems("Crypt")
    while locations.playerLocation["location"]["title"] == "Crypt 2":
        print("Input action")
        userInput = input("→ ")

        misc.commandFilter(userInput)

    locations.playerLocation["location"]["puzzle"] = True
    items.checkArtifactAmount()
    items.playerInventory.append(items.skillPoint)

    pass




def tomb1():
    print("Puzzle not implemented yet. Might be in an update")
    print("For now, you can collect the items within to continue with the story.")
    items.printItems("Tomb")
    while locations.playerLocation["location"]["title"] == "Tomb 1":
        print("Input action")
        userInput = input("→ ")

        misc.commandFilter(userInput)

    locations.playerLocation["location"]["puzzle"] = True
    items.checkArtifactAmount()
    items.playerInventory.append(items.skillPoint)

    pass


def tomb2():
    print("Puzzle not implemented yet. Might be in an update")
    print("For now, you can collect the items within to continue with the story.")
    items.printItems("Tomb")
    while locations.playerLocation["location"]["title"] == "Tomb 2":
        print("Input action")
        userInput = input("→ ")

        misc.commandFilter(userInput)

    locations.playerLocation["location"]["puzzle"] = True
    items.checkArtifactAmount()
    items.playerInventory.append(items.skillPoint)

    pass


def goToPuzzle():
    if locations.playerLocation["location"]["puzzle"] == True:
        title = locations.playerLocation["location"]["title"].split()[0].lower()
        print("You have already explored this", title + ".")
        return
    else:
        if locations.playerLocation["location"]["title"] == "Crypt 1":
            crypt1()
        elif locations.playerLocation["location"]["title"] == "Crypt 2":
            print(locations.playerLocation["requires"])
            if locations.playerLocation["requires"] in items.playerInventory:
                crypt2()
            else:
                pass
        elif locations.playerLocation["location"]["title"] == "Tomb 1":
            tomb1()
        elif locations.playerLocation["location"]["title"] == "Tomb 2":
            print(locations.playerLocation["requires"])
            if locations.playerLocation["requires"] in items.playerInventory:
                tomb2()
            else:
                pass
