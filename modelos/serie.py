class Serie:
    def __init__(self, titulo, genero, rating, anio, temporadas):
        self._titulo = titulo
        self._genero = genero
        self._rating = rating
        self._anio = anio
        self._temporadas = temporadas

    @property
    def titulo(self):
        return self._titulo

    @property
    def genero(self):
        return self._genero

    @property
    def rating(self):
        return self._rating

    @property
    def año(self):
        return self._anio

    @property
    def temporadas(self):
        return self._temporadas

    def __repr__(self):
        return (
            f"{self._titulo} ({self._genero}) "
            f"⭐{self._rating} - {self._anio} - "
            f"{self._temporadas} temporadas"   )
