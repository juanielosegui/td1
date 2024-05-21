import math

#REPRESENTACIÓN DE LA INFORMACIÓN:
    
#La computadora almacena y opera en todos los niveles (procesador, disco rígido,
#memoria...) por medio de bits (ceros y unos) representados mediante
#diferencias de tensión - válvula apagada: 0 y prendida: 1. La computadora
#trabaja con secuencias de bits que se interpretan como enteros, caracteres, etc.



#¿Cómo representar los tipos usando secuencias de bits? Conversiones a mano
#o con páginas web.



#ENTEROS:
#para una computadora son parecidos a los Z matemáticos, pero están
#acotados por encima y por debajo. 

#Notación sin signo: usa n bits para el valor. No hay números negativos.
#                    Rango representable: 0 a 2^n -1.

#Notación signo y magnitud (n bits): usa 1 bit para signo y n-1 bits para el valor.
#                                    Rango reporesentable: -(2^n-1 -1) a 2^n -1.
#                                    Bit de signo: 0 = positivo, 1 = negativo.
#                                    Los bits restantes determinan la magnitud.

#BitwiseNot(1011) = 0100 negación bit a bit.

#Notación exceso: usa n bits, no considera al bit para el signo.
#                             Rango representable: -e a 2^n -e-1.
#                             Permite representar un rango arbitrario.

#Python usa secuencias de bits de longitud variable para representar enteros.
#No imitan a priori el tamaño de los enteros representables, pero en la práctica
#hay un límite dado por la memoria física disponible.



#REALES:
#Los números en una computadora son muy distintos de los reales matemáticos.
#Para representar números se usa una cantidad limitada de bits. No se puede
#mostrar todo el desarrollo de raíz de 2.

print(math.sqrt(2))

#Punto fijo: usamos N bits para representar el número. Un bit S de signo,
#            un número K para la parte entera, y un número F para la fraccionaria.
#            (0)011001010.001001
#             S     K       F

#Números de punto flotante (float): un real r se representa en punto flotante
#por una terna (s, e, f) tal que r ≈ s . f . 2^e.
#Donde S pertenece [-1, 1] y 1 <= f < 2.
#Rango de representación: no uniforme sobre la recta numérica.
#                         Errores de overflow y underflow.
#Tipo de codificación IEEE-754 (32 ó 64).

#Caracteres: ejemplos de codificación de caracteres: ASCII, UTF-8, UTF-16, UTF-32
#            Latin-1, GB 18030.

#Sonido: wav y Hz.

#Pantalla: pixeles en formato BMP.

#Etc...