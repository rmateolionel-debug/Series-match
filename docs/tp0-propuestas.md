# Propuesta del Proyecto

## Nombre del proyecto

**SeriesMatch**

## Dominio elegido

**Series y entretenimiento audiovisual.**

Elegimos este dominio porque actualmente existe una gran cantidad de series disponibles en diferentes plataformas de streaming, lo que puede dificultar la elección de qué mirar.

## Problema que resuelve

SeriesMatch busca resolver el problema de no saber qué serie elegir entre tantas opciones disponibles.

El sistema permitirá al usuario buscar series, consultar el catálogo, filtrarlas por género y encontrar las series mejor valoradas, facilitando así la elección de qué mirar.

## Usuario objetivo

Una persona de 20 años que mira series principalmente por la noche, utiliza plataformas de streaming y suele tener dificultades para decidir qué serie comenzar después de terminar una que le gustó.

## 5 funcionalidades iniciales

1. **Buscar una serie por título.**
2. **Listar todas las series disponibles.**
3. **Filtrar series por género.**
4. **Ver series relacionadas según el género.**
5. **Ver el Top N de series mejor valoradas.**

## Ejemplo de interacción (boceto de consola)

```text
============================================================
                    🎬 SERIESMATCH 🎬
============================================================

1. Buscar una serie
2. Listar todas las series
3. Filtrar por género
4. Ver Top N
0. Salir

------------------------------------------------------------
Seleccione una opción: 3

Género a filtrar: Ciencia Ficción

============================================================
                  SERIES ENCONTRADAS
============================================================

1. Stranger Things
   Género: Ciencia Ficción
   Rating: ⭐ 8.7
   Año: 2016

2. Dark
   Género: Ciencia Ficción
   Rating: ⭐ 8.7
   Año: 2017

3. Black Mirror
   Género: Ciencia Ficción
   Rating: ⭐ 8.7
   Año: 2011

------------------------------------------------------------
Diagrama inicial de clases
+----------------------+
|        Serie         |
+----------------------+
| - _titulo            |
| - _genero            |
| - _rating            |
| - _anio              |
| - _temporadas        |
+----------------------+
| + titulo             |
| + genero             |
| + rating             |
| + anio               |
| + temporadas         |
+----------------------+

             |
             |
             v

+----------------------+
|       Genero         |
+----------------------+
| - _nombre            |
+----------------------+
| + nombre             |
+----------------------+


+----------------------+
|       Catalogo       |
+----------------------+
| - _series            |
+----------------------+
| + buscar()           |
| + listar()           |
| + filtrar()          |
| + top_n()            |
+----------------------+


+----------------------+
|       Usuario        |
+----------------------+
| - _nombre            |
| - _favoritos         |
+----------------------+
| + agregar_favorito() |
| + quitar_favorito()  |
| + listar_favoritos() |
+----------------------+

