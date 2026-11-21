from estructuras.cola_prioridad import obtener_top_n
from servicios.catalogo import obtener_estadisticas, recomendar_series
from servicios.catalogo import obtener_estadisticas, recomendar_series
from servicios.catalogo import obtener_estadisticas, recomendar_series
# ==================== COLORES ====================
VIOLETA = "\033[95m"
ROSA = "\033[38;5;218m"
LILA = "\033[38;5;183m"
VERDE = "\033[92m"
ROJO = "\033[91m"
RESET = "\033[0m"
# ==================== MENÚ PRINCIPAL ====================

def mostrar_menu():
    print("\n" + VIOLETA + "═" * 44)
    print("                 MENÚ PRINCIPAL")
    print("═" * 44 + RESET)

    print("1. Ver catálogo de series")
    print("2. Buscar una serie")
    print("3. Ver Top N series")
    print("4. Explorar categorías (Árbol General)")
    print("5. Ver series relacionadas (DFS)")
    print("6. Encontrar camino entre dos series (BFS)")
    print("7. Recibir recomendación por género")
    print("8. Ver estadísticas del catálogo")
    print("0. Salir")

    print(VIOLETA + "═" * 44 + RESET)

# ==================== CATÁLOGO COMPLETO ====================
def mostrar_catalogo(series):
    print("\n" + VIOLETA + "═" * 44)
    print("             CATÁLOGO DE SERIES")
    print("═" * 44 + RESET)

    for posicion, serie in enumerate(series, start=1):
        print(f"\n{ROSA}{posicion}. {serie.titulo}{RESET}")
        print(f"   Género: {serie.genero}")
        print(f"   Rating: {serie.rating} ★")
        print(f"   Año: {serie.anio}")
        print(f"   Temporadas: {serie.temporadas}")

    print("\n" + VIOLETA + "═" * 44 + RESET)
    print(f"Total de series: {len(series)}")

# ==================== SUBMENÚ DE BÚSQUEDA ====================
def mostrar_submenu_busqueda():
    print("\n" + VIOLETA + "═" * 44)
    print("              BUSCAR UNA SERIE")
    print("═" * 44 + RESET)

    print("1. Buscar con árbol BST (TP3)")
    print("2. Buscar con árbol AVL (TP4/TP5)")
    print("0. Volver")

    print(VIOLETA + "═" * 44 + RESET)

# ==================== BÚSQUEDA AVL ====================
def buscar_serie(arbol_avl):
    titulo = input(
        "\nIngresá el título de la serie: "
    ).strip().lower()

    resultado = arbol_avl.buscar(
        titulo,
        clave=lambda elemento: elemento.titulo.lower()
    )

    if resultado is not None:
        print(VERDE + "\nSERIE ENCONTRADA" + RESET)
        print("Título:", resultado.titulo)
        print("Género:", resultado.genero)
        print("Rating:", resultado.rating)
        print("Año:", resultado.anio)
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
        print("Año:", resultado.anio)
        print("Temporadas:", resultado.temporadas)
    else:
        print(ROJO + "\nNo se encontró la serie." + RESET)
# ==================== TOP N SERIES ====================

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

# ==================== ÁRBOL GENERAL ====================

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
# ==================== SERIES RELACIONADAS (DFS) ====================

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
# ==================== CAMINO ENTRE SERIES (BFS) ====================
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
# ==================== RECOMENDACIONES POR GÉNERO ====================
def recomendar_por_genero(series):
    print("\nGÉNEROS DISPONIBLES:")
    generos = sorted({serie.genero for serie in series}, key=str.casefold)
    for genero in generos:
        print("-", genero)

    genero_buscado = input("\n¿Qué género te interesa?: ").strip()
    if not genero_buscado:
        print(ROJO + "Tenés que ingresar un género." + RESET)
        return

    try:
        cantidad = int(input("¿Cuántas recomendaciones querés?: ").strip())
        rating_minimo = float(input("Rating mínimo (0 a 10, por ejemplo 8): ").strip().replace(",", "."))
        recomendadas = recomendar_series(series, genero_buscado, cantidad, rating_minimo)
    except ValueError as error:
        print(ROJO + f"Dato inválido: {error}" + RESET)
        return

    print("\nRECOMENDACIONES SEGÚN TUS CRITERIOS:")
    if not recomendadas:
        print("No hay series que coincidan con ese género y rating mínimo.")
        return

    for posicion, serie in enumerate(recomendadas, start=1):
        print(f"{posicion}. {serie.titulo} | Rating: {serie.rating} ★ | Año: {serie.anio}")


def mostrar_estadisticas(series):
    """Presenta un resumen descriptivo del catálogo."""
    datos = obtener_estadisticas(series)
    print("\n" + VIOLETA + "═" * 44)
    print("           ESTADÍSTICAS DEL CATÁLOGO")
    print("═" * 44 + RESET)
    print(f"Total de series: {datos['total']}")
    print(f"Rating promedio: {datos['rating_promedio']:.2f} / 10")
    print("\nSeries por género:")
    for genero, cantidad in datos["por_genero"].items():
        print(f"- {genero}: {cantidad}")

    mejor = datos["mejor_valorada"]
    antigua = datos["mas_antigua"]
    if mejor:
        print(f"\nMejor valorada: {mejor.titulo} ({mejor.rating} ★)")
        print(f"Más antigua: {antigua.titulo} ({antigua.anio})")

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
            mostrar_catalogo(series)

        elif opcion == "2":

            while True:
                mostrar_submenu_busqueda()

                opcion_busqueda = input(
                    "\nSeleccioná una opción: "
                ).strip()

                if opcion_busqueda == "1":
                    buscar_serie_bst(arbol_bst)

                elif opcion_busqueda == "2":
                    buscar_serie(arbol_avl)

                elif opcion_busqueda == "0":
                    break

                else:
                    print(ROJO + "\nOpción inválida." + RESET)

        elif opcion == "3":
            mostrar_top_n(series)

        elif opcion == "4":
            explorar_categorias(arbol_general, nodos_generos)

        elif opcion == "5":
            mostrar_relacionadas(series, grafo)

        elif opcion == "6":
            encontrar_camino(series, grafo)

        elif opcion == "7":
            recomendar_por_genero(series)

        elif opcion == "8":
            mostrar_estadisticas(series)

        elif opcion == "0":
            print(
                "\n" + VIOLETA +
                "¡Gracias por utilizar SERIES-MATCH!" + RESET
            )
            break

        else:
            print(ROJO + "\nOpción inválida. Intentá nuevamente." + RESET)

        if opcion != "0":
            input("\nPresioná ENTER para volver al menú...")
