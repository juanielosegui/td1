'''
from typing import List
a:List[int] = [1973, 1977, 2004, 2010]

print(len(a))
print(1977 in a)
print(a [3])
print(a)
print(a * 2)
'''
'''
EJERCICIOS LISTAS 1)

from typing import List
cuadrados:List[int] = [0]
i: int = 1
while i <= 100:
        cuadrados.append(i*i)
        i = i + 1

print(cuadrados)
'''
from typing import List
cuadrados:List[int] = [0]
i:int = 0
while i < len(cuadrados):
    if cuadrados[i]%2==1:
        print(cuadrados[i])
    i = i + 1