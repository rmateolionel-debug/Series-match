
# Análisis TP7 — Grafos

## 1. ¿Qué resolvimos?

En este trabajo práctico implementamos un grafo para representar las relaciones entre las series de nuestro proyecto Series-match.

El objetivo es permitir que el sistema recomiende series relacionadas a partir de características en común.

Para esta implementación decidimos utilizar el género de cada serie como criterio de conexión.

De esta manera, cuando un usuario busca una serie, el sistema puede mostrar otras que pertenecen al mismo género.

## 2. Modelo del grafo

### Vértices

Cada vértice representa una serie de nuestro catálogo.

Por ejemplo:
- Stranger Things
- Dark
- Black Mirror
- Breaking Bad
- Friends

Actualmente, nuestro grafo contiene 20 vértices, correspondientes a las 20 series almacenadas en el archivo series.json.

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

{
    "Stranger Things": ["Dark", "Black Mirror", "Lost"],
    "Dark": ["Stranger Things", "Black Mirror", "Lost"]
}

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

estructuras/grafo.py

Dentro de este archivo implementamos la clase GrafoSeries.

Sus principales métodos son:

- agregar_vertice(): agrega una serie al grafo.
- agregar_arista(): conecta dos series.
- obtener_relacionadas(): devuelve las series conectadas con otra.
- mostrar_grafo(): muestra las conexiones.
- cantidad_vertices(): devuelve la cantidad de series.
- cantidad_aristas(): devuelve la cantidad de conexiones.

También integramos el grafo en main.py.

El programa recorre las series cargadas desde el archivo JSON y conecta automáticamente aquellas que comparten género.

## 6. Consultas implementadas

Incorporamos una funcionalidad que permite ingresar el título de una serie y consultar las series relacionadas.

Ejemplo:

Serie ingresada: Stranger Things

Resultado:

- Dark
- Black Mirror
- Lost

Estas recomendaciones aparecen porque las cuatro series pertenecen al género Ciencia Ficción.

El sistema también permite conocer la cantidad total de vértices y aristas.

## 7. Pruebas realizadas

Ejecutamos el programa mediante el comando:

py main.py

Obtuvimos los siguientes resultados:

Cantidad de series: 20

Cantidad de vértices: 20

Cantidad de aristas: 22

También realizamos una prueba independiente con tres series y dos conexiones.

Los resultados fueron:

- Stranger Things conectada con Dark.
- Stranger Things conectada con Black Mirror.
- Las conexiones funcionaron en ambos sentidos.
- Se contabilizaron correctamente 3 vértices y 2 aristas.

Todas estas pruebas finalizaron sin errores.

## 8. Complejidad temporal

Agregar un vértice tiene una complejidad promedio O(1), utilizando un diccionario.

Consultar las series relacionadas tiene una complejidad promedio O(1) para acceder a la lista de vecinos.

Construir las conexiones a partir del catálogo tiene una complejidad O(n²), porque se comparan parejas de series para determinar si comparten género.

El espacio utilizado para representar el grafo es O(V + E).

Esta solución es adecuada para el tamaño actual de nuestro catálogo.

## 9. Ventajas y limitaciones

### Ventajas

- Permite representar relaciones entre series.
- Facilita generar recomendaciones.
- Se integra con las estructuras existentes.
- Permite agregar nuevas series y conexiones.
- La representación es sencilla de comprender y mantener.

### Limitaciones

Actualmente, las recomendaciones se basan únicamente en el género.

Esto significa que dos series del mismo género pueden estar conectadas aunque sus historias sean muy diferentes.

Además, las recomendaciones no se ordenan por rating ni por popularidad.

Como mejora futura, podríamos incorporar relaciones con pesos que consideren género, rating y otras características.

## 10. Conclusión

Mediante este trabajo práctico logramos incorporar grafos al proyecto Series-match.

Implementamos un grafo no dirigido y sin pesos utilizando una lista de adyacencia.

Cada vértice representa una serie y cada arista indica que dos series comparten género.

La implementación permitió construir una red de 20 vértices y 22 aristas, además de incorporar una funcionalidad de recomendaciones.

Las pruebas realizadas demostraron que el sistema puede identificar correctamente las series relacionadas.

Con este trabajo ampliamos las funcionalidades de Series-match y aplicamos los conceptos de grafos a un problema práctico de recomendación de contenido.
