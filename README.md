# 🎬 Series-Match

## Descripción

Series-Match es un sistema de consulta y recomendación de series desarrollado en Python, utilizando Programación Orientada a Objetos y diferentes estructuras de datos.

El proyecto permite consultar un catálogo de series y realizar distintas operaciones para facilitar la búsqueda y elección de contenido.

El sistema organiza la información mediante árboles, colas de prioridad y grafos, aplicando algoritmos de búsqueda y recorridos.

## Integrantes

- Milena Iñiguez
- Yasmin Arbona

## Dominio

El dominio elegido para el proyecto es **series y entretenimiento audiovisual**.

Elegimos este dominio porque existe una gran cantidad de series disponibles y muchas veces puede resultar difícil decidir qué mirar.

## Problema que resuelve

Series-Match busca facilitar la búsqueda y elección de series según los intereses del usuario.

Para eso, organiza la información del catálogo y permite buscar títulos, explorar géneros, consultar rankings y encontrar series relacionadas.

## Funcionalidades del sistema

El sistema cuenta con un menú principal que ofrece las siguientes opciones:

1. **Buscar una serie (AVL):** permite buscar una serie por su título utilizando un árbol AVL. Si la encuentra, muestra su información.

2. **Ver Top N series:** permite indicar cuántas series se desean consultar y muestra las mejor valoradas mediante una cola de prioridad implementada con un heap máximo.

3. **Explorar categorías (Árbol General):** permite consultar las series organizadas por género mediante un árbol general.

4. **Ver series relacionadas (DFS):** permite ingresar el título de una serie y explorar las series conectadas con ella mediante el recorrido en profundidad DFS.

5. **Encontrar camino entre dos series (BFS):** permite seleccionar dos series y buscar un camino entre ellas utilizando el recorrido en amplitud BFS.

6. **Recibir recomendación por género:** permite seleccionar un género y muestra las series correspondientes ordenadas según su rating.

7. **Ver recorridos y estructuras:** muestra el recorrido inorder del árbol AVL, información del árbol general, su recorrido en amplitud y datos del grafo. También presenta ejemplos de recorridos BFS y DFS.

8. **Buscar una serie (BST):** permite buscar una serie por su título utilizando el árbol binario de búsqueda. Si la encuentra, muestra su información.

0. **Salir:** finaliza la ejecución del programa.

## Estructuras de datos implementadas

### 1. Árbol Binario de Búsqueda (BST)

Se utiliza para organizar las series según su título.

Permite insertar elementos, realizar búsquedas y recorrer los datos.

En el sistema se utiliza para realizar búsquedas mediante la opción 8 del menú.

Archivo: `estructuras/arbol_binario.py`

### 2. Árbol AVL

Es un árbol binario de búsqueda balanceado que mantiene controlada su altura mediante rotaciones.

Se utiliza para buscar series por título de manera eficiente.

En el sistema se utiliza para realizar búsquedas mediante la opción 1 del menú.

Archivo: `estructuras/avl.py`

### 3. Árbol General

Organiza las series de forma jerárquica.

La raíz representa al sistema Series-Match, sus hijos representan los géneros y cada género contiene las series correspondientes.

Permite explorar las categorías y realizar recorridos en amplitud.

Archivo: `estructuras/arbol_general.py`

### 4. Cola de Prioridad

Se implementa mediante un heap máximo.

Prioriza las series según su rating y permite obtener las de mayor puntuación.

Se utiliza para generar el ranking Top N y ordenar las recomendaciones por género.

Archivo: `estructuras/cola_prioridad.py`

### 5. Grafo

Representa las relaciones entre las series del catálogo.

Cada vértice representa una serie y las aristas conectan aquellas que comparten el mismo género.

El grafo es no dirigido y sin pesos, y utiliza una lista de adyacencia para representar las conexiones.

Se utilizan los siguientes algoritmos:

- **BFS (Breadth-First Search):** permite recorrer el grafo en amplitud y encontrar un camino entre dos series.
- **DFS (Depth-First Search):** permite explorar las series relacionadas en profundidad.

Archivo: `estructuras/grafo.py`

## Clase principal del dominio

### Serie

Representa cada serie del catálogo.

Sus atributos son:

- Título.
- Género.
- Rating.
- Año.
- Cantidad de temporadas.

Archivo: `modelos/serie.py`

## Carga de datos

Los datos del catálogo se encuentran almacenados en un archivo JSON:

`datos/series.json`

El programa carga la información desde ese archivo y crea los objetos de tipo `Serie` para construir las diferentes estructuras de datos.

Actualmente, el catálogo contiene 20 series.

## Organización del proyecto

```text
Series-match/
│
├── main.py
│
├── modelos/
│   └── serie.py
│
├── estructuras/
│   ├── arbol_binario.py
│   ├── avl.py
│   ├── arbol_general.py
│   ├── cola_prioridad.py
│   └── grafo.py
│
├── algoritmos/
│   ├── probar_avl.py
│   ├── probar_bst.py
│   └── probar_cola_prioridad.py
│
├── datos/
│   └── series.json
│
├── docs/
│   ├── 01-requerimientos.md
│   ├── 07-analisis-tp3.md
│   ├── 08-analisis-tp4-tp5.md
│   ├── 09-analisis-tp6.md
│   ├── 09-analisis-tp7.md
│   └── tp0-propuestas.md
│
├── ui/
│   └── terminal.py
│
└── README.md
```

## Cómo ejecutar el proyecto

1. Tener Python instalado.
2. Abrir una terminal en la carpeta principal del proyecto.
3. Ejecutar el siguiente comando:

```powershell
python main.py
```

El menú principal permitirá seleccionar las distintas funcionalidades del sistema.

### Pruebas

**Pruebas automatizadas del AVL:**

```bash
python -m unittest algoritmos.probar_avl -v
```

**Pruebas automatizadas de la cola de prioridad:**

```bash
python -m unittest algoritmos.probar_cola_prioridad -v
```

**Prueba manual del BST:**

```bash
python -m algoritmos.probar_bst
```

Las pruebas automatizadas verifican las rotaciones del AVL y el funcionamiento de la cola de prioridad. La prueba manual del BST permite comprobar la inserción de series, los recorridos y las búsquedas.

## Conclusión

A lo largo del desarrollo de Series-Match incorporamos diferentes estructuras de datos y algoritmos para resolver problemas relacionados con la búsqueda, organización y recomendación de series.

El proyecto permitió aplicar los conceptos de árboles binarios de búsqueda, árboles AVL, árboles generales, colas de prioridad y grafos, integrándolos en un mismo sistema.

De esta manera, logramos construir una aplicación que organiza un catálogo de series y ofrece distintas funcionalidades de consulta y recomendación.

