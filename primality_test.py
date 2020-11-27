import math
import random

#================================================================
def primes(n):
    """Решето Эратосфена.
    Множество простых чисел до натурального n"""
    array = list(range(2,n))

    for i in range(len(array)):
        if array[i] != 0:
            for j in range(i + array[i], len(array), array[i]):
                array[j] = 0

    k = 0
    while k < len(array):
        if array[k] == 0:
            del array[k]
        else:
            k += 1


    return array
#================================================================
def primality_test(z):
    """Проверяет число на простоту"""
    if z == 1: return []
    
    for p in primes(math.floor(math.sqrt(z))):
        if z % p == 0:
            return False

    return True
#================================================================
for _ in range(10):
    z = random.randint(1, 10000)
    print(z, primality_test(z))   


            
    
