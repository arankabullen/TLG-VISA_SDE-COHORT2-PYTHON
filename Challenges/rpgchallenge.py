#!/usr/bin/python3
"""Driving a feature-rich game framework with
   a dictionary object | Alta3 Research"""

import json

def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      use [item]  # New command to use an item
      inspect    # New command to get room and item descriptions
    ''')

def showStatus():
    """Determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

def useItem(item):
    """Use the specified item"""
    if item in inventory:
        print('You used the ' + item + '.')
        # Add specific actions based on the item (customize as needed)
        if item == 'potion':
            print('You feel healed and energized!')
            # Implement health increase or other effects
        elif item == 'torch':
            print('The room is now well-lit.')
            # Implement visibility improvement
        inventory.remove(item)
    else:
        print('You don\'t have the ' + item + ' in your inventory.')

# Load room data from the JSON file
with open("rooms.json", "r") as file:
    rooms = json.load(file)

# an inventory, which is initially empty
inventory = []

# start the player in the Hall
currentRoom = 'Hall'

# number of moves made by the player
moves = 0

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # increment the number of moves
    moves += 1

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    elif move[0] == 'get':
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory.append(move[1])
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # if they type 'use' first
    elif move[0] == 'use':
        useItem(move[1])

    # if they type 'inspect'
    elif move[0] == 'inspect':
        # Print room description
        print('Room Description:', rooms[currentRoom].get('description', 'No description available.'))
        # Print item description if present
        if "item" in rooms[currentRoom]:
            print('Item Description:', rooms[currentRoom]['item'].get('description', 'No description available.'))

    # If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

    # Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        print('Number of Moves:', moves)
        break
