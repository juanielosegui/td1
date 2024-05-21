from typing import TextIO #IO: input/output -> es un tipo de datos

#ARCHIVO: 

#Colección numerada y ordenada de bytes que almacena
#datos procesales de un texto. Se almacena en un medio físico como un
#pendrive, disco duro, etc...

#Puede ser leído o escrito en su totalidad o por partes por un programa en ejecución
#--> Chrome o cualquier procesador de texto lo lee y lo vemos nosotros. A su vez almacena
#en sus datos en variables almacenadas en la memoria de la computadora.

#En el nombre del archivo se justifica la extensión que muestra la forma en la que está
#organizado el archivo, como .py, .txt, .html...

#Dos tipos de archivos: de texto (sólo tienen caracteres imprimibles: .py, .txt, .html)
#y binarios, que organizan el contenido de forma distinta (.wav, .jpg, .mp3)

file_handler:TextIO = open('provincias.txt') 
#El archivo TXT debe estar en la misma
#carpeta que el código Python.

#Handler: punteo a un archivo de texto.
#Se queda esperando en el principio hasta que le demos más instrucciones.

texto:str = file_handler.read()
#Si completo el argumento de file_handler.read con un número N me va a mostrar
#N cantidad de caracteres, puedo repetir esta operación y me va a mostrar de
#manera acumulativa

print(texto)
print (len(texto))
#Muestra la longitud del archivo de texto.

#for linea in file_handler:
      #linea = linea.rstrip()
      #print(linea[5:]) #Slice
#   xs:List[str] = linea.split("___")
#   print(xs[1])

file_handler:TextIO = open("20primeros.txt", "w") #W es write.

i:int = 1
while i <= 20:
    file_handler.write(str(i) + "\n") #\n es salto de línea.
    i = i + 1
    
file_handler.close()