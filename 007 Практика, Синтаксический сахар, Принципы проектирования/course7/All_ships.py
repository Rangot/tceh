from pprint import pprint
from SeaBattle import *

class Ship:
    ship_locations = {}

    def __init__(self, name, length, location = 0):
        self.name = name
        self.length = length
        self.location = location

    # def selecting_ship(self):


def all_ships():
    name = 'ship_of_4'
    length = 4
    ship4 = Ship(name, length)
    Ship.ship_locations[ship4.name] = ship4.location

    name3_1 = 'ship_of_3_1'
    name3_2 = 'ship_of_3_2'
    length = 3
    ship3_1 = Ship(name3_1, length)
    ship3_2 = Ship(name3_2, length)
    Ship.ship_locations[ship3_1.name] = ship3_1.location
    Ship.ship_locations[ship3_2.name] = ship3_2.location

    pprint(Ship.ship_locations)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')
