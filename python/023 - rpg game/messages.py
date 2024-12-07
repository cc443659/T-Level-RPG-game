"""
## File summary
File that contains all of the key messages for the game.
"""

import locations

# start message

def startGame():
    print("""
_______________________________________________________________________
|     You are in snowy Siberian woods searching for artifacts.        |
|   They can be found in tombs or crypts - some of these require a    |
| skill point to enter. They can be earned by completing tombs/crypts |
|               & successfully raiding mercenary bases.               |
|                                                                     |
|   Gold coins can also be found in crypts/tombs, which you can use   |
|         to buy supplies from the Supply Shack once found.           |
|                                                                     |
|  You complete the game once you have found all the artifacts; you   |
| can either escape the woods and end the game, or continue exploring |
|  the map [if you have came across the second basecamp, then you can |
|                         use fast travel].                           |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾""")
    print("Leave the input field empty and press enter to exit the game at any time.")
    print("Type 'help' for help.")

# help command

def help():
    print("                 ------ GENERAL COMMANDS ------")
    print("""go <direction>: go in the specified direction [i.e. go n: go north]
take <item>: take a specified item from the location [i.e. take wood]
drop <item>: drop a specified item from inventory [i.e. drop wood]
inv: view current inventory""")
    if "Base Camp" in locations.playerLocation["location"]["title"]:
        # if the player is in a base camp, then...
        print("                 ----- BASE CAMP COMMANDS -----")
        if locations.ftUnlock == True:
            # if the player has unlocked fast travel, then...
            print("fast travel <base camp>: travel to another base camp [i.e. fast travel 1]")
        print("""craft menu: select item to craft from a menu; dependent on materials
craft <item>: craft desired item [i.e. craft bandages]""")
        # will put skill unlock command once made
    elif any(item in locations.playerLocation["location"]["title"] for item in ["Crypt", "Tomb"]) == True:
        # checks whether any of the items of the list - ["Crypt", "Tomb"] - are in the location title
        # if the player is in a puzzle [Crypt or Tomb], then...
        print("                 ------ PUZZLE COMMANDS ------")
        # will put commands once implemented
    elif "Supply Shack" in locations.playerLocation["location"]["title"]:
        # if the player is in a supply shack, then...
        print("                 --- SUPPLY SHACK COMMANDS ---")
        print("""view stock: display the items for sale in the supply shack
buy <item>: purchase the desired item""")
    print()
    # prints a new line for the main game action input

def completeGame():
    print("Congratulations! You have collected all of the artifacts and can now escape the forest.")
    print("However, if you'd still like to explore you are welcome to do so.")
    print("Escape? \n 1: Yes \n 2: No")
    choice = input("→ ")
    if choice == "1":
        exit("You successfully escape the forest with the artifacts.")
    if choice == "2":
        print("Very well. You can continue to move around the map. Exit at any time by pressing enter.")
