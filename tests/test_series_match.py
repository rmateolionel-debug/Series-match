"""Pruebas de integración para las estructuras y servicios de Series-Match."""

import json
import unittest
from pathlib import Path

from modelos.serie import Serie
from estructuras.arbol_binario import ArbolBST
from estructuras.avl import AVL
from estructuras.arbol_general import ArbolGeneral
from estructuras.cola_prioridad import obtener_top_n
from estructuras.grafo import GrafoSeries
from servicios.catalogo import obtener_estadisticas, recomendar_series
from main import construir_grafo, construir_arbol_general


ROOT = Path(__file__).resolve().parents[1]


def cargar_catalogo_prueba():
    with (ROOT / "datos" / "series.json").open(encoding="utf-8") as archivo:
        datos = json.load(archivo)
    return [Serie(d["titulo"], d["genero"], d["rating"], d["anio"], d["temporadas"]) for d in datos]


class TestCatalogo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.series = cargar_catalogo_prueba()

    def test_carga_20_series(self):
        self.assertEqual(len(self.series), 20)

    def test_estadisticas_catalogo(self):
        stats = obtener_estadisticas(self.series)
        self.assertEqual(stats["total"], 20)
        self.assertEqual(sum(stats["por_genero"].values()), 20)
        self.assertAlmostEqual(stats["rating_promedio"], sum(s.rating for s in self.series) / 20)
        self.assertEqual(stats["mejor_valorada"].titulo, "Breaking Bad")
        self.assertEqual(stats["mas_antigua"].titulo, "Friends")

    def test_estadisticas_catalogo_vacio(self):
        stats = obtener_estadisticas([])
        self.assertEqual(stats["total"], 0)
        self.assertIsNone(stats["mejor_valorada"])

    def test_recomendacion_por_genero_ordenada(self):
        resultado = recomendar_series(self.series, "drama", 2, 8.5)
        self.assertEqual(len(resultado), 2)
        self.assertTrue(all(s.genero == "Drama" and s.rating >= 8.5 for s in resultado))
        self.assertGreaterEqual(resultado[0].rating, resultado[1].rating)

    def test_recomendacion_acepta_acento_equivalente(self):
        resultado = recomendar_series(self.series, "ciencia ficcion", 10, 0)
        self.assertEqual(len(resultado), 4)

    def test_recomendacion_valida_parametros(self):
        with self.assertRaises(ValueError):
            recomendar_series(self.series, "Drama", 0, 0)
        with self.assertRaises(ValueError):
            recomendar_series(self.series, "Drama", 2, 11)


class TestEstructuras(unittest.TestCase):
    @staticmethod
    def clave(serie):
        return serie.titulo.lower()

    @classmethod
    def setUpClass(cls):
        cls.series = cargar_catalogo_prueba()

    def test_bst_busqueda_y_orden(self):
        arbol = ArbolBST()
        for serie in self.series:
            arbol.insertar(serie, self.clave)
        encontrada = arbol.buscar("breaking bad", self.clave)
        self.assertEqual(encontrada.titulo, "Breaking Bad")
        self.assertIsNone(arbol.buscar("serie inexistente", self.clave))
        titulos = [s.titulo for s in arbol.inorder()]
        self.assertEqual(titulos, sorted(titulos, key=str.lower))

    def test_avl_busqueda_y_balance(self):
        arbol = AVL()
        for serie in self.series:
            arbol.insertar(serie, self.clave)
        self.assertEqual(arbol.buscar("dark", self.clave).titulo, "Dark")
        self.assertIsNone(arbol.buscar("no existe", self.clave))
        self.assertLessEqual(arbol.altura(), 6)

    def test_heap_top_n(self):
        top = obtener_top_n(self.series, 3)
        self.assertEqual(len(top), 3)
        self.assertEqual(top[0].titulo, "Breaking Bad")
        self.assertGreaterEqual(top[0].rating, top[1].rating)
        self.assertGreaterEqual(top[1].rating, top[2].rating)

    def test_arbol_general_por_genero(self):
        arbol = ArbolGeneral()
        raiz = arbol.insertar_raiz("Series-match")
        drama = arbol.agregar_hijo(raiz, "Drama")
        arbol.agregar_hijo(drama, "Breaking Bad")
        arbol.agregar_hijo(drama, "The Crown")
        self.assertEqual(arbol.listar_hijos(drama), ["Breaking Bad", "The Crown"])
        self.assertEqual(arbol.amplitud(), ["Series-match", "Drama", "Breaking Bad", "The Crown"])

    def test_grafo_real_del_catalogo_y_arbol_de_generos(self):
        grafo = construir_grafo(self.series)
        self.assertIn("Dark", grafo.obtener_relacionadas("Stranger Things"))
        self.assertNotIn("Breaking Bad", grafo.obtener_relacionadas("Stranger Things"))
        camino = grafo.bfs("Stranger Things", "Black Mirror")
        self.assertEqual(camino[0], "Stranger Things")
        self.assertEqual(camino[-1], "Black Mirror")

        arbol, generos = construir_arbol_general(self.series)
        self.assertIn("Drama", generos)
        self.assertIn("Breaking Bad", arbol.listar_hijos(generos["Drama"]))

    def test_grafo_dfs_bfs_y_camino_inexistente(self):
        grafo = GrafoSeries()
        grafo.agregar_arista("Stranger Things", "Dark")
        grafo.agregar_arista("Dark", "Black Mirror")
        self.assertEqual(grafo.bfs("Stranger Things", "Black Mirror"),
                         ["Stranger Things", "Dark", "Black Mirror"])
        self.assertEqual(set(grafo.dfs("Stranger Things")),
                         {"Stranger Things", "Dark", "Black Mirror"})
        self.assertEqual(grafo.bfs("Stranger Things", "Breaking Bad"), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
