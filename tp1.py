from cafetero import filtrar_solo_CAFE, filtrarCAFE_BD, es_cafetero, n_esimo_cafetero, cafeteros_entre

def elegir_funcion() -> str:
    '''
    Despliega el menú de funciones disponibles en la pantalla y devuelve
    la opción elegida por el usuario.
    Requiere: Nada.
    Devuelve: La opción elegida por el usuario, en mayúscula y sin espacios 
    adelante y atrás según la siguiente codificación:
        A -> Filtrar solo CAFE;
        B -> Determinar si un número es cafetero;
        C -> Devolver n-ésimo número cafetero;
        D -> Devolver cafeteros entre dos números;
        X -> Finalizar;
    '''
    print()
    print('Funciones disponibles')
    print('---------------------')
    print('A. Filtrar solo CAFE [s]')
    print('B. Es cafetero [n]')
    print('C. N-ésimo cafetero [n]')
    print('D. Cafeteros entre [n,m]')
    print('X. Finalizar')
    
    # input permite al usuario ingresar su opción, strip le saca caracteres 
    # de fin de línea, upper la pasa a mayúsculas.
    opción_elegida:str = input('Seleccione una opción: ').upper().strip()
    return opción_elegida


# Cuerpo principal del programa
finalizar:bool = False
while not finalizar:
    opcion_seleccionada:str = elegir_funcion()
    # Se analiza la opción elegida
    
    if opcion_seleccionada == 'A':
        s:str = filtrar_solo_CAFE(input('Ingrese texto: '))
        print('String filtrado: ' + s + '.')
    
    elif opcion_seleccionada == 'B':
        n:str = input('Ingrese n: ')
        m:str = es_cafetero(n)
        if m == 'CAFE':
            print('El '+ n +' es cafetero.')
        else:
            print('El '+ n +' no es cafetero')
    
    elif opcion_seleccionada == 'C':
        n:str = n_esimo_cafetero(input('Ingrese n: '))
        resultado:int = n_esimo_cafetero(n)
        print('El ' + n +'-ésimo cafetero es el ' + str(resultado) + '.')

    elif opcion_seleccionada == 'D':
        n:str = cafeteros_entre(input('Ingrese n: '), input('Ingrese m: '))
        print('Cafeteros entre '+ n + ' y ' + m +' ')
    elif opcion_seleccionada == 'X':
        finalizar = True
    else:
        print('Opción inválida.')

    if opcion_seleccionada != 'X':
        input('Presione ENTER para continuar.')
