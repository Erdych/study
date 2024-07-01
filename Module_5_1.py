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


h = House('ЖК "Пашенный"', 20)
h.go_to(10)
h.go_to(15)
h.go_to(8)
h.go_to(8)
nh = House('Домик', 2)
nh.go_to(1)
nh.go_to(3)
nh.go_to(2)
