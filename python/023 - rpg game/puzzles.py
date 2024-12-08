"""
## File summary
File that [in future] contains the puzzle systems for the game.
"""

import locations, items, misc

def crypt1():
    # function for when user enters first crypt
    print("You can see some gold coins further into the crypt. Go north to proceed and go south to exit.")
    print("Input action")
    userInput = input("→ ")

    if userInput != "go n":
        # if the user is not proceeding, then...
        misc.commandFilter(userInput)
        # filter for other commands

    if locations.playerLocation["location"]["title"] != "Crypt 1":
        # if the user has exited the crypt, then...
        items.checkArtifactAmount()
        return
        # exit the function

    locations.playerLocation["location"]["puzzle"] = False
    # puzzle completed? == no

    if items.grapplingHook in items.playerInventory:
        # if the player has a grappling hook, then...
        print("You walk forward and don't realise there is a trap until it is too late. You have fallen into a hole.")
        print("To get out, you use your grappling hook and climb out of the trap.")
        items.printItems("Crypt")
        # runs the function for printing the location's items with crypts being taken out of the exclude list
        exitAllowed = True
        # the player is allowed to exit the crypt at any time
        locations.playerLocation["location"]["puzzle"] = True
        # puzzle completed? == yes
        items.playerInventory.append(items.skillPoint)
        # gives the player a skill point
    elif items.skillPoint in items.playerInventory:
        # if the user has a skill point, then...
        print("You were about to walk forward, but then you realised there is a trap in front of you.")
        print("You avoid the trap and can now access the crypt's treasures.")
        items.printItems("Crypt")
        exitAllowed = True
        locations.playerLocation["location"]["puzzle"] = True
        items.playerInventory.append(items.skillPoint)

    else:
        # if the user has no grappling hook or skill points, then...
        print("You walk forward and don't realise there is a trap in front of you until it it's too late. You have now fallen into a hole in the ground.")
        print("Use the help command to see new commands.")

        exitAllowed = False
        # the player cannot leave

    while locations.playerLocation["location"]["puzzle"] == False:
        # while the puzzle is incomplete...
        print("Input action")
        userInput = input("→ ")

        if userInput == "go s" and exitAllowed == False:
            # if the user tries to exit when they're not allowed, then...
            print("Cannot exit at this time")
        elif userInput == "SKIP!":
            # if the user enters the cheat code 'SKIP!', then...
            print("You skip the puzzle, escape the trap and are now able to claim the crypt's rewards.")
            items.printItems("Crypt")
            exitAllowed = True
            locations.playerLocation["location"]["puzzle"] = True
            items.playerInventory.append(items.skillPoint)
        else:
            # if the user isn't trying to exit or use the cheat code, then...
            misc.commandFilter(userInput)
            # filter for other commands




def crypt2():
    # function for when user enters second crypt
    print("Puzzle not implemented yet. Might be in an update")
    print("For now, you can collect the items within to continue with the story.")
    items.printItems("Crypt")
    while locations.playerLocation["location"]["title"] == "Crypt 2":
        # while the user is here...
        print("Input action")
        userInput = input("→ ")

        misc.commandFilter(userInput)
        # filter their commands
        if locations.playerLocation["location"]["title"] != "Crypt 2":
            # if they exit...
            locations.locationsDict[9]["location"]["puzzle"] = True
            # puzzle complete? = yes
            items.checkArtifactAmount()
            # check if player has 4 artifacts
            items.playerInventory.append(items.skillPoint)
            # give them a skill point

            break
            # break the loop

    pass




def tomb1():
    # function for when user enters first tomb
    print("Puzzle not implemented yet. Might be in an update")
    print("For now, you can collect the items within to continue with the story.")
    items.printItems("Tomb")
    locations.playerLocation["location"]["puzzle"] = False
    while locations.playerLocation["location"]["title"] == "Tomb 1":
        # while the user is here...
        print("Input action")
        userInput = input("→ ")

        misc.commandFilter(userInput)
        if locations.playerLocation["location"]["title"] != "Tomb 1":
            locations.locationsDict[3]["location"]["puzzle"] = True
            items.checkArtifactAmount()
            items.playerInventory.append(items.skillPoint)

            break

    pass


def tomb2():
    # function for when user enters second tomb
    print("Puzzle not implemented yet. Might be in an update")
    print("For now, you can collect the items within to continue with the story.")
    items.printItems("Tomb")
    while locations.playerLocation["location"]["title"] == "Tomb 2":
        # while the user is here...
        print("Input action")
        userInput = input("→ ")

        misc.commandFilter(userInput)
        if locations.playerLocation["location"]["title"] != "Tomb 2":
            locations.locationsDict[6]["location"]["puzzle"] = True
            items.checkArtifactAmount()
            items.playerInventory.append(items.skillPoint)

            break

    pass


def goToPuzzle():
    # function for directing the player to a puzzle
    if locations.playerLocation["location"]["puzzle"] == True:
        # if the player has completed the puzzle, then...
        title = locations.playerLocation["location"]["title"].split()[0].lower()
        # converts the title of the location to a string
        print("You have already explored this", title + ".")
        return
    else:
        # if the puzzle is not completed then...
        if locations.playerLocation["location"]["title"] == "Crypt 1":
            crypt1()
        elif locations.playerLocation["location"]["title"] == "Crypt 2":
            crypt2()
        elif locations.playerLocation["location"]["title"] == "Tomb 1":
            tomb1()
        elif locations.playerLocation["location"]["title"] == "Tomb 2":
            tomb2()

