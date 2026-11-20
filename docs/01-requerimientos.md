# 01 - Documento de Requerimientos

## Proyecto: SERIES-MATCH

### 1. Descripción general
SERIES-MATCH es un sistema de recomendación y exploración de series que permite consultar un catálogo, buscar series por título, explorar categorías, visualizar las series mejor rankeadas y encontrar relaciones entre ellas.
El sistema utiliza diferentes estructuras de datos y algoritmos para organizar y consultar la información de manera eficiente.

### 2. Requerimientos funcionales
Los requerimientos funcionales describen las operaciones que el sistema debe permitir realizar.
| Código | Requerimiento |
| :--- | :--- |
| RF01 | El sistema debe cargar la información de las series desde un archivo JSON. |
| RF02 | El sistema debe mostrar la cantidad de series disponibles en el catálogo. |
| RF03 | El sistema debe permitir buscar una serie por su título utilizando un árbol AVL. |
| RF04 | El sistema debe mostrar los datos de una serie encontrada, incluyendo título, género y rating. |
| RF05 | El sistema debe mostrar el Top 5 de series con mejor rating mediante una cola de prioridad. |
| RF06 | El sistema debe organizar las series según su género utilizando un árbol general. |
| RF07 | El sistema debe permitir explorar las series pertenecientes a un género determinado. |
| RF08 | El sistema debe realizar un recorrido en amplitud (BFS) sobre el árbol general. |
| RF09 | El sistema debe representar las relaciones entre series mediante un grafo. |
| RF10 | El sistema debe permitir encontrar un camino entre series relacionadas mediante el algoritmo BFS aplicado al grafo. |
| RF11 | El sistema debe permitir explorar las series relacionadas mediante el algoritmo DFS. |
| RF12 | El sistema debe permitir buscar una serie por su título utilizando un árbol binario de búsqueda (BST). |
| RF13 | El sistema debe recomendar series según el género seleccionado por el usuario. |

### 3. Requerimientos no funcionales
Los requerimientos no funcionales describen características de calidad y comportamiento que debe cumplir el sistema.
| Código | Requerimiento |
| :--- | :--- |
| RNF01 | La búsqueda de series por título mediante el árbol AVL debe tener una complejidad temporal de O(log n). |
| RNF02 | El sistema debe mantener organizada la información para facilitar su consulta y actualización. |
| RNF03 | El sistema debe utilizar estructuras de datos adecuadas para cada operación. |
| RNF04 | El sistema debe presentar los resultados de forma clara y ordenada en la terminal. |
| RNF05 | Las búsquedas de títulos y las comparaciones de géneros implementadas deben evitar diferencias entre mayúsculas y minúsculas. |
| RNF06 | El sistema debe permitir ampliar el catálogo mediante la incorporación de nuevos registros en el archivo JSON, respetando el formato establecido. |

### 4. Alcance del sistema
El sistema SERIES-MATCH contempla las siguientes funcionalidades:
- Carga de un catálogo de series desde un archivo JSON.
- Organización de las series mediante un árbol binario de búsqueda (BST).
- Búsqueda de series por título mediante un árbol BST.
- Búsqueda de series mediante un árbol AVL.
- Organización jerárquica de las series por género mediante un árbol general.
- Exploración de categorías y recorridos sobre el árbol general.
- Visualización del Top 5 de series mejor rankeadas mediante una cola de prioridad.
- Recomendación de series según el género seleccionado.
- Representación de las relaciones entre series mediante un grafo.
- Búsqueda de caminos entre series relacionadas mediante BFS.
- Exploración de las relaciones entre series mediante DFS.
- Visualización de información y resultados mediante una interfaz de terminal.

### 5. Fuera de alcance
El sistema no contempla las siguientes funcionalidades:
- Registro, autenticación ni administración de usuarios.
- Creación de perfiles personalizados.
- Recomendaciones basadas en el historial o las preferencias individuales de los usuarios.
- Reproducción de episodios o contenido audiovisual.
- Conexión con plataformas externas de streaming.
- Consulta automática de información desde servicios o APIs externas.
- Administración de películas, ya que el catálogo está destinado a series.
- Interfaz gráfica web o aplicación móvil.

### 6. Restricciones
- La información de las series se obtiene del archivo `datos/series.json`.
- El sistema funciona mediante una interfaz de terminal.
- Las búsquedas y recorridos se realizan utilizando las estructuras de datos implementadas en el proyecto.
- Las relaciones del grafo se establecen entre series que comparten el mismo género.
- El catálogo inicial contiene 20 series.

### 7. Consideraciones finales
SERIES-MATCH busca demostrar la aplicación práctica de distintas estructuras de datos y algoritmos para resolver problemas de organización, búsqueda y recomendación de series.
Cada estructura cumple una función específica dentro del sistema, permitiendo integrar los contenidos trabajados durante los distintos trabajos prácticos.