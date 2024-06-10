n = int(input('Введите число от 3 до 20: '))
numbers = list(range(1, 21)) # список чисел [1, ..., 20]

password_list = [
    
]

#Алгоритм подбора чисел
for i in numbers:
    for k in numbers:
        if i < k and n % (i + k) == 0 and i + k <= n:
            password_list.append([i, k])
        elif i < k and i + k > n:
            break
        else:
            continue
        
print(password_list)
