# 🎬 SeriesMatch

## Descripción

SeriesMatch es un sistema de consulta y recomendación de series desarrollado en Python utilizando Programación Orientada a Objetos.

El proyecto permite al usuario consultar un catálogo de series y realizar diferentes operaciones para facilitar la elección de qué mirar.

El sistema permite buscar series por título, listar todas las series disponibles y filtrar las series según su género.

## Integrantes

- Milena Iñiguez
- Mateo Rodriguez 
- Yasmin Arbona 

## Dominio

El dominio elegido para el proyecto es **series y entretenimiento audiovisual**.

Elegimos este dominio porque existe una gran cantidad de series disponibles y muchas veces puede resultar difícil decidir qué mirar.

## Problema que resuelve

SeriesMatch busca solucionar la dificultad que tienen las personas para encontrar una serie que se adapte a sus gustos.

El sistema organiza la información de las series y permite realizar búsquedas y filtros para encontrar más fácilmente una opción.

## Funcionalidades

El sistema cuenta con las siguientes funcionalidades:

1. Buscar una serie por título.
2. Listar todas las series disponibles.
3. Filtrar series por género.
4. Ver el Top N de series mejor valoradas.
5. Gestionar una lista de series favoritas.

## Clases principales

### Serie

Representa una serie del catálogo.

Sus principales atributos son:

- Título
- Género
- Rating
- Anio
- Cantidad de temporadas

### Usuario

Representa al usuario que utiliza el sistema y permite administrar sus series favoritas.

### Genero

Representa los diferentes géneros disponibles para clasificar las series.

### Catalogo

Se encarga de administrar las series y realizar operaciones como:

- Buscar
- Listar
- Filtrar
- Obtener el Top N

## Carga de datos

Los datos de prueba se encuentran almacenados en un archivo JSON:

```text
datos/series.json
