import unittest 
from cafetero import filtrar_solo_CAFE

class TestFiltrar_solo_CAFE(unittest.TestCase):
   
    def test_abecedario(self):
        #minusculas
        self.assertEqual(filtrar_solo_CAFE('aábcdeéfghiéjklmnñoópqrstuúüvwxyz'),'') 
        #mayusculas
        self.assertEqual(filtrar_solo_CAFE('ABÁCDEÉFGHIíJKLMNÑOÓPQRSTUÚÜVWXYZ'),'ACEF')
        #ambas
        self.assertEqual(filtrar_solo_CAFE('aábcdeéfghiéjklmnñoópqrstuúüvwxyzABÁCDEÉFGHIíJKLMNÑOÓPQRSTUÚÜVWXYZ'),'ACEF') 
  
    def test_numeros(self):
        self.assertEqual(filtrar_solo_CAFE('0123456789CAFE'),('CAFE'))
        self.assertEqual(filtrar_solo_CAFE('0123456789'),(''))
            
    def test_puntuacion(self):
        #solo puntuacion
        self.assertEqual(filtrar_solo_CAFE(',;:.¿?¡!…( )— –«»*''”§'), (''))
        #puntuacion y letras
        self.assertEqual(filtrar_solo_CAFE(',;:.¿?¡!…( )—E–«C»*''”§'), ('EC'))
        
    def test_repetidas(self): 
            self.assertEqual(filtrar_solo_CAFE('AA'),'AA')
            
    def test_espacio(self):
            self.assertEqual(filtrar_solo_CAFE('CC A E F'),('CCAEF'))
unittest.main()

import unittest
from cafetero import filtrarCAFE_BD

class TestfiltrarCAFE_BD(unittest.TestCase):
    def test_vacío(self): 
        self.assertEqual(filtrarCAFE_BD(''),'')  
    def test_abecedario(self):
        #minusculas
        self.assertEqual(filtrarCAFE_BD('aábcdeéfghiéjklmnñoópqrstuúüvwxyz'),'') 
        #mayusculas
        self.assertEqual(filtrarCAFE_BD('ABÁCDEÉFGHIíJKLMNÑOÓPQRSTUÚÜVWXYZ'),'ABCDEF')
        #ambas
        self.assertEqual(filtrarCAFE_BD('aábcdeéfghiéjklmnñoópqrstuúüvwxyzABÁCDEÉFGHIíJKLMNÑOÓPQRSTUÚÜVWXYZ'),'ABCDEF')   

    def test_numeros(self):
        self.assertEqual(filtrarCAFE_BD('0123456789'),'')
        self.assertEqual(filtrarCAFE_BD('0123456789CAFEBD'),'CAFEBD')
    def test_puntuacion(self): 
        self.assertEqual(filtrarCAFE_BD(',;:.¿?¡!…( )—–«»*''”§'),'') 
        #puntuacion y letras 
        self.assertEqual(filtrarCAFE_BD(',;:.¿?¡!…()—E–«C»*B"§'),'ECB')
    def test_repetidas(self): 
        self.assertEqual(filtrarCAFE_BD('AA'),'AA')
    def test_espacio(self): 
        self.assertEqual(filtrarCAFE_BD('CC A E B F'),'CCAEBF')
        
unittest.main()

import unittest
from cafetero import es_cafetero 

class TestEsCafetero(unittest.TestCase):
   
    def test_falso(self):
    #LetrasCAFE_Repetidas
        self.assertEqual(es_cafetero(831470), False)
    #Ocurrencias de BD
        self.assertEqual(es_cafetero(831467), False)
        self.assertEqual(es_cafetero(831469), False)
    #Orden incorrecto
        self.assertEqual(es_cafetero(45036), False)

    def test_verdadero(self):
        self.assertEqual(es_cafetero(51966), True)
    #Con numeros y letras
        self.assertEqual(es_cafetero(29994894), True)
        
    def test_cero(self):
        self.assertEqual (es_cafetero(0), False)

unittest.main()

import unittest
from cafetero import n_esimo_cafetero

class Test_n_esimo_cafetero(unittest.TestCase):
    
    def test_posiciones(self):
        self.assertEqual(n_esimo_cafetero(1), 51966)
        self.assertEqual(n_esimo_cafetero(10), 641790)
        self.assertEqual(n_esimo_cafetero(11), 789246)
        self.assertEqual(n_esimo_cafetero(20), 826110)
        self.assertEqual(n_esimo_cafetero(21), 827646)
        self.assertEqual(n_esimo_cafetero(51), 1100542)
        self.assertEqual(n_esimo_cafetero(60), 1690366)
        
unittest.main() 

import unittest
from cafetero import cafeteros_entre

class TestCafeteros_entre(unittest.TestCase):
    
    def test_listavacia(self):
        self.assertEqual(cafeteros_entre(1, 100), [])
    def test_lista(self):
        #Cafetero como borde del intervalo
        self.assertEqual(cafeteros_entre(51966, 51970), [51966])
        self.assertEqual(cafeteros_entre(51966, 117502), [51966, 117502])
        
unittest.main()