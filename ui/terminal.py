
from estructuras.cola_prioridad import obtener_top_n


# ==================== COLORES ====================

VIOLETA = "\033[95m"
ROSA = "\033[38;5;218m"
LILA = "\033[38;5;183m"
VERDE = "\033[92m"
ROJO = "\033[91m"
RESET = "\033[0m"


# ==================== MENÚ ====================

def mostrar_menu():
    print("\n" + VIOLETA + "═" * 44)
    print("                 MENÚ PRINCIPAL")
    print("═" * 44 + RESET)

    print("1. Buscar una serie (AVL)")
    print("2. Ver Top N series")
    print("3. Explorar categorías (Árbol General)")
    print("4. Ver series relacionadas (DFS)")
    print("5. Encontrar camino entre dos series (BFS)")
    print("6. Recibir recomendación por género")
    print("7. Ver recorridos y estructuras")
    print("8. Buscar una serie (BST)")
    print("0. Salir")

    print(VIOLETA + "═" * 44 + RESET)


# ==================== OPCIÓN 1: BÚSQUEDA AVL ====================

def buscar_serie(arbol_avl):
    titulo = input("\nIngresá el título de la serie: ").strip().lower()

    resultado = arbol_avl.buscar(
        titulo,
        clave=lambda elemento: elemento.titulo.lower()
    )

    if resultado is not None:
        print(VERDE + "\nSERIE ENCONTRADA" + RESET)
        print("Título:", resultado.titulo)
        print("Género:", resultado.genero)
        print("Rating:", resultado.rating)
        print("Año:", resultado.año)
        print("Temporadas:", resultado.temporadas)
    else:
        print(ROJO + "\nNo se encontró la serie." + RESET)

# ==================== BÚSQUEDA BST (TP3) ====================

def buscar_serie_bst(arbol_bst):
    titulo = input(
        "\nIngresá el título de la serie: "
    ).strip().lower()

    resultado = arbol_bst.buscar(
        titulo,
        clave=lambda elemento: elemento.titulo.lower()
    )

    if resultado is not None:
        print(VERDE + "\nSERIE ENCONTRADA EN EL BST" + RESET)
        print("Título:", resultado.titulo)
        print("Género:", resultado.genero)
        print("Rating:", resultado.rating)
        print("Año:", resultado.año)
        print("Temporadas:", resultado.temporadas)

    else:
        print(ROJO + "\nNo se encontró la serie." + RESET)
# ==================== OPCIÓN 2: COLA DE PRIORIDAD ====================

def mostrar_top_n(series):
    try:
        cantidad = int(input("\n¿Cuántas series querés ver?: "))

        if cantidad <= 0:
            print("Ingresá un número mayor que cero.")
            return

        mejores_series = obtener_top_n(series, cantidad)

        print("\n" + VIOLETA + "       TOP DE SERIES")
        print("═" * 44 + RESET)

        for posicion, serie in enumerate(mejores_series, start=1):
            print(f"\n{ROSA}{posicion}.{RESET} {serie.titulo}")
            print(f"   Género: {serie.genero}")
            print(f"   Rating: {serie.rating} ★")

    except ValueError:
        print(ROJO + "Tenés que ingresar un número válido." + RESET)


# ==================== OPCIÓN 3: ÁRBOL GENERAL ====================

def explorar_categorias(arbol_general, nodos_generos):
    print("\nGÉNEROS DISPONIBLES:")

    for genero in nodos_generos:
        print("-", genero)

    genero_buscado = input(
        "\nIngresá el género que querés explorar: "
    ).strip().lower()

    nodo = None

    for genero, nodo_genero in nodos_generos.items():
        if genero.lower().replace("ó", "o") == genero_buscado.replace("ó", "o"):
            nodo = nodo_genero
            break

    if nodo is not None:
        print("\nSeries del género:")

        for titulo in arbol_general.listar_hijos(nodo):
            print("-", titulo)
    else:
        print(ROJO + "No se encontró ese género." + RESET)


# ==================== BUSCAR TÍTULO EN EL CATÁLOGO ====================

def buscar_titulo_en_catalogo(series, titulo):
    for serie in series:
        if serie.titulo.lower() == titulo.lower():
            return serie.titulo

    return None


# ==================== OPCIÓN 4: DFS ====================

def mostrar_relacionadas(series, grafo):
    titulo = input(
        "\nIngresá una serie para buscar otras relacionadas: "
    ).strip()

    origen = buscar_titulo_en_catalogo(series, titulo)

    if origen is None:
        print(ROJO + "No se encontró esa serie." + RESET)
        return

    recorrido = grafo.dfs(origen)
    relacionadas = []

    for nombre in recorrido:
        if nombre != origen:
            relacionadas.append(nombre)

    print(f"\nSeries relacionadas con {origen}:")

    if relacionadas:
        for posicion, nombre in enumerate(relacionadas, start=1):
            print(f"{posicion}. {nombre}")
    else:
        print("No se encontraron series relacionadas.")


# ==================== OPCIÓN 5: BFS ====================

def encontrar_camino(series, grafo):
    titulo_origen = input("\nIngresá la serie de origen: ").strip()
    titulo_destino = input("Ingresá la serie de destino: ").strip()

    origen = buscar_titulo_en_catalogo(series, titulo_origen)
    destino = buscar_titulo_en_catalogo(series, titulo_destino)

    if origen is None or destino is None:
        print(ROJO + "No se encontró una o ambas series." + RESET)
        return

    camino = grafo.bfs(origen, destino)

    if camino:
        print("\nCamino más corto encontrado:")
        print(" → ".join(camino))
        print("Cantidad de conexiones:", len(camino) - 1)
    else:
        print(ROJO + "No existe un camino entre esas series." + RESET)


# ==================== OPCIÓN 6: RECOMENDACIONES ====================

def recomendar_por_genero(series):
    print("\nGÉNEROS DISPONIBLES:")

    generos = []

    for serie in series:
        if serie.genero not in generos:
            generos.append(serie.genero)

    for genero in generos:
        print("-", genero)

    genero_buscado = input(
        "\n¿Qué género te interesa?: "
    ).strip().lower()

    seleccionadas = []

    for serie in series:
        if serie.genero.lower().replace("ó", "o") == genero_buscado.replace("ó", "o"):
            seleccionadas.append(serie)

    if not seleccionadas:
        print("No se encontraron series de ese género.")
        return

    recomendadas = obtener_top_n(
        seleccionadas,
        len(seleccionadas)
    )

    print("\nRECOMENDACIONES PARA VOS:")

    for posicion, serie in enumerate(recomendadas, start=1):
        print(
            f"{posicion}. {serie.titulo} - "
            f"Rating: {serie.rating} ★"
        )


# ==================== OPCIÓN 7: RECORRIDOS ====================

def mostrar_recorridos(arbol_avl, arbol_general, nodos_generos, grafo):

    # Recorrido inorder del AVL

    print("\n" + VIOLETA + "═" * 44)
    print("          RECORRIDO INORDER DEL AVL")
    print("═" * 44 + RESET)

    for serie in arbol_avl.inorder():
        print("-", serie.titulo)

    # Información del árbol general

    print("\n" + VIOLETA + "═" * 44)
    print("          ÁRBOL GENERAL DE SERIES")
    print("═" * 44 + RESET)

    print("Raíz:", arbol_general.raiz.dato)
    print("Altura:", arbol_general.altura())
    print("Cantidad de nodos:", arbol_general.cantidad_nodos())

    # Recorrido en amplitud

    print("\nRECORRIDO EN AMPLITUD:")

    recorrido = arbol_general.amplitud()

    for elemento in recorrido:
        print("-", elemento)

    # Información del grafo

    print("\n" + VIOLETA + "═" * 44)
    print("             RED DE SERIES")
    print("═" * 44 + RESET)

    print("Cantidad de series:", grafo.cantidad_vertices())
    print("Conexiones:", grafo.cantidad_aristas())

    # BFS

    origen_bfs = "The Boys"

    print("\nBFS - SERIE MÁS CERCANA")
    print("Origen:", origen_bfs)

    camino = grafo.bfs_mas_cercana(origen_bfs)

    if camino:
        print(" → ".join(camino))
        print("Cantidad de conexiones:", len(camino) - 1)
    else:
        print("No se encontraron series relacionadas.")

    # DFS

    origen_dfs = "Stranger Things"

    print("\nDFS - EXPLORACIÓN EN PROFUNDIDAD")
    print("Origen:", origen_dfs)

    recorrido = grafo.dfs(origen_dfs)

    for posicion, titulo in enumerate(recorrido, start=1):
        print(f"{posicion}. {titulo}")

    print("Total de series exploradas:", len(recorrido))


# ==================== EJECUTAR INTERFAZ ====================

def ejecutar_menu(series, arbol_bst, arbol_avl, arbol_general, nodos_generos, grafo):

    print("\n")
    print(VIOLETA + "╔══════════════════════════════════════════╗")
    print("║                                          ║")
    print("║              " + ROSA + "SERIES-MATCH" + VIOLETA + "                ║")
    print("║" + RESET + LILA + "       SISTEMA DE RECOMENDACIÓN           " + RESET + VIOLETA + "║")
    print("║                                          ║")
    print("╚══════════════════════════════════════════╝" + RESET)

    print(f"\nCatálogo disponible: {len(series)} series")

    while True:
        mostrar_menu()

        opcion = input("\nSeleccioná una opción: ").strip()

        if opcion == "1":
            buscar_serie(arbol_avl)
        
        elif opcion == "2":
            mostrar_top_n(series)

        elif opcion == "3":
            explorar_categorias(arbol_general, nodos_generos)

        elif opcion == "4":
            mostrar_relacionadas(series, grafo)

        elif opcion == "5":
            encontrar_camino(series, grafo)

        elif opcion == "6":
            recomendar_por_genero(series)

        elif opcion == "7":
            mostrar_recorridos(
                arbol_avl,
                arbol_general,
                nodos_generos,
                grafo
            )
        elif opcion == "8":
            buscar_serie_bst(arbol_bst)
        elif opcion == "0":
            print("\n" + VIOLETA + "¡Gracias por utilizar SERIES-MATCH!" + RESET)
            break

        else:
            print(ROJO + "\nOpción inválida. Intentá nuevamente." + RESET)

        input("\nPresioná ENTER para volver al menú...")

