import unittest
import math

from lekcia16 import Kalkulacka

class TestAddFunction(unittest.TestCase):
    def test_add_integers(self):
        calc = Kalkulacka()
        self.assertEqual(calc.sucet(1, 2), 3)

    def test_add_floats(self):
        calc = Kalkulacka()
        self.assertAlmostEqual(calc.sucet(1.1, 2.2), 3.3, places=1)

    def test_devision(self):
        calc = Kalkulacka()
        self.assertEqual(5 / 1, 5)

    def test_division_by_zero(self):
        calc = Kalkulacka()
        with self.assertRaises(ZeroDivisionError):
            result = 5 / 0

    def test_dlzka_odvesny(self):
        calc = Kalkulacka()
        self.assertAlmostEqual(calc.dlzka_odvesny(7, 3), 7.616, places=3)

    def test_quandratic_equasion_zero(self):
        calc = Kalkulacka()
        with self.assertRaises(ZeroDivisionError):
            result = calc.kvadraticka_rovnica(0, 3, 4)

    def test_quadratic_equasion(self):
        calc = Kalkulacka()
        self.assertEqual(calc.kvadraticka_rovnica(6.25,5,1), [-0.4,-0.4])

if __name__ == '__lekcia16__':
    unittest.main()
