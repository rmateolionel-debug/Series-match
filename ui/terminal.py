import json

from modelos.serie import Serie


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
    print("1. Buscar serie")
    print("2. Listar todas las series")
    print("3. Filtrar por género")
    print("0. Salir")
    print("-" * 50)


def buscar(series):
    titulo = input("Ingrese el título de la serie: ")

    encontrados = []

    for serie in series:
        if titulo.lower() in serie.titulo.lower():
            encontrados.append(serie)

    print("\n" + "-" * 50)
    print("              RESULTADOS")
    print("-" * 50)

    if encontrados:
        for serie in encontrados:
            print(serie)
    else:
        print("No se encontraron series con ese título.")


def listar(series):
    print("\n" + "-" * 50)
    print("              CATÁLOGO DE SERIES")
    print("-" * 50)

    for i, serie in enumerate(series, 1):
        print(f"{i}. {serie}")


def filtrar(series):
    genero = input("Ingrese el género: ")

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


def main():
    try:
        series = cargar_datos()
    except FileNotFoundError:
        print("Error: no se encontró el archivo datos/series.json.")
        return

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            buscar(series)

        elif opcion == "2":
            listar(series)

        elif opcion == "3":
            filtrar(series)

        elif opcion == "0":
            print("\n¡Gracias por usar SeriesMatch!")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
