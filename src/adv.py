from room import Room
from player import Player
from item import Item

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
item = {
    'stick': Item("Walking stick", "Long, sturdy stick. Great for walking or maybe breaking something"),
    'candle': Item("Candle with matches", "You never know when you need more light. This long candle with matches will help"),
    'rope': Item("Rope", "An adventure always needs a rope!"),
    'note': Item("Note", "You've found a note! It reads: I have the treasure!\nYou'll never find me, but if you are brave enough you can come into the Dark Forest by way of the Overlook!")
}

room['outside'].add_item(item["stick"])
room['foyer'].add_item(item["candle"])
room['overlook'].add_item(item["rope"])
room['treasure'].add_item(item["note"])

# Make a new player object that is currently in the 'outside' room.
user_name = input("Name your player:")
player = Player(user_name, room['outside'])
possible_directions = ['n', 's', 'e', 'w']
# Write a loop that:
while True:
    # * Prints the current room name
    print(f"{player.current_room}")
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    if len(player.current_room.item) > 0:
        pick_up = input("").strip().lower().split()[0]
        if pick_up == 'y':
            player.get_item(player.current_room.item)
            player.current_room.remove_from_room()

        elif pick_up == 'n':
            print("Choose a direction to move (n, s, e, w) or q for quit:")
            answer = input("").strip().lower().split()[0]
            if answer in possible_directions:
                player.try_direction(answer)

    else:
        print("Choose a direction to move (n, s, e, w) or q for quit:")
        answer = input("").strip().lower().split()[0]
        answer = answer[0]
        print(answer)

                #standardize the input that is coming in - strip whitespace, lowercase it, and


        if answer in possible_directions:
        # If the user enters a cardinal direction, attempt to move to the room there.
            player.try_direction(answer)


        #player.current_room.get_item(thing)




    # If the user enters "q", quit the game.
    if answer == "q":
        print("See you next time! Goodbye")
        break
