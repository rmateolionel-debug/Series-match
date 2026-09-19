from estructuras.arbol_binario import ArbolBST
from modelos.serie import Serie


def main():
    arbol = ArbolBST()

    # Lo construimos SIN orden, para que el árbol ordene solo
    datos = [
        Serie("Stranger Things", "Ciencia Ficción", 8.7, 2016, 4),
        Serie("Breaking Bad", "Drama", 9.5, 2008, 5),
        Serie("The Office", "Comedia", 9.0, 2005, 9),
        Serie("Dark", "Ciencia Ficción", 8.7, 2017, 3),
        Serie("Friends", "Comedia", 8.9, 1994, 10),
    ]

    for d in datos:
        arbol.insertar(d, clave=lambda e: e.titulo.lower())

    print("Altura del árbol:", arbol.altura())

    print("\n--- inorder (ordenado alfabéticamente) ---")
    for e in arbol.inorder():
        print(" ", e)

    print("\n--- preorder ---")
    for e in arbol.preorder():
        print(" ", e.titulo)

    print("\n--- postorder ---")
    for e in arbol.postorder():
        print(" ", e.titulo)

    print("\n--- búsquedas ---")

    encontrado = arbol.buscar(
        "stranger things",
        clave=lambda e: e.titulo.lower()
    )
    print("Buscar 'stranger things':", encontrado)

    no_encontrado = arbol.buscar(
        "zzz",
        clave=lambda e: e.titulo.lower()
    )
    print("Buscar 'zzz':", no_encontrado)


if __name__ == "__main__":
    main()
