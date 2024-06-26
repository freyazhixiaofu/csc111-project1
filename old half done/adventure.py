"""CSC111 Project 1: Text Adventure Game

Instructions (READ THIS FIRST!)
===============================

This Python module contains the code for Project 1. Please consult
the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""

# Note: You may add in other import statements here as needed
from game_data import World, Player, Item, Location, available_actions, deposit, pickup, go

# Note: You may add helper functions, classes, etc. here as needed

# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    w = World(open("map.txt"), open("locations.txt"), open("items.txt"))
    p = Player(0, 0)  # set starting location of player; you may change the x, y coordinates here as appropriate


# def print_format(sentences: str) -> None:
#     """convert a str into several lines for better formating"""
#     i = 0
#     lines = len(sentences) // 80
#     lst = []
#     while i < lines:
#         lst.append(sentences[i * 80: i * 80 + 80])
#         i += 1
#     if len(sentences) // 80 != len(sentences) / 80:
#         lst.append(sentences[i * 80:])
#     for line in lst:
#         print(line)

    menu = ["look", "inventory", "score", "quit", "pickup", "deposit", "go"]
    # we changed the menu(pickup , deposit) deleted "back"
    location = w.get_location(p.x, p.y)
    print(location.long_desc)
    while not p.victory:
        location = w.get_location(p.x, p.y)

        # TODO: ENTER CODE HERE TO PRINT LOCATION DESCRIPTION

        # Depending on whether or not it's been visited before,
        # print either full description (first time visit) or brief description (every subsequent visit)
        for item in p.inventory:
            if item.name == "tcard":
                if item.swipes == 1:
                    print("Warning: you only have 1 swipe left on your tcard, please renew your swipes")

        print("What to do? \n")
        print("[menu]")
        for action in available_actions(p, w).split(','):  # notice, I changed the method of Location into a function
            print(action)
        choice = input("\nEnter action: ")

        if choice == "[menu]":
            print("Menu Options: \n")
            for option in menu:
                print(option)
            choice = input("\nChoose action: ")

        elif choice == "look":
            print(location.long_desc)

        elif choice == "inventory":
            print(p.inventory)

        elif choice == "score":
            print(p.score)

        elif choice == "quit":
            break

        elif choice == "go":
            direction = input("\n Choose a direction")
            go(p, w, direction)
            location = w.get_location(p.x, p.y)
            if location.visit is False:
                print(location.long_desc)
            else:
                print(location.br_desc)

        elif choice == "pickup":
            things_to_pickup = input(
                "\n what do you want to pick up? use 'and' to connect things if you want more than one things")
            lst_of_things = things_to_pickup.split('and')
            pickup(p, lst_of_things, w)

        elif choice == "deposit":
            thing_to_deposit = input(
                "\n what do you want to deposit? you can only deposit one thing at a time")
            deposit(p, thing_to_deposit, w)
        else:
            print('your action is not available')
        if p.steps > 10:
            print('Danger! You are runnning out of steps. Now only 10 steps left.')

        if p.steps > 30:
            print('Sorry, you run out of steps and miss your exam')
            break

        if any(['lucky pen' == thing.name for thing in p.inventory]) and any([
            'cheat sheeet' == thing.name for thing in p.inventory]) and any([
            'lucky pen' == thing.name for thing in p.inventory]) and w.get_location(
            p.x, p.y) == 12 and p.steps < 31:
            print(f'yayyy you win!! your score is {(30 - p.score) * 7}')

            p.victory = True

        # TODO: CALL A FUNCTION HERE TO HANDLE WHAT HAPPENS UPON THE PLAYER'S CHOICE
        #  REMEMBER: the location = w.get_location(p.x, p.y) at the top of this loop will update the location if
        #  the choice the player made was just a movement, so only updating player's position is enough to change the
        #  location to the next appropriate location
        #  Possibilities:
        #  A helper function such as do_action(w, p, location, choice)
        #  OR A method in World class w.do_action(p, location, choice)
        #  OR Check what type of action it is, then modify only player or location accordingly
        #  OR Method in Player class for move or updating inventory
        #  OR Method in Location class for updating location item info, or other location data etc....
