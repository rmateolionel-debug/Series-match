
# Análisis TP6 — Cola de Prioridad (Heap)

## 1. ¿Qué resolvimos?

En este trabajo práctico incorporamos una cola de prioridad al proyecto Series-match para generar un ranking dinámico de las series mejor valoradas.

El objetivo es obtener las 5 series con mayor rating sin necesidad de ordenar todo el catálogo.

## 2. Implementación

Implementamos manualmente una heap binaria utilizando una lista de Python.

Elegimos una **max-heap**, ya que queremos que la serie con mayor rating se encuentre en la raíz y pueda extraerse primero.

Utilizamos el rating como criterio de prioridad.

## 3. Operaciones implementadas

Creamos el archivo `estructuras/cola_prioridad.py`, donde implementamos:

- `prioridad()`: obtiene el rating de una serie.
- `construir_heap()`: construye la heap a partir de una lista de series.
- `insertar()`: agrega una serie y restaura el orden.
- `_subir()`: realiza el filtrado hacia arriba.
- `extraer_maximo()`: elimina y devuelve la serie de mayor prioridad.
- `_bajar()`: restaura el orden después de extraer un elemento.
- `esta_vacia()`: verifica si la cola está vacía.
- `obtener_top_n()`: devuelve las N series con mayor rating.

## 4. Integración en el proyecto

Integramos la estructura en `main.py`, reutilizando las series cargadas desde `datos/series.json`.

El programa muestra las 5 series con mayor rating al iniciar.

El resultado obtenido fue:

1. Breaking Bad — 9.5
2. The Office — 9.0
3. Friends — 8.9
4. Stranger Things — 8.7
5. Black Mirror — 8.7

## 5. Complejidad temporal

- Construir la heap: O(n).
- Insertar un elemento: O(log n).
- Extraer el máximo: O(log n).
- Obtener el Top N: O(n + k log n).

Donde n representa la cantidad total de series y k la cantidad de elementos solicitados.

Elegimos esta estructura porque permite obtener los elementos de mayor prioridad de manera eficiente, especialmente cuando se necesita un Top N pequeño en comparación con el catálogo completo.

## 6. Pruebas realizadas

Creamos el archivo `algoritmos/probar_cola_prioridad.py` utilizando `unittest`.

Realizamos cuatro pruebas para verificar:

- Inserción y extracción del máximo.
- Construcción de la heap.
- Obtención del Top N.
- Comportamiento de la cola vacía.

Las cuatro pruebas finalizaron correctamente.

## 7. Conclusión

Mediante este trabajo práctico incorporamos una heap binaria de máximo al proyecto Series-match.

La implementación permitió generar un ranking de las series mejor valoradas utilizando una estructura de datos que facilita la extracción de elementos según su prioridad.
