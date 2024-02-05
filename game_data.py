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
        - item_ava: a list of available commands/directions to move

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
    item_ava: Optional[dict[str, int]] = None

    def __init__(self, number: int, points: int, brief: str, long: str,
                 visit: bool, itemavai: dict) -> None:
        """Initialize a new location.

        """
        self.number = number
        self.points = points
        self.br_desc = brief
        self.long_desc = long
        # self.direc = direc
        self.visit = visit
        self.item_ava = itemavai

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

    def available_actions(self):
        """
        Return the available actions in this location.
        The actions should depend on the items available in the location
        and the x,y position of this location on the world map.
        """

        # NOTE: This is just a suggested method
        # i.e. You may remove/modify/rename this as you like, and complete the
        # function header (e.g. add in parameters, complete the type contract) as needed
        if self.item_ava == {}:
            return "look", "inventory", "score", "quit", "deposit"
        return "look", "inventory", "score", "quit", "pickup", "deposit"


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
    def __init__(self, name: str, start: int, target: int, target_points: int, swipes: int):
        Item.__init__(self, name, start, target, target_points)
        self.swipes = swipes


class Player:
    """
    A Player in the text advanture game.

    Instance Attributes:
        - x: coordinator of x
        - y: coordinator of y
        - inventory: the backpack of the player
        - vitory: whether the player wins

    Representation Invariants:
        - self.x >= 0
        - self.y >= 0
    """

    x: int
    y: int
    inventory: list
    victory: bool

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


class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - # TODO add more instance attributes as needed; do NOT remove the map attribute

    Representation Invariants:
        - map != []
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
        self.items_data =

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
        for string in lst: #['1 -2 0','3 4 5']
            strrow = string.split() #['1','-2','0']
            introw = [int(num) for num in strrow] #[1,-2,0]
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
            preitem = location_data.readline().strip()
            if preitem == '\n':
                item_avai = None
            else:
                preitem1 = preitem.split(';')
                item_avai = {int(t.split('=')[0]): t.split('=')[1] for t in preitem1}
            location = Location(name,points,brief_desc,long_desc,False,item_avai)
            locations.append(location)
            location_data.readline()
            lastline = location_data.readline() # we let the lastline of location file to be ENDFILE
        return locations


    # TODO: Add methods for loading location data and item data (see note above).

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        """
        if

        return None
