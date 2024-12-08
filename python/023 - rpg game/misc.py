"""
## File summary
File that contains all of the command filtering for the game.
"""

import locations, items, messages

def commandFilter(userInput):
    if userInput == "":
        # if the user just presses enter, then...
        exit("Game exited.")

    command = userInput.split()[0]
    # declares the command as the first word in the user's input

    if command == "go":
        # if the command is 'go', then...
        try:
            # if the user's input is valid, then...
            userInput = userInput.split()[1]
            # the `userInput` is declared as the direction the user intends to go
            locations.goTo(userInput)
            # runs the function for going in the direction stated in `userInput`
        except IndexError:
            # if the user has only entered 'go' and no direction, then...
            print("Invalid command")

    elif command == "take":
        # if the command is 'take', then...
        if len(userInput.split()) == 1:
            # if the item is only one word long, then...
            try:
                userInput = userInput.split()[1]
                # `userInput` is declared as the second word in the input [or, the item]
            except IndexError:
                print("Invalid command")
                return
        else:
            # if the item is multiple words long, then...
            userInput = ' '.join(userInput.split()[1:])
            # takes all the words that denote the item, and bind them together with spaces

        if (userInput in items.allItems and "items" in locations.playerLocation["location"].keys()) and userInput in locations.playerLocation["location"]["items"]:
            # if the item is a valid item and the location has items, and the item is in the area, then...
            items.takeItem(userInput, locations.playerLocation["location"]["items"])
            # runs the function for taking the desired item from the current location's item list
        else:
            # if the item is not valid or it is not in the area, then...
            print("Item not found")

    elif command == "drop":
        # if the command is 'drop', then...
        if len(userInput.split()) == 1:
            try:
                userInput = userInput.split()[1]
            except IndexError:
                print("Invalid command")
                return
        else:
            userInput = ' '.join(userInput.split()[1:])

        if userInput in items.allItems and "items" in locations.playerLocation["location"].keys():
            # if the item is not a skill point and the location has items [not a base camp], then...
            items.dropItem(userInput, locations.playerLocation["location"]["items"])
            # runs the function for dropping an item in the area
        else:
            print("Item not found")

    elif command == "inv":
        # if the command is 'inv', then...
        items.printInv()
        # run the function for printing the items in the player's inventory

    elif command == "help":
        # if the command is 'help', then...
        messages.help()
        # run the function for printing the general and/or relative area commands

    elif userInput == "COINS!":
        # if the user types in 'COINS!', then...
        items.coinCheat()
        # run a cheat code that gives the user 10 coins [stackable]

    elif userInput == "FASTTRAVEL!":
        locations.ftUnlock = True
        # changes the fast travel unlock variable to True
        print("You have unlocked fast travel.")

    elif "Base Camp" in locations.playerLocation["location"]["title"]:
        # if the user is at a base camp, then...
        if "fast" and "travel" in userInput.split()[:2]:
            # if the first two words in the user's input are 'fast travel', then...
            userInput = userInput.split()[2]
            # the target of the fast travel is the last word of the input
            locations.fastTravel(userInput)
            # runs the function for fast travelling
        if userInput == "craft menu":
            # if the input is 'craft menu', then...
            items.craftItemMenu()
            # run the function for bringing up the craftable items
            command = None

        if command == "craft":
            # if the command is 'craft', then...
            if len(userInput.split()[1:]) > 1:
                # if the item consists of multiple words, then...
                items.craftItem(' '.join(userInput.split()[1:]))
                # runs the function for crafting an item, taking the words after the command as the item
                command = None
                # prevents the function looping over
            elif len(userInput.split()[1:]) == 1:
                # if the item only consists of one word, then...
                items.craftItem(userInput.split()[1])
                # runs the function for crafting an item, taking the second word as the item
                command = None
            else:
                # if the command and/or item is invalid, then...
                print("Invalid command.")
                return
                # exits to main input menu

    elif locations.playerLocation["location"]["title"] == "Supply Shack":
        # if the user is at the supply shack, then...
        if userInput == "view stock":
            # if the user enters 'view stock', then...
            items.supplyShackMenu()
            # runs the function for bringing up the supply shack menu

        if command == "buy":
            # if the command is 'buy', then...
            amount = 1
            # default amount to buy is 1
            print("Input the amount you'd like to buy [enter 0 to cancel]")
            amount = int(input("→ "))

            if amount == 0:
                # if the user has entered 0, then...
                print("Purchase cancelled.")
                command = None
                return
                # exits to main input

            if len(userInput.split()[1:]) > 1:
                item = " ".join(userInput.split()[0:])
            elif len(userInput.split()[1:]) == 1:
                item = userInput.split()[1]
            else:
                print("Invalid command.")
                return

            if item not in items.supplyShackItems:
                # if the item is not in stock, then...
                print("Item not found")
                return

            if items.supplyShackItems[item]["stock"] < (items.supplyShackItems[item]["quantity"] * amount):
                # if the stock is lower than the amount the user is trying to buy, then...
                print("Not enough in stock.")
                command = None
                return

            coinCount = items.playerInventory.count(items.goldCoins)
            if coinCount >= (items.supplyShackItems[item]["price"] * amount):
                # if the amount of coins the player has is more than or equal to the total price, then...
                items.buyItem(item, amount)
                # runs the function for buying the item, taking the item and amount as parameters
                command = None
            else:
                # if the amount of coins the player has is less than the total price, then...
                print("You do not have the required funds.")
                return

    else:
        # if the command doesn't meet any of the requirements, then...
        print("Invalid command.")

