#Christine Carde

# Define rooms with name, location, and items
rooms = {
    'Piltover Sky Tower': {'West': 'Hexcore Cafe', 'Item': 'empty room'},
    'Hexcore Cafe': {'East': 'Piltover Sky Tower', 'South': 'Arcane Arena', 'Item': 'Burrito'},
    'Arcane Arena': {'North': 'Hexcore Cafe', 'West': 'Abandoned Factory', 'East': 'Apothecary Shop',
                     'South': 'Zaun Alleyway', 'Item': 'Master Key'},
    'Abandoned Factory': {'East': 'Arcane Arena', 'Item': 'Gas Mask'},
    'Apothecary Shop': {'West': 'Arcane Arena', 'North': 'The Enchanted Library', 'Item': 'Strength Potion'},
    'The Enchanted Library': {'South': 'Apothecary Shop', 'Item': 'Spell Book'},
    'Zaun Alleyway': {'North': 'Arcane Arena', 'East': 'The Underground Lab', 'Item': 'Fists Gauntlets'},
    'The Underground Lab': {'West': 'Zaun Alleyway', 'Item': 'empty room'}
}
#List of items needed to defeat Silco
required_items = ['Burrito', 'Master Key', 'Strength Potion', 'Spell Book', 'Gas Mask', 'Fists Gauntlets']

def print_instructions():
    print( """
    Welcome to the world of Arcane! 
    
    Arcane is composed of two cities: The thriving city of Piltover and the starving, undercity of Zaun.
    They are both in danger and need your help!
    The evil inventor, Silco has stolen the powerful Hextech Cube and plans to use it to take over the world.
    Your goal is to collect all required items and defeat Silco in The Undeground Lab.
    
    You will need these items to win:
    - Burrito 
    - Master Key 
    - Strength Potion 
    - Spell Book 
    - Gas Mask
    - Fists Gauntlets 
    """)
#Initialize player
inventory = []
current_location = "Piltover Sky Tower"

def player_status():
    print('\n'f'You are in the {current_location}')
    print(f'Inventory: {inventory}')
    item = rooms[current_location]['Item']
    if item not in inventory:
        print(f'You see the {item}.')


#Function to move between rooms
def move_rooms(direction):
    global current_location
    if direction in rooms[current_location]:
        current_location = rooms[current_location][direction]
        print(f'You moved to {current_location}.')  # Inform the player where they are
    else:
        print('Invalid direction. Try again.')

#Function to collect items
def collect_item():
    item = rooms[current_location]['Item']
    if item not in inventory:
        inventory.append(item)
        print(f'You collected the {item}.')
    elif item in inventory: #If item is already collected
        print(f'You have already collected the {item}.')
    else: #There is no item in the room
        print('There is no item to collect here.')

#Main Game Loop
def main():
    print_instructions()

    while True:
        player_status()
        # Prompt player for movement
        action = input(f"\n""Enter a direction (North, South, East, West) or type 'Collect' to pick up item:").strip().capitalize()

        if action in ['North', 'South', 'East', 'West']:
            move_rooms(action)
        elif action == 'Collect':
            collect_item()
        else:
            print("Invalid action. Try again.")  #Input validation

        if current_location == "The Underground Lab":
            if len(inventory) == len(required_items):
                print("Woohoo, you've collected all items and defeated Silco!")
                print("You won!")
                break
            else:
                print("Oh no, you didn't get all the items you needed. Silco has captured you.")
                print("You lose!")
                break



# Call the main function to start the game
if __name__ == "__main__":
    main()
