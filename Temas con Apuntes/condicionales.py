'''
def f(n:int):
    print('.....')
    if n > 5:
        print('n vale', n)
        print('_______')
    print('%%%%%')

print('che')
f(4)
f(5)
f(6)
print('chau')
'''

'''
def f(n:int):
    if n > 5:
        print(n, 'es mayor que 5.')
    elif n==5:
        print(n, 'es igual que 5.')
    else:
        print(n, 'es menor que 5.')

print('che,')
f(4)
f(5)
f(6)
print('chau')
'''

'''
a:int = 1234
b:int = 987
c:int = 0

if a > b:
    c=a
else:
    c = b
print(c)
'''

def decime_si_es_par (n:int):
    b:bool = (n % 2 == 0)
    return b

        if decime_si_es_par (n):
            print('Es par')
        else:
            print('No es par')