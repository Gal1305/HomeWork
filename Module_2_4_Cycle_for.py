numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for q in numbers:
    if q < 2:
        continue
    is_primes = True
    for i in range(2, int(q ** 0.5) +1):
        if q % i == 0:
            is_primes = False
            not_primes.append(q)
            break
    if is_primes:
        primes.append(q)
print(primes, ' - список простых чисел')
print(not_primes, ' - список составных чисел')