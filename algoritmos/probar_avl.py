import unittest
from estructuras.avl import AVL


class ProbarAVL(unittest.TestCase):

    def crear_arbol(self, datos):
        arbol = AVL()

        for dato in datos:
            arbol.insertar(dato, clave=lambda x: x)

        return arbol

    # Caso 1: Izquierda-Izquierda (rotación simple derecha)
    def test_rotacion_izquierda_izquierda(self):
        arbol = self.crear_arbol([30, 20, 10])

        self.assertEqual(arbol.raiz.dato, 20)
        self.assertEqual(arbol.raiz.izquierdo.dato, 10)
        self.assertEqual(arbol.raiz.derecho.dato, 30)
        self.assertEqual(arbol.altura(), 2)

    # Caso 2: Derecha-Derecha (rotación simple izquierda)
    def test_rotacion_derecha_derecha(self):
        arbol = self.crear_arbol([10, 20, 30])

        self.assertEqual(arbol.raiz.dato, 20)
        self.assertEqual(arbol.raiz.izquierdo.dato, 10)
        self.assertEqual(arbol.raiz.derecho.dato, 30)
        self.assertEqual(arbol.altura(), 2)

    # Caso 3: Izquierda-Derecha (rotación doble)
    def test_rotacion_izquierda_derecha(self):
        arbol = self.crear_arbol([30, 10, 20])

        self.assertEqual(arbol.raiz.dato, 20)
        self.assertEqual(arbol.raiz.izquierdo.dato, 10)
        self.assertEqual(arbol.raiz.derecho.dato, 30)
        self.assertEqual(arbol.altura(), 2)

    # Caso 4: Derecha-Izquierda (rotación doble)
    def test_rotacion_derecha_izquierda(self):
        arbol = self.crear_arbol([10, 30, 20])

        self.assertEqual(arbol.raiz.dato, 20)
        self.assertEqual(arbol.raiz.izquierdo.dato, 10)
        self.assertEqual(arbol.raiz.derecho.dato, 30)
        self.assertEqual(arbol.altura(), 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)