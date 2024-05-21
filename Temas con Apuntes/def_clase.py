def millas_a_kilometros(d: float) -> float:
    #(def) explica la función hasta L11.
    #REQUIERE: d >= 0
    #DEVUELVE: el resultado (aprox)
    #de convertir d de millas a kilómetros.

    resultado: float = d * 1.60934
#Resultado de la operación de distancia (d) * 1.60934

    return resultado
#Devuelve el valor del resultado.

mi: float = 50.0
#Se crea la variable (mi)

km: float = millas_a_kilometros(mi)
#Se crea la variable (km), donde la
#función millas_a_kilometros -L1 hasta L11-
#usará los valores de la variable (mi).

print(str(int(mi)) + ' millas equivalen a '
     +str(int(km)) + ' kilómetros.')


'''Se puede poner "help(.)" en la consola para
   que dé información acerca de x comando.
'''