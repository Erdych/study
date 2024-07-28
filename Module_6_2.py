class Vehicle:
    __COLOR_VARIANTS = ['Чёрный', 'Белый', 'Синий', 'Бордовый', 'Серебро', 'Фисташковый', 'Циан']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        lower_color_variants = []
        for i in self.__COLOR_VARIANTS:
            lower_color_variants.append(i.lower())
        if new_color.lower() in lower_color_variants:
            self.__color = new_color
            print(f'Цвет изменён на {new_color}')
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['Черный', 'Белый', 'Синий', 'Бордовый', 'Серебро', 'Фисташковый', 'Циан']
vehicle1 = Sedan('Фёдор', 'Toyota Mark II', 500,'Циан')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Розовый')
vehicle1.set_color('Чёрный')
vehicle1.owner = 'Василий'

# Проверяем что поменялось
vehicle1.print_info()
