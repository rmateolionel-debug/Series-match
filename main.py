import json
from modelos.serie import Serie
from estructuras.arbol_binario import ArbolBST


# Cargar datos desde el JSON
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


# Crear árbol binario de búsqueda
arbol = ArbolBST()

for elemento in lista_de_elementos:
    arbol.insertar(elemento, clave=lambda e: e.titulo.lower())
print("Cantidad de series:", len(arbol.inorder()))

resultado = arbol.buscar(
    "breaking bad",
    clave=lambda e: e.titulo.lower()
)

print("Resultado de búsqueda:", resultado)