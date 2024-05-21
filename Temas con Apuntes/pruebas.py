'''
print(hex(121212).upper())  #Hexadecimal con uppercases.

if 10 > 5:
    if 14 + 10 == 24:
        print('14 más 10 es 24')
    print('10 es mayor que 5')

print('C' in 'Casa')
'''

'''
if 10 + 10 == 20:
    
    return res
    print (res)

'''
'''

a = 54.12391 + 12.91381
print(round(a, 2))

'''

from typing import List

'''

def redondeo (a:str) -> int:
    r:int = 0
    i:int = 0
    a:List[str] = ['a', 'b', 'c']

    while i < len(a):
        r = r + round(a[i])
        i = i + 1

    return r

print(redondeo)

'''

def agregar_2_r (a:List[int]) -> List:
    
    r: List [int] = []
    i:int = len(a) -1
    
    while i >= 0:
        r . append (a[i])
        i = i - 1
    return r

print(agregar_2_r(['1', '2', '3']))