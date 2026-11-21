# Casos de uso – Series-Match

## Actor

**Usuario:** persona que interactúa con el sistema desde la terminal.

## Diagrama textual de casos de uso

```text
                 SISTEMA SERIES-MATCH

Usuario ─────── (Ver catálogo)
Usuario ─────── (Buscar serie)
                 ├── Buscar mediante BST
                 └── Buscar mediante AVL
Usuario ─────── (Ver Top N series)
                 └── Heap máximo ordenado por rating
Usuario ─────── (Explorar categorías)
                 └── Árbol general: género → series
Usuario ─────── (Ver series relacionadas)
                 └── DFS sobre el grafo
Usuario ─────── (Encontrar camino entre series)
                 └── BFS sobre el grafo
Usuario ─────── (Pedir recomendación por género)
                 └── Filtrar por género y rating mínimo; ordenar con Heap
Usuario ─────── (Consultar estadísticas del catálogo)
                 └── Totales, distribución por género, promedio y extremos
```

## Descripción de los casos de uso

| Código | Caso de uso | Descripción | Estructura o algoritmo |
|---|---|---|---|
| CU01 | Ver catálogo | El usuario consulta todas las series y sus datos principales. | Lista de objetos `Serie` |
| CU02 | Buscar serie | El usuario ingresa un título y elige BST o AVL. El sistema informa si existe y muestra sus datos. | BST / AVL |
| CU03 | Ver Top N | El usuario indica una cantidad y recibe las series con mayor rating. | Heap máximo |
| CU04 | Explorar categorías | El usuario selecciona un género y consulta las series que contiene. | Árbol general |
| CU05 | Ver series relacionadas | El usuario elige una serie y el sistema recorre las series alcanzables desde ella. | Grafo / DFS |
| CU06 | Encontrar camino | El usuario ingresa origen y destino; el sistema busca el camino con menor cantidad de aristas. | Grafo / BFS |
| CU07 | Pedir recomendación | El usuario elige género, cantidad y rating mínimo. El sistema filtra y ordena los resultados. | Filtro + Heap máximo |
| CU08 | Consultar estadísticas | El usuario consulta métricas descriptivas del catálogo cargado. | Recorridos de la colección |

## Flujo principal de recomendación (CU07)

1. El sistema muestra los géneros disponibles.
2. El usuario ingresa un género.
3. El usuario indica cuántas recomendaciones desea.
4. El usuario indica el rating mínimo aceptable, entre 0 y 10.
5. El sistema filtra las series por género y rating mínimo.
6. El sistema utiliza el heap máximo para ordenar por rating.
7. El sistema muestra hasta la cantidad solicitada o todos los resultados coincidentes si hay menos.

## Precondiciones y excepciones

- El catálogo debe poder cargarse desde `datos/series.json`.
- Para buscar, explorar, recomendar o recorrer el grafo, el catálogo debe contener datos.
- Si el usuario ingresa un título inexistente, un género sin coincidencias o un valor numérico inválido, el sistema informa el problema y permite volver al menú.
- Si no existe camino entre dos series, BFS devuelve una lista vacía y el sistema informa que no hay conexión.

## Alcance de las recomendaciones

La recomendación es por consulta: se basa en el género y rating mínimo ingresados en ese momento. El sistema no almacena perfiles, historial ni preferencias persistentes.
