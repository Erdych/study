my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

while my_list != []:
    if my_list[0] > 0:
        print(my_list.pop(0))
    else:
        my_list.pop(0)
        
print('Code executed')