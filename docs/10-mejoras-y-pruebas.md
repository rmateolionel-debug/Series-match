# Mejoras de la versión final

## Funcionalidades agregadas

### Estadísticas del catálogo

La opción 8 presenta el total de registros, la cantidad de series por género, el rating promedio, la serie mejor valorada y la serie más antigua. Los cálculos se realizan sobre los datos cargados y no modifican el catálogo.

### Recomendaciones con más criterios

La opción 7 permite seleccionar género, cantidad de resultados y rating mínimo. Primero se filtra el catálogo por género y rating; luego se utiliza la cola de prioridad (heap máximo) para ordenar los resultados de mayor a menor rating. La consulta no guarda un perfil permanente del usuario.

## Pruebas automatizadas agregadas

El archivo `tests/test_series_match.py` contiene pruebas de:

- Carga de los 20 registros del catálogo.
- Estadísticas con catálogo normal y vacío.
- Recomendaciones por género, rating mínimo y validación de parámetros.
- Búsqueda y ordenamiento inorder del BST.
- Búsqueda y altura del AVL.
- Extracción de Top N mediante Heap.
- Organización y recorrido del árbol general.
- Recorridos BFS y DFS del grafo, camino inexistente y conexiones del grafo construido desde el catálogo.

Ejecución:

```powershell
py -m unittest discover -s tests -v
```

En esta versión se verificaron 12 pruebas nuevas. También se ejecutaron las 4 pruebas existentes del AVL y las 4 pruebas existentes de la cola de prioridad; todas finalizaron correctamente.
