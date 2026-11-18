
"""
TP7 - Grafos
Proyecto: Series-match

Grafo no dirigido y sin pesos.
Cada vértice representa una serie.
Dos series están conectadas si comparten género.
Representación mediante lista de adyacencia.
"""
from collections import deque

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

    def bfs(self, origen, destino):
        """Busca el camino más corto entre dos series usando BFS."""

        if origen not in self.adyacencias or destino not in self.adyacencias:
            return []

        visitados = {origen}
        cola = deque([origen])
        anteriores = {origen: None}

        while cola:
            actual = cola.popleft()

            if actual == destino:
                camino = []
                while actual is not None:
                    camino.append(actual)
                    actual = anteriores[actual]

                return camino[::-1]

            for vecino in self.adyacencias[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    anteriores[vecino] = actual
                    cola.append(vecino)

        return []

    def dfs(self, origen):
        """Explora las series relacionadas usando DFS."""

        if origen not in self.adyacencias:
            return []

        visitados = set()
        pila = [origen]
        recorrido = []

        while pila:
            actual = pila.pop()

            if actual not in visitados:
                visitados.add(actual)
                recorrido.append(actual)

                for vecino in reversed(self.adyacencias[actual]):
                    if vecino not in visitados:
                        pila.append(vecino)

        return recorrido

    def bfs_mas_cercana(self, origen):
        """Encuentra la serie más cercana usando BFS."""

        if origen not in self.adyacencias:
            return []

        visitados = {origen}
        cola = deque([origen])
        anteriores = {origen: None}

        while cola:
            actual = cola.popleft()

            if actual != origen:
                camino = []

                while actual is not None:
                    camino.append(actual)
                    actual = anteriores[actual]

                return camino[::-1]

            for vecino in self.adyacencias[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    anteriores[vecino] = actual
                    cola.append(vecino)

        return []