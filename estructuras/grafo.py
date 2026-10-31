
"""
TP7 - Grafos
Proyecto: Series-match

Grafo no dirigido y sin pesos.
Cada vértice representa una serie.
Dos series están conectadas si comparten género.
Representación mediante lista de adyacencia.
"""


class GrafoSeries:
    def __init__(self):
        # Diccionario que almacena las conexiones
        self.adyacencias = {}

    def agregar_vertice(self, serie):
        """Agrega una serie al grafo."""
        if serie not in self.adyacencias:
            self.adyacencias[serie] = []

    def agregar_arista(self, serie1, serie2):
        """Conecta dos series en ambos sentidos."""
        self.agregar_vertice(serie1)
        self.agregar_vertice(serie2)

        if serie1 != serie2:
            if serie2 not in self.adyacencias[serie1]:
                self.adyacencias[serie1].append(serie2)

            if serie1 not in self.adyacencias[serie2]:
                self.adyacencias[serie2].append(serie1)

    def obtener_relacionadas(self, serie):
        """Devuelve las series conectadas."""
        return self.adyacencias.get(serie, [])

    def mostrar_grafo(self):
        """Muestra todas las conexiones."""
        for serie, relacionadas in self.adyacencias.items():
            print(f"{serie} -> {', '.join(relacionadas)}")

    def cantidad_vertices(self):
        return len(self.adyacencias)

    def cantidad_aristas(self):
        # Cada arista aparece dos veces
        return sum(
            len(vecinos) for vecinos in self.adyacencias.values()
        ) // 2
