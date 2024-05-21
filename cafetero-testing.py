import unittest
from cafetero import filtrarCAFE_BD

class TestfiltrarCAFE_BD(unittest.TestCase):
    def test_vacío(self): 
        self.assertEqual(filtrarCAFE_BD(''),'')  
    def test_abecedario(self):
        self.assertEqual(filtrarCAFE_BD('abcdefghijklmnñopqrstuvwxyz'),'') 
        self.assertEqual(filtrarCAFE_BD('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'),'ABCDEF')
        self.assertEqual(filtrarCAFE_BD('abcCdEeCfghFijklmAAAnñopqrDDstuvwBxyz'),'CECFAAADDB')   
    def test_minusculas(self): 
        self.assertEqual(filtrarCAFE_BD('cafe'),'') 
        self.assertEqual(filtrarCAFE_BD('CcBDbdaAfFEe'),'CBDAFE') 
    def test_numeros(self):self.assertEqual(filtrarCAFE_BD('0123456789'),'')
    def test_numeros_y_letras(self): 
        self.assertEqual(filtrarCAFE_BD('0D1C234A567F89EB'),'DCAFEB')
        self.assertEqual(filtrarCAFE_BD('012B3C456Cce90FE4Adddb'),'BCCFEA')     
    def test_puntuacion(self):self.assertEqual(filtrarCAFE_BD(',.;:¿?¡!_-\|/"'),'')
        self.assertEqual(filtrarCAFE_BD('E.C:¿?!!_-?|\D/'),'ECD')                                
    def test_repetidas(self): self.assertEqual(filtrarCAFE_BD('AA'),'AA')
    def test_espacio(self): self.assertEqual(filtrarCAFE_BD('CC A E B F'),'CCAEBF')
        
unittest.main()