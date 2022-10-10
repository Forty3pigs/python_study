import time


class TrafficLight:
    __color = 'red'

    def running(self):
        self.__color = 'red'
        print(f'\033[41m{self.__color}\033[0m')
        time.sleep(7)
        self.__color = 'yellow'
        print(f'\033[43m{self.__color}\033[0m')
        time.sleep(2)
        self.__color = 'green'
        print(f'\033[42m{self.__color}\033[0m')
        time.sleep(3)


class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    __mass = 25  # kg/m^2

    def calc_asphalt_mass(self, height):
        return self.length * self.width * self.__mass * height / 1000


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


tl = TrafficLight()
tl.running()

road_length = 5000
road_width = 20
road_height = 5

r = Road(road_length, road_width)
print(f'{r.calc_asphalt_mass(road_height)} tons')

name = 'Igor'
last_name = 'Khorev'
position = 'manager'
salary = 100
bonus = 50

pos1 = Position(name, last_name, position, salary, bonus)
print(f'Total income of {pos1.get_full_name()} is {pos1.get_total_income()}')
