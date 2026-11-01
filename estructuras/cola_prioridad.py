
class ColaPrioridad:
    def __init__(self):
        self.elementos = []

    def construir_heap(self, series):
        self.elementos = list(series)

        for i in range(len(self.elementos) // 2 - 1, -1, -1):
            self._bajar(i)

    def esta_vacia(self):
        return len(self.elementos) == 0

    def insertar(self, serie):
        self.elementos.append(serie)
        self._subir(len(self.elementos) - 1)

    def _subir(self, indice):
        while indice > 0:
            padre = (indice - 1) // 2

            if self.elementos[indice].rating > self.elementos[padre].rating:
                self.elementos[indice], self.elementos[padre] = (
                    self.elementos[padre],
                    self.elementos[indice]
                )
                indice = padre
            else:
                break

    def extraer_maximo(self):
        if self.esta_vacia():
            return None

        if len(self.elementos) == 1:
            return self.elementos.pop()

        maximo = self.elementos[0]
        self.elementos[0] = self.elementos.pop()
        self._bajar(0)

        return maximo

    def _bajar(self, indice):
        cantidad = len(self.elementos)

        while True:
            izquierdo = 2 * indice + 1
            derecho = 2 * indice + 2
            mayor = indice

            if (izquierdo < cantidad and
                self.elementos[izquierdo].rating >
                self.elementos[mayor].rating):
                mayor = izquierdo

            if (derecho < cantidad and
                self.elementos[derecho].rating >
                self.elementos[mayor].rating):
                mayor = derecho

            if mayor == indice:
                break

            self.elementos[indice], self.elementos[mayor] = (
                self.elementos[mayor],
                self.elementos[indice]
            )

            indice = mayor

def obtener_top_n(series, n):
    cola = ColaPrioridad()

    for serie in series:
        cola.insertar(serie)

    resultado = []

    cantidad = min(n, len(series))

    for i in range(cantidad):
        resultado.append(cola.extraer_maximo())

    return resultado
