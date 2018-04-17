from pprint import pprint
from .All_ships import *


class Player:
    players = {}

    def __init__(self, name, turn):
        self.turn = turn
        self.name = name


class Field:
    size = [[i for i in range(10)] for _ in range(10)]
    pprint(size)

    def __init__(self, size, number_of_ships):
        self.size = size
        self.number_of_ships = number_of_ships

    @staticmethod
    def locating_ship(self):
        horizontal = True
        while True:
            is_horizontal = input('Хотите, чтобы корабль был размещен вертикально? Yes/no: ').lower()
            if is_horizontal == 'yes':
                horizontal = True
                break
            elif is_horizontal == 'no':
                horizontal = False
                break
            else:
                print('Введите "yes" или "no"')


class Ship:
    ship_locations = {}

    def __init__(self, name, length, location=0):
        self.name = name
        self.length = length
        self.location = location

    @staticmethod
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

        name2_1 = 'ship_of_2_1'
        name2_2 = 'ship_of_2_2'
        name2_3 = 'ship_of_2_3'
        length = 2
        ship2_1 = Ship(name2_1, length)
        ship2_2 = Ship(name2_2, length)
        ship2_3 = Ship(name2_3, length)
        Ship.ship_locations[ship2_1.name] = ship2_1.location
        Ship.ship_locations[ship2_2.name] = ship2_2.location
        Ship.ship_locations[ship2_3.name] = ship2_2.location

        name1_1 = 'ship_of_1_1'
        name1_2 = 'ship_of_1_2'
        name1_3 = 'ship_of_1_3'
        name1_4 = 'ship_of_1_4'
        length = 1
        ship1_1 = Ship(name1_1, length)
        ship1_2 = Ship(name1_2, length)
        ship1_3 = Ship(name1_3, length)
        ship1_4 = Ship(name1_4, length)
        Ship.ship_locations[ship1_1.name] = ship1_1.location
        Ship.ship_locations[ship1_2.name] = ship1_2.location
        Ship.ship_locations[ship1_3.name] = ship1_3.location
        Ship.ship_locations[ship1_4.name] = ship1_4.location

        pprint(Ship.ship_locations)

    @staticmethod
    def selecting_ship():
        while True:
            select_ship = 0
            try:
                select_ship = int(input('Выберите корабль для размещения (4, 3, 2, 1): '))
            except ValueError as e:
                print('Неверный ввод! Введите число от 1 до 4'.format(e))
            if select_ship == 4:
                print('Разместите 4-палубный корабль: ')
                Field.locating_ship(Ship.ship_locations['ship_of_4'])
                break
            if select_ship == 3:
                print('Разместите 3-палубный корабль: ')
                break
            if select_ship == 2:
                print('Разместите 2-палубный корабль: ')
                break
            if select_ship == 1:
                print('Разместите 1-палубный корабль: ')
                break
            elif select_ship > 4:
                print('Такого корабля нет! Выберите другой: ')




class Shoot:
    made_shots = {}

    def __init__(self, who_shoot, coordinates, hit):
        self.who_shoot = who_shoot
        self.coordinates = coordinates
        self.hit = hit


def main():
    print('Морской бой запущен!')
    number_of_ships = 10
    size = [[i for i in range(10)] for j in range(10)]
    field = Field(size, number_of_ships)

    name = 'Вася'
    turn = 1
    player1 = Player(name, turn)
    Player.players[player1.name] = turn

    name = 'Дима'
    turn = 2
    player2 = Player(name, turn)
    Player.players[player2.name] = turn

    Ship.all_ships()

    print('\n{}, разместите свои корабли на поле!'.format(player1.name))

    Ship.selecting_ship()







if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')



