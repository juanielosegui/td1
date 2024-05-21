def sumar_digitos(s:str) ->
    '''
    Requiere: s está formado sólo por dígitos (0123456789)
    Devuelve: la suma de los dígitos de s.
    
    s:'45120'
    suma=0
    para cada posición i en s:
    suma = suma + s[i] -> el dígito en la posición i.
    devolver suma
    '''

    res:int=0
    i:int=0

    while i < len(s)
        res = res + int(s[i])
        i = i + 1
    return res

    print(sumar_digitos('01391235'))