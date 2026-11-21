# Análisis TP6 — Cola de Prioridad (Heap)

## 1. ¿Qué resolvimos?

En este trabajo práctico incorporamos una cola de prioridad al proyecto Series-match para generar un ranking de las series mejor valoradas.

El objetivo es obtener las N series con mayor rating sin necesidad de ordenar todo el catálogo previamente.

El usuario puede elegir cuántas series desea visualizar desde el menú principal del programa.

## 2. Implementación

Implementamos manualmente una heap binaria utilizando una lista de Python.

Elegimos una **max-heap**, ya que necesitamos que la serie con mayor rating se encuentre en la raíz y pueda extraerse primero.

Utilizamos el atributo `rating` de cada serie como criterio de prioridad.

De esta manera, los elementos con mayor puntuación tienen mayor prioridad.

## 3. Operaciones implementadas

Creamos el archivo `estructuras/cola_prioridad.py`, donde implementamos las siguientes operaciones:

- `construir_heap()`: construye la heap a partir de una lista de series.
- `insertar()`: agrega una serie y restaura el orden de la heap.
- `_subir()`: realiza el filtrado hacia arriba, comparando un elemento con su padre.
- `extraer_maximo()`: elimina y devuelve la serie de mayor prioridad, ubicada en la raíz.
- `_bajar()`: restaura el orden de la heap después de extraer el máximo.
- `esta_vacia()`: verifica si la cola de prioridad está vacía.

También implementamos `obtener_top_n()` para obtener las N series con mayor rating.

Esta función inserta todas las series en la cola de prioridad y luego extrae los elementos de mayor puntuación hasta alcanzar la cantidad solicitada.

## 4. Integración en el proyecto

Integramos la cola de prioridad en el menú principal del proyecto, mediante la opción 2: **Top de series**.

El usuario ingresa la cantidad de series que desea visualizar y el programa muestra los resultados ordenados de mayor a menor rating.

Para cada serie se muestra:

- Título.
- Género.
- Rating.

Si el usuario solicita una cantidad mayor a la cantidad de series disponibles, el programa muestra todas las series existentes en el catálogo.

Por ejemplo, si se solicitan 25 series y el catálogo contiene 20, se muestran las 20 disponibles.

## 5. Complejidad temporal

Las complejidades de las operaciones implementadas son:

| Operación | Complejidad |
|---|---|
| Construir la heap | O(n) |
| Insertar un elemento | O(log n) |
| Extraer el máximo | O(log n) |
| Verificar si está vacía | O(1) |
| Obtener el Top N (implementación actual) | O(n log n + k log n) |

Donde:

- `n` representa la cantidad total de series.
- `k` representa la cantidad de series solicitadas.

La complejidad de obtener el Top N corresponde a la implementación actual: primero se insertan las N series del catálogo una por una y luego se extraen los `k` elementos de mayor prioridad.

Elegimos esta estructura porque permite obtener los elementos con mayor puntuación de manera eficiente, sin tener que ordenar previamente todo el catálogo.

## 6. Pruebas realizadas

Creamos el archivo `algoritmos/probar_cola_prioridad.py` utilizando `unittest`.

Realizamos pruebas para verificar:

- Inserción y extracción del máximo.
- Construcción de la heap.
- Obtención del Top N.
- Comportamiento de la cola vacía.

Las cuatro pruebas finalizaron correctamente.

También realizamos pruebas desde el menú principal para comprobar el funcionamiento de la integración:

- Al solicitar 15 series, el programa devuelve correctamente 15 resultados.
- Al solicitar 25 series, el programa devuelve las 20 disponibles.
- Las series aparecen ordenadas de mayor a menor rating.
- Se muestran correctamente el título, el género y la puntuación de cada serie.

## 7. Conclusión

Mediante este trabajo práctico incorporamos una heap binaria de máximo al proyecto Series-match.

La implementación permitió generar un ranking dinámico de las series mejor valoradas, utilizando el rating como criterio de prioridad.

Además, integramos la estructura al menú principal para que el usuario pueda seleccionar cuántas series desea visualizar.

De esta manera, aplicamos los conceptos de colas de prioridad y heaps en un caso práctico, comprobando su funcionamiento mediante pruebas automatizadas y pruebas desde la interfaz del programa.
