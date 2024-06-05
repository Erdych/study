# Решение 1.
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

while my_list != []:
    if my_list[0] > 0:
        print(my_list.pop(0))
    else:
        my_list.pop(0)
        
print('Code executed')

# Решение 2.
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

while True:
    if my_list == []:
        break
    elif my_list[0] > 0:
        print(my_list.pop(0))
        continue
    else:
        my_list.pop(0)
        continue

print('Code executed')

# Решение 3. С использованием цикла for
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
for el in my_list:
    if el > 0:
        print(el)
    else:
        continue

print('Code executed')
