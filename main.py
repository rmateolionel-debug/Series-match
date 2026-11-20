
import json

from modelos.serie import Serie
from estructuras.arbol_binario import ArbolBST
from estructuras.avl import AVL
from estructuras.arbol_general import ArbolGeneral
from estructuras.grafo import GrafoSeries

from ui.terminal import ejecutar_menu


# ==================== CARGAR SERIES ====================

def cargar_series():
    with open("datos/series.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    series = []

    for elemento in datos:
        serie = Serie(
            elemento["titulo"],
            elemento["genero"],
            elemento["rating"],
            elemento["anio"],
            elemento["temporadas"]
        )

        series.append(serie)

    return series


# ==================== ÁRBOL BST (TP3) ====================

def construir_bst(series):
    arbol_bst = ArbolBST()

    for serie in series:
        arbol_bst.insertar(
            serie,
            clave=lambda elemento: elemento.titulo.lower()
        )

    return arbol_bst


# ==================== ÁRBOL AVL (TP4) ====================

def construir_avl(series):
    arbol_avl = AVL()

    for serie in series:
        arbol_avl.insertar(
            serie,
            clave=lambda elemento: elemento.titulo.lower()
        )

    return arbol_avl


# ==================== ÁRBOL GENERAL (TP5) ====================

def construir_arbol_general(series):
    arbol_general = ArbolGeneral()

    raiz = arbol_general.insertar_raiz("Series-match")

    nodos_generos = {}

    for serie in series:
        genero = serie.genero

        if genero not in nodos_generos:
            nodo_genero = arbol_general.agregar_hijo(
                raiz,
                genero
            )

            nodos_generos[genero] = nodo_genero

        arbol_general.agregar_hijo(
            nodos_generos[genero],
            serie.titulo
        )

    return arbol_general, nodos_generos


# ==================== GRAFO DE SERIES (TP7) ====================

def construir_grafo(series):
    grafo = GrafoSeries()

    # Agregar los vértices

    for serie in series:
        grafo.agregar_vertice(serie.titulo)

    # Conectar las series que comparten género

    for i in range(len(series)):
        for j in range(i + 1, len(series)):

            serie1 = series[i]
            serie2 = series[j]

            if serie1.genero.lower() == serie2.genero.lower():
                grafo.agregar_arista(
                    serie1.titulo,
                    serie2.titulo
                )

    return grafo


# ==================== PROGRAMA PRINCIPAL ====================

def main():

    try:
        lista_de_elementos = cargar_series()

    except FileNotFoundError:
        print("Error: no se encontró datos/series.json.")
        print("Ejecutá el programa desde la carpeta principal.")
        return

    # Construir las estructuras

    arbol_bst = construir_bst(lista_de_elementos)

    arbol_avl = construir_avl(lista_de_elementos)

    arbol_general, nodos_generos = construir_arbol_general(
        lista_de_elementos
    )

    grafo_series = construir_grafo(lista_de_elementos)

    # Iniciar la interfaz

    ejecutar_menu(
    lista_de_elementos,
    arbol_bst,
    arbol_avl,
    arbol_general,
    nodos_generos,
    grafo_series
)


if __name__ == "__main__":
    main()


