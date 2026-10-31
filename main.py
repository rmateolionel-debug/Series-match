import json
from modelos.serie import Serie
from estructuras.arbol_binario import ArbolBST
from estructuras.avl import AVL
from estructuras.arbol_general import ArbolGeneral
from estructuras.grafo import GrafoSeries


# ==================== CARGAR SERIES ====================

with open("datos/series.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

lista_de_elementos = []

for elemento in datos:
    serie = Serie(
        elemento["titulo"],
        elemento["genero"],
        elemento["rating"],
        elemento["anio"],
        elemento["temporadas"]
    )
    lista_de_elementos.append(serie)


# ==================== ÁRBOL BST (TP3) ====================

arbol_bst = ArbolBST()

for elemento in lista_de_elementos:
    arbol_bst.insertar(
        elemento,
        clave=lambda e: e.titulo.lower()
    )


# ==================== ÁRBOL AVL (TP4) ====================

arbol_avl = AVL()

for elemento in lista_de_elementos:
    arbol_avl.insertar(
        elemento,
        clave=lambda e: e.titulo.lower()
    )

# ==================== ÁRBOL GENERAL (TP5) ====================

arbol_general = ArbolGeneral()
raiz = arbol_general.insertar_raiz("Series-match")

# Guardar los nodos de los géneros
nodos_generos = {}

for serie in lista_de_elementos:
    genero = serie.genero

    # Crear el género si todavía no existe
    if genero not in nodos_generos:
        nodo_genero = arbol_general.agregar_hijo(raiz, genero)
        nodos_generos[genero] = nodo_genero

    # Agregar la serie como hija de su género
    arbol_general.agregar_hijo(
        nodos_generos[genero],
        serie.titulo
    )
    
# ==================== GRAFO DE SERIES (TP7) ====================

grafo_series = GrafoSeries()

# Agregar todas las series como vértices
for serie in lista_de_elementos:
    grafo_series.agregar_vertice(serie.titulo)

# Conectar las series que comparten género
for i in range(len(lista_de_elementos)):
    for j in range(i + 1, len(lista_de_elementos)):
        serie1 = lista_de_elementos[i]
        serie2 = lista_de_elementos[j]

        if serie1.genero.lower() == serie2.genero.lower():
            grafo_series.agregar_arista(
                serie1.titulo,
                serie2.titulo
            )

# ==================== MOSTRAR RESULTADOS ====================

print("=== SERIES-MATCH ===")

print("Cantidad de series:", len(lista_de_elementos))

print("\n=== COMPARACIÓN BST VS AVL ===")
print("Altura BST:", arbol_bst.altura())
print("Altura AVL:", arbol_avl.altura())


# ==================== BÚSQUEDA CON AVL ====================

print("\n=== BÚSQUEDA DE SERIES CON AVL ===")

titulo = input("Ingrese el título de una serie: ").strip().lower()

resultado = arbol_avl.buscar(
    titulo,
    clave=lambda e: e.titulo.lower()
)

if resultado is not None:
    print("Serie encontrada:", resultado)
else:
    print("No se encontró la serie.")


# ==================== RECORRIDOS AVL ====================

print("\n=== RECORRIDO INORDER DEL AVL ===")

for serie in arbol_avl.inorder():
    print(serie)
    # ==================== RECORRIDOS ÁRBOL GENERAL ====================

print("\n=== ÁRBOL GENERAL DE SERIES ===")

print("Raíz:", arbol_general.raiz.dato)
print("Altura:", arbol_general.altura())
print("Cantidad de nodos:", arbol_general.cantidad_nodos())

print("\n--- Recorrido en amplitud ---")
for elemento in arbol_general.amplitud():
    print(elemento)

print("\n--- Recorrido en profundidad ---")
for elemento in arbol_general.profundidad_preorder():
    print(elemento)


# ==================== BÚSQUEDA DE CATEGORÍAS ====================

print("\n=== EXPLORAR CATEGORÍAS ===")

genero_buscado = input("Ingrese un género: ").strip().lower()

nodo = None

for genero in nodos_generos:
    if genero.lower() == genero_buscado:
        nodo = nodos_generos[genero]
        break

if nodo is not None:
    print("\nSeries del género", genero_buscado)
    for titulo in arbol_general.listar_hijos(nodo):
        print("-", titulo)
else:
    print("No se encontró el género.")
    
# ==================== RECOMENDACIONES CON GRAFOS (TP7) ====================

print("\n=== SERIES RELACIONADAS ===")

print("Vértices:", grafo_series.cantidad_vertices())
print("Aristas:", grafo_series.cantidad_aristas())

titulo_buscado = input(
    "\nIngrese el título de una serie para ver recomendaciones: "
).strip()

# Buscar el título sin distinguir mayúsculas
titulo_original = None

for serie in lista_de_elementos:
    if serie.titulo.lower() == titulo_buscado.lower():
        titulo_original = serie.titulo
        break

if titulo_original is not None:
    relacionadas = grafo_series.obtener_relacionadas(titulo_original)

    if relacionadas:
        print("\nSeries relacionadas con", titulo_original)
        for titulo in relacionadas:
            print("-", titulo)
    else:
        print("Esta serie no tiene conexiones.")
else:
    print("No se encontró la serie.")
