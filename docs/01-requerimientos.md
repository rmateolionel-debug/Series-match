# Documento de Requerimientos – SERIES-MATCH

## 1. Descripción general

SERIES-MATCH es un sistema de consulta y recomendación de series que permite explorar un catálogo, buscar títulos, consultar rankings, recorrer categorías, conocer relaciones entre series y obtener recomendaciones según criterios ingresados por el usuario. Funciona mediante una interfaz de terminal y utiliza estructuras de datos implementadas en Python.

## 2. Requerimientos funcionales

| Código | Requerimiento |
|---|---|
| RF01 | El sistema debe cargar las series desde `datos/series.json`. |
| RF02 | El sistema debe informar la cantidad de series disponibles. |
| RF03 | El sistema debe permitir consultar el catálogo completo con título, género, rating, año y temporadas. |
| RF04 | El sistema debe permitir buscar un título mediante BST o AVL. |
| RF05 | El sistema debe mostrar los datos de la serie encontrada e informar cuando no exista. |
| RF06 | El sistema debe permitir indicar N y mostrar hasta N series ordenadas por rating mediante un heap máximo. |
| RF07 | El sistema debe organizar las series por género mediante un árbol general. |
| RF08 | El sistema debe permitir explorar las series de un género. |
| RF09 | El sistema debe representar las relaciones entre series mediante un grafo no dirigido con lista de adyacencia. |
| RF10 | El sistema debe permitir explorar las series alcanzables desde una serie mediante DFS. |
| RF11 | El sistema debe permitir encontrar el camino con menor cantidad de aristas entre dos series mediante BFS. |
| RF12 | El sistema debe permitir elegir un género, una cantidad y un rating mínimo para recibir recomendaciones ordenadas por rating mediante Heap. |
| RF13 | El sistema debe mostrar estadísticas del catálogo: total de series, distribución por género, rating promedio, serie mejor valorada y serie más antigua. |
| RF14 | El sistema debe validar entradas numéricas de cantidad y rating mínimo, e informar cuando no haya resultados. |

## 3. Requerimientos no funcionales

| Código | Requerimiento |
|---|---|
| RNF01 | La búsqueda en AVL debe mantener el balance del árbol para ofrecer búsqueda O(log n). |
| RNF02 | El sistema debe separar modelos, estructuras, servicios e interfaz. |
| RNF03 | El sistema debe presentar mensajes y resultados claros en la terminal. |
| RNF04 | Las búsquedas por título y las comparaciones de género deben ser insensibles a mayúsculas/minúsculas. |
| RNF05 | Las operaciones deben manejar entradas inválidas sin interrumpir inesperadamente el menú. |
| RNF06 | El catálogo debe poder ampliarse agregando registros que respeten el formato JSON establecido. |
| RNF07 | Las pruebas automatizadas deben poder ejecutarse con la biblioteca estándar de Python. |

## 4. Alcance

El sistema contempla la carga del catálogo, consulta de series, búsquedas BST/AVL, Top N con heap máximo, exploración de categorías con árbol general, recorridos DFS y BFS sobre el grafo, recomendaciones por género y rating mínimo, y estadísticas descriptivas.

## 5. Fuera de alcance

- Registro, autenticación y administración de usuarios.
- Perfiles o historial persistente de preferencias.
- Reproducción de episodios o contenido audiovisual.
- Conexión con plataformas externas de streaming o APIs.
- Interfaz web o aplicación móvil.

## 6. Restricciones y reglas del dominio

- La fuente de datos es `datos/series.json`.
- La aplicación funciona desde la terminal.
- En el grafo, dos series se conectan si comparten género.
- Las recomendaciones se calculan para cada consulta y no se guardan como perfil del usuario.
- El catálogo incluido en la entrega contiene 20 series; puede ampliarse respetando el esquema de datos.
