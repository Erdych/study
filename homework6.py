#Словарь
my_dict = {
    'Дмитрий' : 1299,
    'Владимир' : 1187,
    'Аскольд' : 844
}
print('Dict: ', my_dict)
print('Existing value: ', my_dict.get('Аскольд', 'Евгений'))
my_dict.update({'Евгений' : 1383, 'Павел' : 1754})
print('Deleted Value: ', my_dict.pop('Павел'))
print('Modified dictionary: ', my_dict)

#Множества
my_set = {1, 2, 1, 'Value', 'Value', }
print('Set: ', my_set)
my_set.add(999)
my_set.add(1999)
my_set.discard(1)
print('Modified set: ', my_set)