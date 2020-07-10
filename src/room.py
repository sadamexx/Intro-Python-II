# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.item = []
       

    def __str__(self):
        str = f"This is the {self.name}. {self.description}"

        for x in self.item:
            str += f"\n You see a {x}"

        if len(self.item) > 0:
            str += f"\n Would you like to pick up this item? (y/n)"
        return str


    def remove_from_room(self):
        self.item= []

    def add_item(self, item):
        self.item.append(item)
