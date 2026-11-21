# Análisis TP7 – Grafos

**Proyecto: SERIES-MATCH**

## 1. Objetivo

En este trabajo se incorporó un grafo para representar las relaciones entre las series del catálogo de SERIES-MATCH.

Cada vértice representa una serie y dos series se conectan mediante una arista cuando comparten el mismo género.

Se implementó un grafo no dirigido y sin pesos, utilizando una lista de adyacencia como representación. También se incorporaron los algoritmos BFS (búsqueda en amplitud) y DFS (búsqueda en profundidad) para explorar las relaciones y encontrar caminos entre series.

## 2. Implementación del grafo

La implementación se encuentra en el archivo `estructuras/grafo.py`, dentro de la clase `GrafoSeries`.

Se utilizó un diccionario de Python para representar la lista de adyacencia. Cada clave representa una serie y su valor es una lista con las series conectadas.

### Características

- **No dirigido:** las conexiones se almacenan en ambos sentidos.
- **Sin pesos:** las aristas no tienen valores asociados.
- **Lista de adyacencia:** cada serie mantiene una lista de sus series relacionadas.
- **Criterio de conexión:** dos series se conectan cuando comparten el mismo género.

### Métodos implementados

| Método | Descripción |
|---|---|
| `agregar_vertice(serie)` | Agrega una serie al grafo si todavía no existe. |
| `agregar_arista(serie1, serie2)` | Conecta dos series en ambos sentidos, evitando conexiones duplicadas. |
| `obtener_relacionadas(serie)` | Devuelve la lista de series conectadas a una serie. |
| `mostrar_grafo()` | Muestra las conexiones de todas las series. |
| `cantidad_vertices()` | Devuelve la cantidad de vértices del grafo. |
| `cantidad_aristas()` | Cuenta las conexiones sin duplicarlas. |
| `bfs(origen, destino)` | Busca el camino más corto entre dos series. |
| `dfs(origen)` | Explora las series relacionadas mediante un recorrido en profundidad. |
| `bfs_mas_cercana(origen)` | Encuentra la primera serie relacionada a menor distancia mediante BFS. |

## 3. Construcción e integración

La construcción del grafo se realiza en `main.py`, mediante la función `construir_grafo(series)`.

Primero se agrega cada título como vértice. Luego, mediante dos ciclos `for`, se recorren los pares de series y se comparan sus géneros.

La comparación se realiza utilizando `lower()`, para que no dependa de las mayúsculas o minúsculas.

Cuando dos series comparten género, se agrega una arista entre ellas mediante `agregar_arista()`.

El grafo se construye al iniciar el programa y se pasa a la interfaz del menú para utilizar sus operaciones.

## 4. Resultados obtenidos

Al utilizar el catálogo de `datos/series.json`, compuesto por 20 series, se obtuvieron los siguientes resultados:

| Indicador | Resultado |
|---|---:|
| Cantidad de series (vértices) | 20 |
| Cantidad de géneros | 7 |
| Cantidad de conexiones (aristas) | 22 |

### Conexiones por género

Las conexiones se generan entre todos los pares de series que comparten un mismo género.

| Género | Cantidad de series | Conexiones |
|---|---:|---:|
| Ciencia Ficción | 4 | 6 |
| Drama | 4 | 6 |
| Comedia | 3 | 3 |
| Terror | 3 | 3 |
| Acción | 3 | 3 |
| Romance | 2 | 1 |
| Suspenso | 1 | 0 |
| **Total** | **20** | **22** |

Por ejemplo, un género con cuatro series genera seis conexiones, ya que cada serie se conecta con las otras tres, sin contar dos veces la misma arista.

Como el grafo es no dirigido, cada conexión se almacena en las listas de adyacencia de ambos vértices. Por ese motivo, el método `cantidad_aristas()` suma las conexiones almacenadas y divide el resultado por dos.

## 5. Algoritmos de recorrido

### 5.1. Búsqueda en amplitud (BFS)

El algoritmo BFS permite encontrar el camino con menor cantidad de aristas entre dos vértices de un grafo no ponderado.

Se implementó utilizando una cola (`deque`) para procesar primero los vértices descubiertos anteriormente.

Además, se utiliza un conjunto de vértices visitados para evitar recorrer repetidamente los mismos nodos y un diccionario llamado `anteriores` para reconstruir el camino encontrado.

**Integración en el menú:**

La opción 5 permite ingresar una serie de origen y otra de destino. El programa valida que ambas existan en el catálogo y ejecuta `bfs(origen, destino)`.

Si existe un camino, muestra las series que lo componen y la cantidad de conexiones. Si no existe, informa que no se encontró un camino.

También se utiliza `bfs_mas_cercana()` en la opción 7 para encontrar la primera serie relacionada a menor distancia desde un origen establecido.

**Ejemplo con el catálogo:**

Origen: The Boys.

Resultado:

The Boys → La Casa de Papel

Cantidad de conexiones: 1.

Este resultado corresponde a la búsqueda de la serie más cercana mediante `bfs_mas_cercana()`. No es una búsqueda con destino previamente elegido.

### 5.2. Búsqueda en profundidad (DFS)

El algoritmo DFS permite explorar los vértices de un grafo avanzando en profundidad antes de retroceder.

Se implementó utilizando una pila y un conjunto de vértices visitados.

**Integración en el menú:**

La opción 4 permite ingresar una serie y mostrar las demás series alcanzables mediante DFS, sin incluir el origen en la lista de resultados.

También se utiliza en la opción 7 para mostrar un recorrido de ejemplo desde una serie establecida.

**Ejemplo con el catálogo:**

Origen: Stranger Things.

Recorrido obtenido:

1. Stranger Things
2. Dark
3. Black Mirror
4. Lost

El recorrido permite observar cómo el algoritmo explora las conexiones entre las series que comparten género.

## 6. Análisis de complejidad

Se considera:

- `V`: cantidad de vértices.
- `E`: cantidad de aristas.
- `grado(v)`: cantidad de vecinos de un vértice.

| Operación | Complejidad | Justificación |
|---|---|---|
| Agregar vértice | O(1) promedio | Inserción y consulta en un diccionario. |
| Agregar arista | O(grado(u) + grado(v)) | Se comprueba que las series no estén ya conectadas recorriendo sus listas de vecinos. |
| Obtener relacionadas | O(1) promedio | Acceso a la lista mediante la clave del diccionario. |
| Cantidad de vértices | O(1) | Se utiliza `len()` sobre el diccionario. |
| Cantidad de aristas | O(V + E) | Se recorren las listas de adyacencia y se suman sus longitudes. |
| Construcción del grafo | O(n²) | Se comparan todos los pares de series del catálogo. |
| BFS | O(V + E) | Cada vértice y cada arista se procesan como máximo una cantidad constante de veces. |
| DFS | O(V + E) | Cada vértice y cada arista se recorren durante la exploración. |

El espacio utilizado por la representación del grafo es O(V + E), debido al almacenamiento de los vértices y sus conexiones.

Los algoritmos BFS y DFS utilizan además estructuras auxiliares cuyo espacio adicional es O(V).

## 7. Comparación entre BFS y DFS

| Característica | BFS | DFS |
|---|---|---|
| Estrategia | Explora por niveles. | Explora en profundidad. |
| Estructura utilizada | Cola (`deque`). | Pila. |
| Aplicación en el proyecto | Encontrar caminos con menor cantidad de conexiones. | Explorar las series relacionadas. |
| Complejidad | O(V + E) | O(V + E) |

Ambos algoritmos permiten recorrer el grafo, pero tienen diferentes objetivos dentro del proyecto.

BFS resulta adecuado para encontrar caminos con la menor cantidad de conexiones en un grafo no ponderado, mientras que DFS permite explorar las relaciones en profundidad.

## 8. Ventajas y limitaciones

**Ventajas:**

- Permite representar las relaciones entre series de manera organizada.
- Facilita la búsqueda de caminos entre dos series.
- Permite explorar las series relacionadas mediante BFS y DFS.
- La lista de adyacencia evita almacenar una matriz completa de conexiones.
- La estructura puede ampliarse incorporando nuevas series y relaciones.

**Limitaciones:**

- Las conexiones se establecen únicamente por género.
- No se consideran otros criterios de similitud entre series.
- Todas las conexiones tienen la misma importancia, ya que el grafo no utiliza pesos.
- La construcción compara todos los pares de series, por lo que su costo aumenta cuadráticamente con el tamaño del catálogo.

Como posible mejora futura, se podrían incorporar otros criterios para establecer relaciones entre series.

## 9. Conclusión

La incorporación del grafo permitió representar las relaciones entre las series del catálogo mediante conexiones basadas en sus géneros.

Se implementó una estructura no dirigida y sin pesos, utilizando listas de adyacencia, con 20 vértices y 22 aristas para los datos actuales del proyecto.

Además, la implementación de BFS y DFS permitió agregar funcionalidades para encontrar caminos entre series y explorar sus relaciones.

De esta manera, el grafo complementa las demás estructuras de datos utilizadas en SERIES-MATCH y amplía las posibilidades de exploración del catálogo.

