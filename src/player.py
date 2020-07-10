# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.item = []

    def __str__(self):
        return f"{self.name} is in the {self.current_room}"

    def print_item_status(self, item):
        return f"You currently have the following items: {self.item}"

    def try_direction(self, answer):
        attribute = answer + '_to'
        # If the user enters a cardinal direction, attempt to move to the room there.
        if hasattr(self.current_room, attribute):
            self.current_room = getattr(self.current_room, attribute)
        else:
            # Print an error message if the movement isn't allowed.
            print("Sorry, you can't go that way")

    def get_item(self, item):
        self.item.append(item)
        print(f"You just added {self.item} to your inventory. Use it wisely!")

    #def drop_item(self, item):
        #self.item.remove(item)