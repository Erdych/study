immutable_var = 1, 'string', 5.0, False, [10, True, 'List']
print('Immutable tupple:', immutable_var)

# immutable_var[0] = 5 # программа выдаст ошибку, т.к. кортеж относится к неизменяемым объектам и не поддерживает обращение к элементу

immutable_var[4][1] = False #Кортеж может содержать в себе изменяемый элемент, например, список
print(immutable_var) #второй элемент списка "True" изменился на "False"


mutable_list = [50, 10.99, 'string', False, [1, 2, 3]]
print('Mutable list:', mutable_list)
mutable_list[0] = 45
mutable_list[1] = 9.99
mutable_list[2] = 'strong'
mutable_list[3] = True
mutable_list[4][2] = 4
print(mutable_list) # Все элементы списка изменились