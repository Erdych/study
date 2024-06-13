def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    
print_params() # выводит a, b, c по умолчанию
print_params(b = 25) # изменяет arg b
print_params(c = [1, 2, 3]) # изменяет arg c

values_list = [2, 'string', False]
values_dict = {
    'a': 10,
    'b': 'String_2',
    'c': True
}

print_params(*values_list) # распаковка списка args
print_params(**values_dict)  # распаковка словаря kwargs

values_list_2 = ['string', 10.05]
print_params(*values_list_2, 42) # в распакованном списке только два элемента, которые заменяют args a, b
