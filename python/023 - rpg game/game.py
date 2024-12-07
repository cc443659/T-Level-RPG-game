import messages, misc

messages.startGame()

while True:
    print("Input action")
    userInput = input("→ ")

    misc.commandFilter(userInput)
