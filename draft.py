import semester_1.primality_test as test
import time

i = 0
for _ in range(1000000):
    if test.primality_test_fermat(561):
        i += 1

print(i)