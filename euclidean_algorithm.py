# Алгоритм Евклида (простой)
#===============================
def gsd(a,b):
    if a < 0: a *= -1         
    if b < 0: b *= -1  
    if a == 0 and b != 0: return b  
    if b == 0 and a != 0: return a
    if a == 0 and b == 0: return 0  
       
    r = int
    while r != 0:
        if a < b:
            z = a
            a = b
            b = z
        r = a % b
        a = r
    return b
#===============================
print(gsd(1001,112))
print(gsd(0,-112))
print(gsd(0,0))
    

        
        
