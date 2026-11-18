# Análisis TP7 — Grafos

## 1. ¿Qué resolvimos?

En este trabajo práctico implementamos un grafo para representar las relaciones entre las series de nuestro proyecto Series-match.

El objetivo es permitir que el sistema recomiende series relacionadas a partir de características en común.

Para esta implementación decidimos utilizar el género de cada serie como criterio de conexión.

De esta manera, cuando un usuario busca una serie, el sistema puede mostrar otras que pertenecen al mismo género.

Además, incorporamos los recorridos BFS y DFS para realizar búsquedas y explorar las conexiones de la red.

## 2. Modelo del grafo

### Vértices

Cada vértice representa una serie de nuestro catálogo.

Por ejemplo:
- Stranger Things
- Dark
- Black Mirror
- Breaking Bad
- Friends

Actualmente, nuestro grafo contiene 20 vértices, correspondientes a las 20 series almacenadas en el archivo `series.json`.

### Aristas

Las aristas representan una relación entre dos series.

Decidimos conectar dos series cuando comparten el mismo género.

Por ejemplo, Stranger Things, Dark y Black Mirror pertenecen al género Ciencia Ficción, por lo tanto están conectadas entre sí.

El grafo contiene 22 aristas.

## 3. Tipo de grafo

Implementamos un grafo no dirigido y sin pesos.

### Grafo no dirigido

Elegimos un grafo no dirigido porque las relaciones funcionan en ambos sentidos.

Por ejemplo, si Stranger Things está relacionada con Dark, entonces Dark también está relacionada con Stranger Things.

### Grafo sin pesos

Elegimos un grafo sin pesos porque las conexiones representan únicamente si dos series comparten género.

No necesitamos asignar valores numéricos a las relaciones.

En futuras versiones podríamos incorporar pesos para calcular el nivel de similitud entre dos series.

## 4. Representación del grafo

Utilizamos una lista de adyacencia implementada mediante un diccionario de Python.

Cada clave representa una serie y su valor es una lista con las series relacionadas.

Ejemplo:

```python
{
    "Stranger Things": ["Dark", "Black Mirror", "Lost"],
    "Dark": ["Stranger Things", "Black Mirror", "Lost"]
}
```

### ¿Por qué elegimos una lista de adyacencia?

Elegimos esta representación porque:

- Permite almacenar las conexiones de manera sencilla.
- Es fácil agregar nuevos vértices y aristas.
- Facilita consultar las series relacionadas.
- Evita almacenar conexiones inexistentes.
- Resulta conveniente cuando el grafo tiene pocas conexiones en comparación con la cantidad máxima posible.

Una matriz de adyacencia requiere espacio proporcional al cuadrado de la cantidad de vértices.

En cambio, una lista de adyacencia requiere espacio O(V + E), donde V representa los vértices y E las aristas.

## 5. Implementación

Creamos el archivo:

`estructuras/grafo.py`

Dentro de este archivo implementamos la clase `GrafoSeries`.

Sus principales métodos son:

- `agregar_vertice()`: agrega una serie al grafo.
- `agregar_arista()`: conecta dos series.
- `obtener_relacionadas()`: devuelve las series conectadas con otra.
- `mostrar_grafo()`: muestra las conexiones.
- `cantidad_vertices()`: devuelve la cantidad de series.
- `cantidad_aristas()`: devuelve la cantidad de conexiones.
- - `bfs_mas_cercana()`: encuentra automáticamente la serie relacionada más cercana utilizando BFS.
- `dfs()`: explora las series conectadas en profundidad.

También integramos el grafo en `main.py`.

El programa recorre las series cargadas desde el archivo JSON y conecta automáticamente aquellas que comparten género.

## 6. Consultas implementadas

Definimos dos consultas para aplicar los recorridos de grafos a nuestro sistema de recomendación.

### Consulta mediante BFS

Utilizamos BFS (Breadth-First Search) para encontrar la serie relacionada más cercana a una serie de origen.

**Caso de uso:**

¿Cuál es la serie relacionada más cercana a The Boys?

El programa utiliza el método `bfs_mas_cercana(origen)`, que recibe la serie de origen y encuentra automáticamente la primera serie relacionada a menor distancia.

El algoritmo utiliza una cola para visitar los vértices por niveles y un diccionario de predecesores para reconstruir el camino encontrado.

**Resultado obtenido:**

`The Boys → La Casa de Papel`

Cantidad de conexiones: 1.

### Consulta mediante DFS

Utilizamos DFS (Depth-First Search) para explorar en profundidad todas las series alcanzables desde una serie de origen.

**Caso de uso:**

¿Qué series están relacionadas con Stranger Things?

El programa utiliza el método `dfs(origen)`, que recibe la serie inicial y devuelve el recorrido de las series visitadas.

El algoritmo utiliza una pila para recorrer el grafo en profundidad y un conjunto de visitados para evitar procesar varias veces el mismo vértice.

**Resultado obtenido:**

- Stranger Things
- Dark
- Black Mirror
- Lost

## 7. Pruebas realizadas

Ejecutamos el programa mediante el comando:

```powershell
python main.py
```

Obtuvimos los siguientes resultados:

- Cantidad de series: 20.
- Cantidad de vértices: 20.
- Cantidad de aristas: 22.

También realizamos una prueba independiente con tres series y dos conexiones.

Los resultados fueron:

- Stranger Things conectada con Dark.
- Stranger Things conectada con Black Mirror.
- Las conexiones funcionaron en ambos sentidos.
- Se contabilizaron correctamente 3 vértices y 2 aristas.

Además, probamos los recorridos de grafos desde el programa principal:

- BFS encontró la serie relacionada más cercana a The Boys: La Casa de Papel.
- DFS exploró las series alcanzables desde Stranger Things: Dark, Black Mirror y Lost.

Las pruebas realizadas finalizaron sin errores.

## 8. Complejidad temporal

Agregar un vértice tiene una complejidad promedio O(1), utilizando un diccionario.

Consultar las series relacionadas tiene una complejidad promedio O(1) para acceder a la lista de vecinos, sin contar el tiempo necesario para mostrar sus elementos.

Construir las conexiones a partir del catálogo tiene una complejidad O(n²), porque se comparan parejas de series para determinar si comparten género.

Los recorridos BFS y DFS tienen una complejidad temporal O(V + E), ya que cada vértice se visita como máximo una vez y se recorren sus conexiones.

El espacio utilizado para representar el grafo es O(V + E).

BFS y DFS utilizan además un espacio auxiliar O(V) para almacenar los vértices visitados y las estructuras necesarias para realizar el recorrido.

## 9. Comparación entre BFS y DFS

| Característica | BFS | DFS |
|---|---|---|
| Nombre | Búsqueda en amplitud | Búsqueda en profundidad |
| Recorrido | Por niveles | En profundidad |
| Estructura utilizada | Cola | Pila |
| Objetivo | Encontrar caminos más cortos en cantidad de aristas | Explorar conexiones |
| Complejidad temporal | O(V + E) | O(V + E) |
| Espacio auxiliar | O(V) | O(V) |

### ¿Cuándo conviene utilizar cada uno?

BFS conviene cuando necesitamos encontrar el camino con menor cantidad de aristas entre dos vértices. BFS conviene cuando necesitamos encontrar los vértices más cercanos a uno de origen, considerando la menor cantidad de aristas. Por eso lo utilizamos para encontrar automáticamente la serie relacionada más cercana a The Boys.

DFS conviene cuando queremos explorar las conexiones de un vértice y recorrer los elementos alcanzables en profundidad.

Aunque ambos algoritmos permiten recorrer grafos, se diferencian en el orden de visita y en la estructura auxiliar que utilizan.

## 10. Ventajas y limitaciones

### Ventajas

- Permite representar relaciones entre series.
- Facilita generar recomendaciones.
- Se integra con las estructuras existentes.
- Permite agregar nuevas series y conexiones.
- La representación es sencilla de comprender y mantener.
- Incorpora dos algoritmos de recorrido para explorar la red.

### Limitaciones

Actualmente, las recomendaciones se basan únicamente en el género.

Esto significa que dos series del mismo género pueden estar conectadas aunque sus historias sean muy diferentes.

Además, las recomendaciones no se ordenan por rating ni por popularidad.

Como mejora futura, podríamos incorporar relaciones con pesos que consideren género, rating y otras características.

## 11. Conclusión

Mediante este trabajo práctico logramos incorporar grafos al proyecto Series-match.

Implementamos un grafo no dirigido y sin pesos utilizando una lista de adyacencia.

Cada vértice representa una serie y cada arista indica que dos series comparten género.

La implementación permitió construir una red de 20 vértices y 22 aristas, además de incorporar funcionalidades de consulta y recomendación.

También implementamos BFS y DFS, que permiten encontrar caminos más cortos y explorar las conexiones de la red.

De esta manera, aplicamos los conceptos de grafos y sus recorridos a un problema práctico de recomendación de contenido.

