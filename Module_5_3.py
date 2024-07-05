class House:

    def __init__(self, name, number_of_floors):
        self.current_floor = 1
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        print(f'Выбран этаж: {new_floor}')
        if self.number_of_floors >= new_floor > self.current_floor:
            for i in range(self.current_floor, new_floor):
                print(self.current_floor)
                self.current_floor += 1
        elif 1 <= new_floor < self.current_floor:
            for i in range(new_floor, self.current_floor):
                print(self.current_floor)
                self.current_floor -= 1
        elif new_floor == self.current_floor:
            print(f'Мы уже находимся на этаже {new_floor}')
            return
        else:
            print('Неверно выбран этаж')
            return
        print(f'Прибыли на {self.current_floor} этаж')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Пашенный', 25)
h2 = House('ЖК Баланс', 30)
print(h1)
print(h2)
print(h1 == h2)
h1 = h1 + 5
print(h1)
print(h1 == h2)
h1 += 10
print(h1)
h2 = 10 + h2
print(h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)
