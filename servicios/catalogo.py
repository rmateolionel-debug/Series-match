"""Operaciones de consulta y análisis sobre el catálogo de Series-Match."""

import unicodedata

from estructuras.cola_prioridad import obtener_top_n


def obtener_estadisticas(series):
    """Calcula estadísticas descriptivas del catálogo sin modificarlo."""
    if not series:
        return {"total": 0, "por_genero": {}, "rating_promedio": 0.0,
                "mejor_valorada": None, "mas_antigua": None}

    por_genero = {}
    for serie in series:
        por_genero[serie.genero] = por_genero.get(serie.genero, 0) + 1

    return {
        "total": len(series),
        "por_genero": dict(sorted(por_genero.items(), key=lambda item: item[0].lower())),
        "rating_promedio": sum(s.rating for s in series) / len(series),
        "mejor_valorada": max(series, key=lambda s: s.rating),
        "mas_antigua": min(series, key=lambda s: s.anio),
    }


def recomendar_series(series, genero, cantidad=5, rating_minimo=0.0):
    """Filtra por género y rating mínimo, y ordena los resultados con Heap."""
    if cantidad < 1:
        raise ValueError("La cantidad debe ser mayor que cero.")
    if not 0 <= rating_minimo <= 10:
        raise ValueError("El rating mínimo debe estar entre 0 y 10.")

    def normalizar(texto):
        texto = unicodedata.normalize("NFD", texto.strip().casefold())
        return "".join(caracter for caracter in texto if unicodedata.category(caracter) != "Mn")
    seleccionadas = [s for s in series
                     if normalizar(s.genero) == normalizar(genero)
                     and s.rating >= rating_minimo]
    return obtener_top_n(seleccionadas, cantidad)
