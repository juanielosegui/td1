def bisiesto ( a : int) -> bool :
    ''' Requiere : a >=0
    Devuelve : True si a es un año bisiesto ; False si no.
    '''
    b:bool = (a % 4 == 0 and a % 100 != 0) or a % 400 == 0
    return b

a = 2000