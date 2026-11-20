# 🎬 Series-Match

## Descripción

Series-Match es un sistema de consulta y recomendación de series desarrollado en Python utilizando Programación Orientada a Objetos y diferentes estructuras de datos.

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

Para ello, organiza la información del catálogo y permite buscar títulos, explorar géneros, consultar rankings y encontrar series relacionadas.

## Funcionalidades

El sistema cuenta con las siguientes funcionalidades:

1. **Buscar una serie:** permite buscar una serie por título utilizando un árbol AVL.
2. **Ver Top N series:** muestra las series mejor valoradas mediante una cola de prioridad.
3. **Explorar categorías:** permite consultar las series organizadas por género mediante un árbol general.
4. **Ver series relacionadas:** utiliza DFS para explorar las series conectadas con una serie de origen.
5. **Encontrar camino entre dos series:** utiliza BFS para encontrar el camino más corto entre dos series.
6. **Recibir recomendaciones por género:** muestra series de un género seleccionado, ordenadas por rating.
7. **Buscar una serie en el BST:** el árbol binario de búsqueda también se encuentra implementado y permite realizar búsquedas por título.

## Estructuras de datos implementadas

### 1. Árbol Binario de Búsqueda (BST)

Se utiliza para organizar las series según su título.

Permite insertar elementos, realizar búsquedas y recorrer los datos.

Archivo: `estructuras/arbol_binario.py`

### 2. Árbol AVL

Es un árbol binario de búsqueda balanceado que permite mantener una altura controlada.

Se utiliza para buscar series por título de manera eficiente.

Archivo: `estructuras/avl.py`

### 3. Árbol General

Organiza las series de forma jerárquica.

La raíz representa al sistema Series-Match, sus hijos representan los géneros y cada género contiene las series correspondientes.

Archivo: `estructuras/arbol_general.py`

### 4. Cola de Prioridad

Se implementa mediante un heap máximo.

Permite obtener las series con mayor rating y generar el ranking Top N.

Archivo: `estructuras/cola_prioridad.py`

### 5. Grafo

Representa las relaciones entre las series del catálogo.

Cada vértice representa una serie y las aristas conectan aquellas que comparten el mismo género.

Se utilizan los algoritmos:

- **BFS:** encuentra el camino más corto entre dos series.
- **DFS:** explora las series relacionadas en profundidad.

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

Los datos de prueba se encuentran almacenados en un archivo JSON:

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
│   ├── 07-analisis-tp3.md
│   ├── 08-analisis-tp4-tp5.md
│   ├── 09-analisis-tp6.md
│   └── 09-analisis-tp7.md
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

## Pruebas

El proyecto incluye pruebas para verificar el funcionamiento de las estructuras implementadas.

Los archivos de pruebas se encuentran dentro de la carpeta `algoritmos`.

Para ejecutar las pruebas unitarias de AVL:

```powershell
python -m unittest algoritmos.probar_avl -v
```

Para ejecutar las pruebas de la cola de prioridad:

```powershell
python -m unittest algoritmos.probar_cola_prioridad -v
```

También se realizaron pruebas manuales desde el menú principal para comprobar las búsquedas, los recorridos, las recomendaciones y el funcionamiento de las estructuras.

## Conclusión

A lo largo del desarrollo de Series-Match incorporamos diferentes estructuras de datos y algoritmos para resolver problemas relacionados con la búsqueda, organización y recomendación de series.

El proyecto permitió aplicar los conceptos de árboles binarios, árboles AVL, árboles generales, colas de prioridad y grafos, integrándolos en un mismo sistema.

De esta manera, logramos construir una aplicación que organiza un catálogo de series y ofrece distintas funcionalidades de consulta y recomendación.

