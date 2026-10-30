Análisis TP4 y TP5 
#1. Objetivo
En este análisis se estudian los resultados obtenidos al incorporar el árbol AVL (TP4) y el árbol general o n-ario (TP5) al proyecto SeriesMatch. Se comparan los resultados observados al ejecutar el programa y se relacionan con la complejidad temporal de las operaciones.
##2. Resultados reales
Los siguientes datos se obtuvieron ejecutando main.py con el catálogo del proyecto:
| Indicador                                    | Resultado |
|   |---:                                      |
| Series cargadas                                   | 20 |
| Altura del BST con el orden original del catálogo | 7 |
| Altura del AVL con el orden original del catálogo | 5 |
| Altura del árbol general                          | 3 |
| Cantidad de nodos del árbol general               | 28 |
------------------------------------------------------------
Medición de búsqueda
La función comparar_bst_vs_avl realiza 1000 búsquedas del primer elemento insertado. Se repitió la medición cinco veces y se tomó la mediana de los tiempos:
Indicador	                        |BST|	             | AVL
Búsquedas realizadas por medición	|1000|	           |1000
Mediana del tiempo medido	       |0,173 ms|	       |0,559 ms
Estos tiempos corresponden a una ejecución concreta y a un conjunto pequeño de 20 elementos.
No deben interpretarse como una demostración de que el BST sea mejor. La altura sí muestra claramente la ventaja de balanceo del AVL en el caso ordenado.
##3. Análisis de complejidad temporal
| Estructura | Operación | Complejidad          | Justificación |
|         ---|    ---|          -- |                           -|
| BST        | Inserción | O(h); peor caso O(n) | Se recorre desde la     raíz hasta encontrar la posición. Si queda degenerado, la altura puede ser n. |
| BST         | Búsqueda | O(h); peor caso O(n) | La búsqueda sigue una rama según la clave. |
| BST          | Recorridos inorder, preorder y postorder | O(n) | Cada nodo se visita una vez. |
| BST |   Cálculo de altura | O(n) | Se visitan los nodos para calcular la altura máxima. |
| AVL | Inserción | O(log n) | El árbol se mantiene balanceado y puede necesitar una rotación en el camino de regreso. |
| AVL | Búsqueda | O(log n) | El balance garantiza una altura logarítmica. |
| AVL | Recorridos inorder, preorder y postorder | O(n) | Cada nodo se visita una vez. |
| AVL | Consulta de altura | O(1) | La altura está almacenada en la raíz y se devuelve directamente. |
| Árbol general | Agregar un hijo a un nodo padre ya conocido | O(1) | Se crea el nodo y se agrega al final de la lista de hijos. |
| Árbol general | Búsqueda por amplitud (`buscar`) | O(n²) en esta implementación | Puede visitar n nodos y usa `pop(0)` sobre una lista; desplazar los elementos cuesta tiempo. |
| Árbol general | Búsqueda recursiva (`buscar_recursivo`) | O(n) | En el peor caso visita todos los nodos. |
| Árbol general | Recorrido en amplitud (`amplitud`) | O(n²) en esta implementación | Visita todos los nodos, pero la cola usa `pop(0)` de una lista. |
| Árbol general | Recorridos en profundidad preorder y postorder | O(n) | Cada nodo se visita una sola vez. |
| Árbol general | Altura y cantidad de nodos | O(n) | Para obtener esos valores se recorren los nodos del árbol. |
##4. Conclusión
Los resultados muestran que el AVL mantiene una altura menor que el BST cuando ambos reciben los mismos datos en orden alfabético: con 20 series, el BST alcanza altura 20 y el AVL altura 5. Esto confirma la utilidad del balanceo y de las rotaciones implementadas en el TP4, especialmente cuando los datos llegan ordenados.
Con el orden original del catálogo también se observó una altura menor en el AVL (5) que en el BST (7). Aunque los tiempos medidos para 20 elementos fueron muy pequeños y variaron entre ejecuciones, la complejidad teórica permite concluir que el AVL ofrece búsquedas e inserciones O(log n) de forma garantizada, mientras que el BST puede degradarse a O(n) si queda desbalanceado.
En conclusión, el AVL es conveniente para buscar series por título manteniendo un rendimiento predecible; el árbol general es apropiado para organizar y explorar categorías jerárquicas; y el BST es una estructura más simple, pero puede perder eficiencia cuando las inserciones generan un árbol muy desbalanceado.