__author__ = 'Jerad'
import unittest
from Figuras import Figuras

class TestFiguras(unittest.TestCase):

    def setUp(self):
        self.figura=Figuras()

    def test_area_cuadrado_lado_5(self):
        resultado = self.figura.cuadrado(5)
        self.assertEqual(25,resultado)
        
    def test_area_cuadrado_lado_2(self):
        resultado = self.figura.cuadrado(2)
        self.assertEqual(4,resultado)

    def test_area_cuadrado_lado_g(self):
        resultado = self.figura.cuadrado("g")
        self.assertEqual("Dato Incorrecto",resultado)

    def test_area_cuadrado_lado_4(self):
        resultado = self.figura.cuadrado(4.5)
        self.assertEqual(20.25,resultado)


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()


