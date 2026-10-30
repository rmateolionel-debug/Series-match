import json
from modelos.serie import Serie
from estructuras.avl import AVL
from estructuras.arbol_general import ArbolGeneral


def cargar_datos():
    with open("datos/series.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    series = []

    for dato in datos:
        serie = Serie(
            dato["titulo"],
            dato["genero"],
            dato["rating"],
            dato["anio"],
            dato["temporadas"]
        )
        series.append(serie)

    return series


def mostrar_menu():
    print("=" * 50)
    print("             🎬 SERIESMATCH 🎬")
    print("=" * 50)
    print("1. Buscar serie por título (AVL)")
    print("2. Listar todas las series")
    print("3. Filtrar por género")
    print("4. Explorar categorías (Árbol General)")
    print("0. Salir")
    print("-" * 50)


def buscar(arbol):
    titulo = input("Ingrese el título de la serie: ").strip()

    resultado = arbol.buscar(
        titulo.lower(),
        clave=lambda e: e.titulo.lower()
    )

    print("\n" + "-" * 50)
    print("              RESULTADO")
    print("-" * 50)

    if resultado is not None:
        print(resultado)
    else:
        print("No se encontró una serie con ese título.")


def listar(series):
    print("\n" + "-" * 50)
    print("              CATÁLOGO DE SERIES")
    print("-" * 50)

    for i, serie in enumerate(series, 1):
        print(f"{i}. {serie}")


def filtrar(series):
    genero = input("Ingrese el género: ").strip()

    encontrados = []

    for serie in series:
        if genero.lower() in serie.genero.lower():
            encontrados.append(serie)

    print("\n" + "-" * 50)
    print("              SERIES FILTRADAS")
    print("-" * 50)

    if encontrados:
        for serie in encontrados:
            print(serie)
    else:
        print("No se encontraron series de ese género.")


def explorar_categorias(arbol_general, nodos_generos):
    print("\n" + "-" * 50)
    print("           EXPLORAR CATEGORÍAS")
    print("-" * 50)

    print("Géneros disponibles:")

    for genero in nodos_generos:
        print("-", genero)

    genero_buscado = input(
        "\nIngrese el género que quiere explorar: "
    ).strip().lower()

    nodo_genero = None

    for genero, nodo in nodos_generos.items():
        if genero.lower() == genero_buscado:
            nodo_genero = nodo
            break

    if nodo_genero is not None:
        print("\nSeries del género", nodo_genero.dato)

        for titulo in arbol_general.listar_hijos(nodo_genero):
            print("-", titulo)
    else:
        print("No se encontró ese género.")


def main():
    try:
        series = cargar_datos()

    except FileNotFoundError:
        print("Error: no se encontró datos/series.json.")
        print("Ejecutá el programa desde la carpeta principal.")
        return

    # Crear el AVL para buscar series por título.
    arbol_avl = AVL()

    for serie in series:
        arbol_avl.insertar(
            serie,
            clave=lambda e: e.titulo.lower()
        )

    # Crear el Árbol General para organizar las series por género.
    arbol_general = ArbolGeneral()
    raiz = arbol_general.insertar_raiz("SeriesMatch")

    nodos_generos = {}

    for serie in series:
        genero = serie.genero

        if genero not in nodos_generos:
            nodos_generos[genero] = arbol_general.agregar_hijo(
                raiz, genero
            )

        arbol_general.agregar_hijo(
            nodos_generos[genero],
            serie.titulo
        )

    # Menú principal.
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            buscar(arbol_avl)

        elif opcion == "2":
            listar(series)

        elif opcion == "3":
            filtrar(series)

        elif opcion == "4":
            explorar_categorias(arbol_general, nodos_generos)

        elif opcion == "0":
            print("\n¡Gracias por usar SeriesMatch!")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
