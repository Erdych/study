numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    for k in range(2, i):
        if i % k != 0:
            is_prime = True
            continue
        else:
            is_prime = False
            break
    if is_prime == True:
        primes.append(i)
    else:
        not_primes.append(i)

primes.remove(1)
print(primes)
print(not_primes)