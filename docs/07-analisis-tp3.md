
# Análisis TP3 — Árbol Binario de Búsqueda

## 1. ¿Qué resolvimos?

Incorporamos un **árbol binario de búsqueda (BST)** para resolver la búsqueda de series por **título** de forma más eficiente.

El árbol permite almacenar las series manteniendo un orden según su título y realizar búsquedas utilizando esa estructura.

## 2. Clave de ordenamiento

Utilizamos el **título de la serie** como clave de ordenamiento porque el usuario puede buscar una serie por su título.

Para evitar diferencias entre mayúsculas y minúsculas, utilizamos el título convertido a minúsculas mediante `lower()`.

De esta manera, por ejemplo, buscar `"stranger things"` permite encontrar la serie `"Stranger Things"`.

## 3. Prueba del árbol

Salida de `python algoritmos/probar_bst.py`:

```text
Altura del árbol: 4

--- inorder (ordenado alfabéticamente) ---
  Breaking Bad (Drama) ⭐9.5 - 2008 - 5 temporadas
  Dark (Ciencia Ficción) ⭐8.7 - 2017 - 3 temporadas
  Friends (Comedia) ⭐8.9 - 1994 - 10 temporadas
  Stranger Things (Ciencia Ficción) ⭐8.7 - 2016 - 4 temporadas
  The Office (Comedia) ⭐9.0 - 2005 - 9 temporadas

--- preorder ---
  Stranger Things
  Breaking Bad
  Dark
  Friends
  The Office

--- postorder ---
  Friends
  Dark
  Breaking Bad
  The Office
  Stranger Things

--- búsquedas ---
Buscar 'stranger things': Stranger Things (Ciencia Ficción) ⭐8.7 - 2016 - 4 temporadas
Buscar 'zzz': None
```

La prueba demuestra que el árbol funciona correctamente. El recorrido **inorder** devuelve las series ordenadas alfabéticamente por título.

Además, la búsqueda de `"stranger things"` encuentra correctamente la serie correspondiente, mientras que la búsqueda de `"zzz"` devuelve `None` porque esa serie no existe en el árbol.

La altura obtenida para este conjunto de cinco elementos fue **4**.

## 5. Análisis de complejidad

* **Búsqueda secuencial:** `O(n)`. En el peor caso debe recorrer todos los elementos de la lista hasta encontrar el buscado o determinar que no existe.

* **Búsqueda binaria:** `O(log n)`, siempre que la lista esté ordenada previamente. El proceso de ordenar los datos tiene un costo de `O(n log n)`.

* **Búsqueda en árbol BST:** `O(log n)` en promedio cuando el árbol se encuentra razonablemente balanceado. En el peor caso puede ser `O(n)` si el árbol queda degenerado, comportándose de forma similar a una lista.

* **Inserción en el árbol:** `O(log n)` en promedio y `O(n)` en el peor caso.

* **Recorridos (`inorder`, `preorder` y `postorder`):** `O(n)`, porque cada nodo del árbol se visita una vez.

## 6. Conclusión

A partir de las pruebas realizadas, podemos comparar el comportamiento de los tres métodos de búsqueda: secuencial, binaria y mediante árbol BST.

Con la prueba realizada verificamos que el BST permite organizar las series por título y realizar búsquedas utilizando esa estructura.

**La comparación final de rendimiento se completará con los tiempos reales obtenidos mediante `algoritmos/medir_tiempos.py`.**

## 7. Errores o dudas que tuvimos

Durante la implementación tuvimos que adaptar el ejemplo inicial del BST a la estructura real de nuestro proyecto.

Uno de los cambios principales fue reemplazar la clase de ejemplo `Elemento` por nuestra clase `Serie`, que contiene los atributos `titulo`, `genero`, `rating`, `anio` y `temporadas`.

También tuvimos que utilizar el atributo `titulo` como clave del árbol y aplicar `lower()` para que la búsqueda no dependiera de si el título estaba escrito con mayúsculas o minúsculas.

Otro punto que tuvimos que verificar fue la función `buscar()`, ya que recibe como parámetro el valor a buscar y una función `clave` que indica qué atributo utilizar para realizar la comparación.
