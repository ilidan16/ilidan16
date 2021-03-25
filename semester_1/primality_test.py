import math
import random
import time

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
def primality_test_fermat(z, iter=25):
    """Вероятностая проверка на простоту с помощью малой теоремы Ферма"""
    if z == 1: return []
    if z == 2: return True
    for _ in range(iter):
        a = random.randint(2,z-1)
        if a**(z-1) % z != 1:
            return False
    return True
#================================================================
def primality_test_2_0(z):
    if primality_test_fermat(z):
        if primality_test(z):
            return True
        else:
            return False
    else:
        return False
#================================================================
print(primality_test_2_0(1))  
    
