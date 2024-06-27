calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string=''):
    count_calls()
    tuple_ = len(string), string.upper(), string.lower()
    return tuple_


def is_contains(string, list_to_search):
    count_calls()
    list_lower = []
    string_lower = string.lower()
    for i in list_to_search:
        if isinstance(i, str):
            list_lower.append(i.lower())
    if string_lower in list_lower:
        return True
    else:
        return False


print(string_info('module 3'))
print(string_info('new string'))
print(is_contains('painTing', ['Pain', 'Paint', 'PAINting']))
print(is_contains('ranSOM', ['ranDOM', 'soME']))
print(calls)
