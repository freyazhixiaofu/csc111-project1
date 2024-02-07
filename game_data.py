"""CSC111 Project 1: Text Adventure Game Classes

Instructions (READ THIS FIRST!)
===============================

This Python module contains the main classes for Project 1, to be imported and used by
 the `adventure` module.
 Please consult the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""
from typing import Optional, TextIO


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - number: a position in the world map
        - points: a brief description
        - br_desc: a brief description
        - long_desc: a long description
        - direc: a list of available commands/directions to move
        - visit: whether the place has been visited

    Representation Invariants:
        - number >= -1
        - points >= 0
    """
    number: int
    points: int
    br_desc: str
    long_desc: str
    # direc: list[str]
    visit: bool
    tcard: bool

    def __init__(self, number: int, points: int, brief: str, long: str,
                 visit: bool) -> None:
        """Initialize a new location.

        """
        self.number = number
        self.points = points
        self.br_desc = brief
        self.long_desc = long
        # self.direc = direc
        self.visit = visit
        self.tcard = False

        # NOTES:
        # Data that could be associated with each Location object:
        # a position in the world map,
        # a brief description,
        # a long description,
        # a list of available commands/directions to move,
        # items that are available in the location,
        # and whether the location has been visited before.
        # Store these as you see fit, using appropriate data types.
        #
        # This is just a suggested starter class for Location.
        # You may change/add parameters and the data available for each Location object as you see fit.
        #
        # The only thing you must NOT change is the name of this class: Location.
        # All locations in your game MUST be represented as an instance of this class.

        # TODO: Complete this method


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - name: str
        - start: int
        - target: int
        - target_points: int

    Representation Invariants:
        - start >= 0
        - target >= 0
        - target_points >= 0
    """
    name: str
    start: int
    target: int
    target_points: int

    def __init__(self, name: str, start: int, target: int, target_points: int) -> None:
        """Initialize a new item.
        """

        # NOTES:
        # This is just a suggested starter class for Item.
        # You may change these parameters and the data available for each Item object as you see fit.
        # (The current parameters correspond to the example in the handout).
        # Consider every method in this Item class as a "suggested method".
        #
        # The only thing you must NOT change is the name of this class: Item.
        # All item objects in your game MUST be represented as an instance of this class.

        self.name = name
        self.start_position = start
        self.target_position = target
        self.target_points = target_points


class Tcard(Item):
    def __init__(self, name: str, start: int, target: int, target_points: int):
        Item.__init__(self, name, start, target, target_points)
        self.swipes = 3


class Player:
    """
    A Player in the text advanture game.

    Instance Attributes:
        - x: coordinator of x
        - y: coordinator of y
        - inventory: the backpack of the player
        - vitory: whether the player wins
        - steps: how many steps has the player used so far

    Representation Invariants:
        - self.x >= 0
        - self.y >= 0
    """

    x: int
    y: int
    inventory: list
    victory: bool
    steps: int
    score: int

    def __init__(self, x: int, y: int) -> None:
        """
        Initializes a new Player at position (x, y).
        """

        # NOTES:
        # This is a suggested starter class for Player.
        # You may change these parameters and the data available for the Player object as you see fit.

        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False
        self.steps = 0
        self.score = 0


class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - location: a list of locations in the world
        - items: a list of items in the world
    Representation Invariants:
        - map != []
        - location != []
        - items != []
    """
    map: list[list[int]]
    location: list[Location]
    items: list[Item]

    def __init__(self, map_data: TextIO, location_data: TextIO, items_data: TextIO) -> None:
        """
        Initialize a new World for a text adventure game, based on the data in the given open files.

        - location_data: name of text file containing location data (format left up to you)
        - items_data: name of text file containing item data (format left up to you)
        """

        # NOTES:

        # map_data should refer to an open text file containing map data in a grid format, with integers separated by a
        # space, representing each location, as described in the project handout. Each integer represents a different
        # location, and -1 represents an invalid, inaccessible space.

        # You may ADD parameters/attributes/methods to this class as you see fit.
        # BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES IN THIS CLASS

        # The map MUST be stored in a nested list as described in the load_map() function's docstring below
        self.map = self.load_map(map_data)
        self.location = self.load_location(location_data)
        self.items = self.load_item(items_data)

        # NOTE: You may choose how to store location and item data; create your own World methods to handle these
        # accordingly. The only requirements:
        # 1. Make sure the Location class is used to represent each location.
        # 2. Make sure the Item class is used to represent each item.

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def load_map(self, map_data: TextIO) -> list[list[int]]:
        """
        Store map from open file map_data as the map attribute of this object, as a nested list of integers like so:

        If map_data is a file containing the following text:
            1 2 5
            3 -1 4
        then load_map should assign this World object's map to be [[1, 2, 5], [3, -1, 4]].

        Return this list representation of the map.
        """
        # with open("D:/23 winter courses/csc111/assignments/csc111-project1/map.txt") as f:
        lst = []
        for line in map_data:
            lst.append(line.strip())
        maplst = []
        for string in lst:  # ['1 -2 0','3 4 5']
            strrow = string.split()  # ['1','-2','0']
            introw = [int(num) for num in strrow]  # [1,-2,0]
            maplst.append(introw)
        return maplst

    def load_location(self, location_data: TextIO) -> list[Location]:
        """Store location file in to a dictionary
        each line of the text are related to the keys of the dictionary"""
        # with open("D:/23 winter courses/csc111/assignments/csc111-project1/locations.txt") as location_data:
        locations = []
        lastline = 0
        while lastline != "ENDFILE\n":
            name = int(location_data.readline().strip())
            points = int(location_data.readline().strip())
            # point2 = int(location_data.readline().strip())
            brief_desc = location_data.readline().strip()
            long_desc = location_data.readline().strip()

            location = Location(name, points, brief_desc, long_desc, False)

            need_tcard = location_data.readline().strip()
            if need_tcard == 'True':
                location.tcard = True

            locations.append(location)
            location_data.readline()
            lastline = location_data.readline()  # we let the lastline of location file to be ENDFILE
        return locations

    def load_item(self, items_data: TextIO) -> list[Item]:
        """Store a list of items in the world"""
        # with open("D:/23 winter courses/csc111/assignments/csc111-project1/items.txt") as items_data:

        itemlist = []
        for line in items_data.readlines():
            listline = line.strip().split()
            start = int(listline[0])
            target = int(listline[1])
            target_points = int(listline[2])
            name = listline[3]
            if name == 'tcard':
                item = Tcard(name, start, target, target_points, 4)
            else:
                item = Item(name, start, target, target_points)
            itemlist.append(item)
        return itemlist

    # TODO: Add methods for loading location data and item data (see note above).

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
         Preconditions:
         - x >= 0
         - y >= 0"""
        size_map_x = len(self.map[0])  # how many horizontally
        size_map_y = len(self.map)  # how many vertically
        if (x >= size_map_x) or (y >= size_map_y):
            return None
        elif self.map[y][x] >= 0:
            for loca in self.location:
                if loca.number == self.map[y][x]:
                    return loca
        else:
            return None


def pickup(player: Player, things: list, w: World) -> None:
    """put the list of things he wants into his backpack"""
    for thing in things:
        for item in w.items:
            if (item.name == thing and w.get_location(player.x, player.y) == item.start and thing != 'cat food'
                    and thing != 'dog food'):
                player.inventory.append(item)
            if item.name == thing and (item.name == 'tcard' or item.name == 'lucky pen' or item.name == 'cheat sheet'):
                item.start = -1 # so that you cannot pick up a second time
            if item.name == thing and item.name == 'cat food' and not any(
                    [item1.name == 'dog food' for item1 in player.inventory]):
                player.inventory.append(item)
            if item.name == thing and item.name == 'cat food' and not any(
                    [item2.name == 'dog food' for item2 in player.inventory]):
                player.inventory.append(item)
        print(f'successfully pickup {thing}')
    else:
        print('you cannot get them')


def deposit(player: Player, thing: str, w: World) -> None:
    """take one thing out from player's backpack and deposit it """

    for item in w.items:
        if thing == item.name and w.get_location(player.x, player.y) == item.target:
            player.inventory.remove(thing)
            player.score += item.target_points
            print(f'successfully deposit {thing}')
            if thing == 'latte':
                i = get_item_index(player, "lucky pen")
                player.inventory[i].start = w.get_location(player.x, player.y)
                print('now you can pick up lucky pen')
        else:
            print('you cannot deposit it')


def available_actions(player: Player, w: World) -> str:
    """
    Return the available actions in this location.
    The actions should depend on the items available in the location
    and the x,y position of this location on the world map.
    """

    # NOTE: This is just a suggested method
    # i.e. You may remove/modify/rename this as you like, and complete the
    # function header (e.g. add in parameters, complete the type contract) as needed
    curr_actions = 'look, inventory, score, quit, go'
    if any([item.start == w.get_location(player.x, player.y) for item in w.items]):
        curr_actions += ', pickup'
    elif any([item.target == w.get_location(player.x, player.y) and item in player.inventory
              for item in w.items]):
        curr_actions += ', deposit'
    return curr_actions


def get_item_index(player: Player, thing: str) -> int:
    """ get the idex of from the list of Items
    """
    i = 0
    while i < len(player.inventory):
        if player.inventory[i].name == thing:
            return i
        i += 1
