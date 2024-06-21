def calculate_structure_sum(*args):
    counter = 0
    for i in args:
            if isinstance(i, int):
                counter += i
            elif isinstance (i, str):
                counter += len(i)
            elif isinstance (i, list) or isinstance(i, tuple):
                counter += calculate_structure_sum(*i)
            elif isinstance(i, set):
               counter += calculate_structure_sum(tuple(i))
            elif isinstance(i, dict):
                counter += calculate_structure_sum(tuple(i.items()))
            else:
                continue
    
    return counter

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(*data_structure)
print(result)
