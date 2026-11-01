
import unittest

from estructuras.cola_prioridad import ColaPrioridad, obtener_top_n
from modelos.serie import Serie


class TestColaPrioridad(unittest.TestCase):

    def setUp(self):
        self.series = [
            Serie("Dark", "Ciencia ficción", 9.0, 2017, 3),
            Serie("Friends", "Comedia", 8.5, 1994, 10),
            Serie("Breaking Bad", "Drama", 9.5, 2008, 5),
            Serie("The Office", "Comedia", 8.8, 2005, 9)
        ]

    def test_insertar_y_extraer_maximo(self):
        cola = ColaPrioridad()

        for serie in self.series:
            cola.insertar(serie)

        mayor = cola.extraer_maximo()

        self.assertEqual(mayor.titulo, "Breaking Bad")

    def test_construir_heap(self):
        cola = ColaPrioridad()
        cola.construir_heap(self.series)

        mayor = cola.extraer_maximo()

        self.assertEqual(mayor.titulo, "Breaking Bad")

    def test_obtener_top_n(self):
        resultado = obtener_top_n(self.series, 3)

        titulos = [serie.titulo for serie in resultado]

        self.assertEqual(
            titulos,
            ["Breaking Bad", "Dark", "The Office"]
        )

    def test_cola_vacia(self):
        cola = ColaPrioridad()

        self.assertTrue(cola.esta_vacia())
        self.assertIsNone(cola.extraer_maximo())


if __name__ == "__main__":
    unittest.main()

