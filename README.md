# 🎬 Series-Match

## Descripción

Series-Match es un sistema de consulta y recomendación de series desarrollado en Python. Integra árboles BST y AVL, un árbol general, una cola de prioridad implementada mediante heap máximo y un grafo no dirigido representado con listas de adyacencia.

El programa funciona desde una interfaz de terminal y carga su catálogo desde `datos/series.json`.

## Integrantes

- Milena Iñiguez
- Yasmin Arbona

## Funcionalidades del menú

1. **Ver catálogo:** lista las series con género, rating, año y temporadas.
2. **Buscar una serie:** permite elegir búsqueda mediante BST (TP3) o AVL (TP4).
3. **Ver Top N:** el usuario indica cuántas series quiere consultar; el heap máximo las devuelve ordenadas por rating.
4. **Explorar categorías:** permite seleccionar un género y listar sus series mediante el árbol general.
5. **Ver series relacionadas:** recorre con DFS el componente del grafo conectado a la serie elegida. Las conexiones representan series que comparten género.
6. **Encontrar camino:** utiliza BFS para encontrar el camino más corto en cantidad de aristas entre dos series conectadas.
7. **Recibir recomendación por género:** el usuario elige género, cantidad y rating mínimo; el sistema filtra y ordena los resultados con el heap máximo.
8. **Ver estadísticas:** muestra cantidad total, cantidad por género, rating promedio, serie mejor valorada y serie más antigua.
0. **Salir:** finaliza el programa.

## Estructuras de datos

- **BST:** búsqueda por título y recorridos del árbol binario de búsqueda.
- **AVL:** búsqueda por título en un árbol binario balanceado.
- **Árbol general:** jerarquía raíz → géneros → títulos de series.
- **Heap máximo / cola de prioridad:** ranking Top N y ordenamiento de recomendaciones por rating.
- **Grafo:** cada vértice representa una serie; existe una arista no dirigida entre series del mismo género. DFS explora las relacionadas y BFS encuentra caminos mínimos en cantidad de conexiones.

## Datos del catálogo

El archivo `datos/series.json` contiene los registros del catálogo. Cada registro incluye título, género, rating, año y cantidad de temporadas. El programa transforma los registros en objetos de la clase `Serie`.

## Estructura del proyecto

```text
Series-match/
├── algoritmos/                 # Scripts de prueba existentes
├── datos/
│   └── series.json
├── docs/                       # Requerimientos y análisis de los TP
├── estructuras/
│   ├── arbol_binario.py
│   ├── arbol_general.py
│   ├── avl.py
│   ├── cola_prioridad.py
│   └── grafo.py
├── modelos/
│   └── serie.py
├── servicios/
│   └── catalogo.py             # Estadísticas y recomendaciones
├── tests/
│   └── test_series_match.py    # Pruebas automatizadas
├── ui/
│   └── terminal.py
├── main.py
├── .gitignore
└── README.md
```

## Requisitos y ejecución

- Python 3.10 o superior recomendado.
- No requiere instalar dependencias externas: utiliza la biblioteca estándar de Python.

Desde la carpeta principal del proyecto, ejecutar:

```powershell
py main.py
```

## Pruebas automatizadas

Ejecutar desde la carpeta principal:

```powershell
py -m unittest discover -s tests -v
```

Las pruebas cubren carga del catálogo, estadísticas, recomendaciones, BST, AVL, heap, árbol general y recorridos BFS/DFS del grafo.

## Alcance y limitaciones

- Las recomendaciones se calculan para cada consulta a partir del género, cantidad y rating mínimo elegidos. No se guarda un perfil ni un historial del usuario.
- Las relaciones del grafo se definen por compartir género; por eso, dos series de géneros diferentes pueden no tener un camino entre sí.
- El sistema es una aplicación de terminal; no incluye interfaz web, reproducción de contenido ni conexión con plataformas externas.
