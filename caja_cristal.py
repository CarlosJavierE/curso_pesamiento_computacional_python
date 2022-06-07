import unittest


def es_mayor_de_edad(edad):
    if edad >= 18:
        # aqui la opcion debia ser True pero so cambio para hacer el test
        return False
    else:
        return False

# generamos nuestro test de pruebas
class PruebaDeCristalTest(unittest.TestCase):
    # se empieza a escribir los test
    def test_es_mayor_de_edad(self):
        edad = 20

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, True)

    def test_es_menor_de_edad(self):
        edad = 15

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)


if __name__ == '__main__':
    unittest.main()
    # unittest.main(verbosity=2)
    # se puede poner esto para tener mas detalle del test