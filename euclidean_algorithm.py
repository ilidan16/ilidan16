#=======================================================
"""Алгоритм Евклида (простой)"""
def gcd(a, b):
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    if a == 0 and b != 0:
        return b
    if b == 0 and a != 0:
        return a
    if a == 0 and b == 0:
        return 0

    r = int
    while r != 0:
        if a < b:
            z = a
            a = b
            b = z
        r = a % b
        a = r
    return b
#=======================================================
"""Алгоритм Евклида (расширенный)"""
def linear_representation(a, b):
    if a == 0 and b != 0:
        return [0, 1]
    if b == 0 and a != 0:
        return [1, 0]
    if a == 0 and b == 0:
        return [0, 0]

    flag1 = False
    flag2 = False
    flag3 = False
    if a < 0:
        a *= -1
        flag1 = True
    if b < 0:
        b *= -1
        flag2 = True
    if a < b:
        z = a
        a = b
        b = z
        flag3 = True

    
    i = 1
    array1 = [a, b]          #Далее первое число массива будет означать
    array2 = [[1, 0],[0, 1]]  #коэффициент перед a, второе - перед b"""
    while True:
        array1.append(array1[i-1] % array1[i])
        q = array1[i-1] // array1[i]
        m1 = array2[i]
        m2 = array2[i-1]
        array2.append([m2[0] - q*m1[0],m2[1] - q*m1[1]])
        if array1[i+1] != 0:
            i += 1
        else:
            result = array2[i]
            break

    if flag1:
        result[0] *= -1
    if flag2:
        result[1] *= -1
    if flag3:
        w = result[0]
        result[0] = array2[1]
        result[1] = w
    return result
#=======================================================
print(gcd(1001,112))
print(gcd(-1001,-112))
print(gcd(0,-112))
print(gcd(0,0))
print(linear_representation(1001,112))
print(linear_representation(-1001,-112))
print(linear_representation(-1001,0))
print(linear_representation(0,0))




        
