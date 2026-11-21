# 🎬 Series-Match

## Descripción

Series-Match es un sistema de consulta y recomendación de series desarrollado en Python. Integra árboles BST y AVL, un árbol general, una cola de prioridad implementada mediante heap máximo y un grafo no dirigido representado con listas de adyacencia.

El programa funciona desde una interfaz de terminal y carga su catálogo desde `datos/series.json`.

## Integrantes

- Milena Iñiguez
- Yasmin Arbona

## Funcionalidades del menú

1. **Ver catálogo de series:** lista todas las series disponibles con su género, rating, año y cantidad de temporadas.
2. **Buscar una serie:** permite elegir entre búsqueda mediante BST (TP3) o AVL (TP4).
3. **Ver Top N series:** el usuario indica cuántas series quiere consultar; el heap máximo devuelve las series con mayor rating, ordenadas de mayor a menor.
4. **Explorar categorías:** permite seleccionar un género y listar sus series mediante el árbol general.
5. **Ver series relacionadas:** utiliza DFS para recorrer las series conectadas a la serie elegida. Las conexiones representan series que comparten género.
6. **Encontrar camino entre dos series:** utiliza BFS para encontrar el camino más corto, en cantidad de aristas, entre dos series conectadas.
7. **Recibir recomendación por género:** el usuario elige un género, una cantidad de resultados y un rating mínimo. El sistema filtra y ordena las recomendaciones mediante el heap máximo.
8. **Ver estadísticas del catálogo:** muestra información general del catálogo, como la cantidad de series, los géneros disponibles y sus estadísticas.
0. **Salir:** finaliza el programa.

## Estructuras de datos

- **Árbol BST:** permite realizar búsquedas por título y ejecutar recorridos del árbol binario de búsqueda.
- **Árbol AVL:** permite realizar búsquedas por título utilizando un árbol binario balanceado. Implementa rotaciones simples y dobles para mantener el equilibrio.
- **Árbol general:** organiza las series mediante una jerarquía de raíz → géneros → títulos de series.
- **Heap máximo / Cola de prioridad:** permite obtener las series con mayor rating y ordenar los resultados de las recomendaciones.
- **Grafo no dirigido:** cada vértice representa una serie y existe una arista entre dos series cuando comparten el mismo género. Se implementan los recorridos DFS y BFS.

## Datos del catálogo

El archivo `datos/series.json` contiene los registros del catálogo. Cada registro incluye:

- Título.
- Género.
- Rating.
- Año de lanzamiento.
- Cantidad de temporadas.

El programa transforma los registros del archivo JSON en objetos de la clase `Serie`.

## Estructura del proyecto

```text
Series-match/
├── algoritmos/
│   ├── probar_avl.py
│   ├── probar_bst.py
│   └── probar_cola_prioridad.py
├── datos/
│   └── series.json
├── docs/
│   ├── 01-requerimientos.md
│   ├── 02-docs.casosdeuso.md
│   ├── 03-diagrama-clases.md
│   ├── 04-diagrama-datos.md
│   ├── 07-analisis-tp3.md
│   ├── 08-analisis-tp4-tp5.md
│   ├── 09-analisis-tp6.md
│   ├── 09-analisis-tp7.md
│   └── 10-mejoras-y-pruebas.md
├── estructuras/
│   ├── arbol_binario.py
│   ├── arbol_general.py
│   ├── avl.py
│   ├── cola_prioridad.py
│   └── grafo.py
├── modelos/
│   └── serie.py
├── servicios/
│   └── catalogo.py
├── tests/
│   └── test_series_match.py
├── ui/
│   └── terminal.py
├── main.py
├── .gitignore
└── README.md
```

## Requisitos y ejecución

- Python 3.10 o superior recomendado.
- No requiere instalar dependencias externas, ya que utiliza la biblioteca estándar de Python.

Para ejecutar el programa, abrir una terminal desde la carpeta principal del proyecto y ejecutar:

```powershell
py main.py
```

También se puede ejecutar mediante:

```bash
python main.py
```

## Pruebas automatizadas

Para ejecutar las pruebas desde la carpeta principal del proyecto:

```powershell
py -m unittest discover -s tests -v
```

También se pueden ejecutar los scripts de prueba de las estructuras:

```powershell
py algoritmos/probar_avl.py
py algoritmos/probar_bst.py
py algoritmos/probar_cola_prioridad.py
```

Las pruebas permiten verificar el funcionamiento de las estructuras de datos, sus operaciones y los recorridos implementados.

## Alcance y limitaciones

- Las recomendaciones se calculan para cada consulta a partir del género, la cantidad de resultados y el rating mínimo elegidos. No se guarda un perfil ni un historial del usuario.
- Las relaciones del grafo se definen por compartir género. Por este motivo, dos series de géneros diferentes pueden no tener relación ni un camino entre ellas.
- El sistema funciona mediante una aplicación de terminal.
- No incluye interfaz web, reproducción de contenido ni conexión con plataformas externas.
