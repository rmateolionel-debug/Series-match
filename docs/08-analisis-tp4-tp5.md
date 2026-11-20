# Análisis TP4 y TP5 — Árbol AVL y Árbol General

## 1. Objetivo

En este análisis se estudian los resultados obtenidos al incorporar el árbol AVL (TP4) y el árbol general o n-ario (TP5) al proyecto SERIES-MATCH.

Se comparan los resultados observados al ejecutar el programa y se relacionan con la complejidad temporal de las operaciones de cada estructura.

## 2. Resultados reales

Los siguientes datos se obtuvieron ejecutando `main.py` con el catálogo del proyecto:

| Indicador | Resultado |
| :--- | ---: |
| Series cargadas | 20 |
| Altura del BST con el orden original del catálogo | 7 |
| Altura del AVL con el orden original del catálogo | 5 |
| Altura del árbol general | 3 |
| Cantidad de nodos del árbol general | 28 |

Los resultados muestran que, para el catálogo utilizado, el árbol AVL obtuvo una altura menor que el BST.

Además, se ejecutaron pruebas automatizadas para verificar las cuatro rotaciones del AVL:

- Rotación izquierda-izquierda.
- Rotación derecha-derecha.
- Rotación izquierda-derecha.
- Rotación derecha-izquierda.

Las cuatro pruebas finalizaron correctamente.

## 3. Análisis de complejidad temporal

### Árbol binario de búsqueda (BST)

En un árbol binario de búsqueda, las operaciones de búsqueda e inserción dependen de la altura del árbol.

- Mejor caso de búsqueda: `O(1)`, cuando el elemento buscado está en la raíz.
- Caso promedio: `O(log n)`, si el árbol está equilibrado.
- Peor caso: `O(n)`, cuando el árbol se encuentra muy desbalanceado.

### Árbol AVL

El árbol AVL mantiene el equilibrio mediante rotaciones simples y dobles después de las inserciones.

- Búsqueda: `O(log n)`.
- Inserción: `O(log n)`.
- Recorridos (inorden, preorden y postorden): `O(n)`.

A diferencia del BST común, el AVL mantiene una altura logarítmica, evitando que las operaciones principales se degraden a `O(n)`.

### Árbol general o n-ario

El árbol general permite organizar la información mediante una estructura jerárquica de nodos y varios hijos.

- Búsqueda de un nodo: `O(n)` en el peor caso, porque puede ser necesario recorrer todos los nodos.
- Recorrido en profundidad (DFS): `O(n)`, porque visita cada nodo una vez.
- Recorrido en anchura (BFS): puede llegar a `O(n²)` en la implementación utilizada, debido a que se emplea `pop(0)` sobre una lista para extraer elementos de la cola. Esta operación requiere desplazar los elementos restantes.

## 4. Conclusión

La incorporación del árbol AVL y del árbol general permitió ampliar las funcionalidades y mejorar la organización de la información del proyecto SERIES-MATCH.

Al comparar el BST y el AVL con los datos obtenidos, se observó que el AVL presentó una altura menor (5 frente a 7), lo que demuestra una mejor organización para el catálogo utilizado.

Además, el árbol general permitió representar las series agrupadas por género mediante una estructura jerárquica. En la ejecución se obtuvieron 28 nodos y una altura de 3.

Las pruebas automatizadas también permitieron comprobar que las cuatro rotaciones del AVL funcionan correctamente.

En conclusión, cada estructura cumple una función diferente: el BST permite realizar búsquedas, el AVL mantiene el equilibrio para mejorar la eficiencia de las operaciones y el árbol general facilita la organización jerárquica de la información.