import unittest


def suma(num_1, num_2):
    return abs(num_1) + num_2


# es un modulo de python que nos permite generar pruebas
# y la forma para generar prueba es un una clase
class CajaNegratest(unittest.TestCase):  #testcase es un caso de prueba

    def test_suma_dos_positivo(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)  # 15 es el resultado que esperamos

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)

if __name__ == '__main__':
    unittest.main()


