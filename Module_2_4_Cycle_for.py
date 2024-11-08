numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for q in numbers:
    print(q)
for q in numbers:
    if q <= 1:
        continue
    elif q == 2:
        primes.append(q)
    elif q == 3:
        primes.append(q)
    elif q % 2 == 0:
        not_primes.append(q)
    elif q % 3 == 0:
        not_primes.append(q)
    else: primes.append(q)
print(primes, ' - список простых чисел')
print(not_primes, ' - список составных чисел')