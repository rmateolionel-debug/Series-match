
import json
from modelos.serie import Serie
from estructuras.arbol_binario import ArbolBST
from estructuras.avl import AVL
from estructuras.arbol_general import ArbolGeneral
from estructuras.grafo import GrafoSeries
from estructuras.cola_prioridad import obtener_top_n

# ==================== COLORES ====================

VIOLETA = "\033[95m"
ROSA = "\033[38;5;218m"
LILA = "\033[38;5;183m"
VERDE = "\033[92m"
ROJO = "\033[91m"
RESET = "\033[0m"


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

nodos_generos = {}

for serie in lista_de_elementos:
    genero = serie.genero

    if genero not in nodos_generos:
        nodo_genero = arbol_general.agregar_hijo(raiz, genero)
        nodos_generos[genero] = nodo_genero

    arbol_general.agregar_hijo(
        nodos_generos[genero],
        serie.titulo
    )


# ==================== GRAFO DE SERIES (TP7) ====================

grafo_series = GrafoSeries()

for serie in lista_de_elementos:
    grafo_series.agregar_vertice(serie.titulo)

for i in range(len(lista_de_elementos)):
    for j in range(i + 1, len(lista_de_elementos)):
        serie1 = lista_de_elementos[i]
        serie2 = lista_de_elementos[j]

        if serie1.genero.lower() == serie2.genero.lower():
            grafo_series.agregar_arista(
                serie1.titulo,
                serie2.titulo
            )


# ==================== ENCABEZADO ====================

print("\n")
print(VIOLETA + "╔══════════════════════════════════════════╗")
print("║                                          ║")
print("║              " + ROSA + "SERIES-MATCH" + VIOLETA + "                ║")
print("║" + RESET + LILA + "       SISTEMA DE RECOMENDACIÓN           " + RESET + VIOLETA + "║")
print("║                                          ║")
print("╚══════════════════════════════════════════╝" + RESET)

print(f"\n  Catálogo disponible: {len(lista_de_elementos)} series")


# ==================== RECOMENDACIONES TOP 5 (TP6) ====================

print("\n" + VIOLETA + "═" * 44)
print("          ★ TOP 5 SERIES RECOMENDADAS")
print("═" * 44 + RESET)

mejores_series = obtener_top_n(lista_de_elementos, 5)

for posicion, serie in enumerate(mejores_series, start=1):
    print(f"\n  {ROSA}{posicion}.{RESET} {serie.titulo}")
    print(f"     Género: {serie.genero}")
    print(f"     Rating: {serie.rating} ★")

print("\n" + VIOLETA + "─" * 44 + RESET)


# ==================== BÚSQUEDA CON AVL ====================

print("\n" + VIOLETA + "═" * 44)
print("             🔎 BUSCAR UNA SERIE")
print("═" * 44 + RESET)

titulo = input("\n  Ingresá el título de una serie: ").strip().lower()

resultado = arbol_avl.buscar(
    titulo,
    clave=lambda e: e.titulo.lower()
)

if resultado is not None:
    print("\n  ✓ SERIE ENCONTRADA")
    print("\n  ┌────────────────────────────────")
    print(f"  │ Título: {resultado.titulo}")
    print(f"  │ Género: {resultado.genero}")
    print(f"  │ Rating: {resultado.rating} ★")
    print("  └────────────────────────────────")
else:
    print("\n  ✗ No se encontró la serie.")

print("\n" + VIOLETA + "─" * 44 + RESET)


# ==================== RECORRIDO INORDER DEL AVL ====================

print("\n" + VIOLETA + "═" * 44)
print("          🌳 RECORRIDO INORDER DEL AVL")
print("═" * 44 + RESET)

for serie in arbol_avl.inorder():
    print(f"\n  {VIOLETA}{serie.titulo}{RESET}")
    print(f"     Género: {serie.genero}")
    print(f"     Rating: {serie.rating} ★")


# ==================== ÁRBOL GENERAL DE SERIES ====================

print("\n" + VIOLETA + "═" * 44)
print("          🌳 ÁRBOL GENERAL DE SERIES")
print("═" * 44 + RESET)

print("Raíz:", arbol_general.raiz.dato)
print("Altura:", arbol_general.altura())
print("Cantidad de nodos:", arbol_general.cantidad_nodos())


# ==================== RECORRIDO EN AMPLITUD ====================

print("\n" + VIOLETA + "═" * 44)
print("       🌳 RECORRIDO EN AMPLITUD")
print("═" * 44 + RESET)

recorrido = arbol_general.amplitud()

print("\n  🏠 SERIES-MATCH")

for genero, nodo_genero in nodos_generos.items():
    if genero in recorrido:
        print(f"\n  📁 {genero.upper()}")

        series = arbol_general.listar_hijos(nodo_genero)

        for serie in series:
            if serie in recorrido:
                print(f"      └── {VIOLETA}{serie}{RESET}")

print("\n" + VIOLETA + "═" * 44 + RESET)


# ==================== BÚSQUEDA DE CATEGORÍAS ====================

print("\n" + VIOLETA + "═" * 44)
print("          🔎 EXPLORAR CATEGORÍAS")
print("═" * 44 + RESET)

genero_buscado = input("\n  Ingresá un género: ").strip().lower()

nodo = None

for genero in nodos_generos:
    if genero.lower().replace("ó", "o") == genero_buscado.replace("ó", "o"):
        nodo = nodos_generos[genero]
        break

if nodo is not None:
    print("\nSeries del género", genero_buscado)

    for titulo in arbol_general.listar_hijos(nodo):
        print("-", titulo)
else:
    print("No se encontró el género.")

print("\n" + VIOLETA + "─" * 44 + RESET)


# ==================== RECORRIDOS DE GRAFOS (TP7) ====================

print("\n" + VIOLETA + "═" * 44)
print("             🌐 RED DE SERIES")
print("═" * 44 + RESET)

print(f"\n  Cantidad de series: {grafo_series.cantidad_vertices()}")
print(f"  Conexiones: {grafo_series.cantidad_aristas()}")


# ==================== CONSULTA BFS ====================

print("\n" + VIOLETA + "─" * 44)
print("       🔎 BFS - SERIE MÁS CERCANA")
print("─" * 44 + RESET)

origen_bfs = "The Boys"

print(f"\n  Consulta: ¿Cuál es la serie relacionada más cercana a {origen_bfs}?")

camino = grafo_series.bfs_mas_cercana(origen_bfs)

if camino:
    print("\n  ✓ RESULTADO")
    print("\n  " + " → ".join(camino))
    print(f"\n  Cantidad de conexiones: {len(camino) - 1}")
else:
    print("\n  No se encontraron series relacionadas.")

# ==================== CONSULTA DFS ====================

print("\n" + VIOLETA + "─" * 44)
print("       🧭 DFS - EXPLORACIÓN EN PROFUNDIDAD")
print("─" * 44 + RESET)

origen_dfs = "Stranger Things"

print(f"\n  Consulta: ¿Qué series están relacionadas con {origen_dfs}?")

recorrido = grafo_series.dfs(origen_dfs)

print("\n  ✓ SERIES EXPLORADAS:\n")

for posicion, titulo in enumerate(recorrido, start=1):
    print(f"    {posicion}. {titulo}")

print(f"\n  Total de series exploradas: {len(recorrido)}")

# ==================== DESPEDIDA ====================

print("\n" + VIOLETA + "═" * 44)
print("       ¡GRACIAS POR UTILIZAR")
print("            SERIES-MATCH!")
print("═" * 44 + RESET)
