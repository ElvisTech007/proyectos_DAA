# proyectos_DAA
[![Status](https://img.shields.io/badge/status-In%20Development-yellow.svg)]()
[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Repositorio del proyecto para diseño y análisis de algoritmos

Proyecto 1
# Biblioteca de Grafos en Python

Este repositorio contiene una biblioteca orientada a objetos en Python 3 para describir y utilizar grafos. Incluye clases para representar grafos, nodos y aristas, así como funciones para generar grafos utilizando varios modelos comunes.

## Clases

* **Grafo**: Representa un grafo con nodos y aristas.
    * Permite crear grafos dirigidos o no dirigidos.
    * Incluye métodos para añadir y obtener nodos y aristas.
    * Implementa modelos de generación de grafos aleatorios.
    * Permite guardar grafos en formato Graphviz.
* **Nodo**: Representa un nodo en el grafo.
    * Cada nodo tiene una etiqueta única y un diccionario de atributos.
    * Incluye métodos para obtener el grado del nodo.
* **Arista**: Representa una arista que conecta dos nodos.

## Modelos de Generación de Grafos

Se implementan los siguientes modelos de generación de grafos:

* **Grafo de Malla (Gm,n)**: Crea una malla de nodos con conexiones adyacentes.
    ```python
    grafo_malla(m, n, dirigido=False)
    ```
* **Erdös-Rényi (Gn,m)**: Genera un grafo aleatorio con un número fijo de aristas.
    ```python
    grafo_erdos_renyi(n, m, dirigido=False)
    ```
* **Gilbert (Gn,p)**: Genera un grafo aleatorio con probabilidad de conexión entre nodos.
    ```python
    grafo_gilbert(n, p, dirigido=False)
    ```
* **Geográfico Simple (Gn,r)**: Genera un grafo basado en la distancia entre nodos en un espacio geográfico.
    ```python
    grafo_geografico(n, r, dirigido=False)
    ```
* **Barabási-Albert (Gn,d)**: Genera un grafo con crecimiento preferencial.
    ```python
    grafo_barabasi_albert(n, d, dirigido=False)
    ```
* **Dorogovtsev-Mendes (Gn)**: Genera un grafo con crecimiento triangular.
    ```python
    grafo_dorogovtsev_mendes(n, dirigido=False)
    ```

## Funcionalidades Adicionales

* **Guardar Grafos en Graphviz**: Permite guardar grafos en formato Graphviz para visualización.
    ```python
    guardar_graphviz(nombre_archivo="graph.dot", directorio="proyecto_1/archivos_graphviz")
    ```
* **Obtener Nodos**: Permite obtener un nodo del grafo por su etiqueta.
    ```python
    obtener_nodo(etiqueta)
    ```
* **Añadir Aristas**: Añade una arista al grafo y actualiza los vecinos de los nodos.
    ```python
    aniadir_arista(arista)
    ```
* **Obtener Grado de un Nodo**: Calcula y devuelve el número de vecinos que tiene el nodo.
    ```python
    obtener_grado()
    ```
* **Verificar Grafo Vacío**: Verifica si el grafo está vacío (no tiene nodos ni aristas).
    ```python
    es_vacio()
    ```
* **Verificar Emparejamiento Válido**: Verifica si una arista propuesta cumple las condiciones de emparejamiento.
    ```python
    emparejamiento_valido(arista, dirigido)
    ```

## Uso

Para utilizar esta biblioteca, importa las clases y funciones necesarias desde los archivos correspondientes:

```python
    from grafo import Grafo, Nodo, Arista

    # Crear un grafo
    grafo = Grafo()

    # Crear nodos
    nodo1 = Nodo(1, atributos={"vecinos": []})
    nodo2 = Nodo(2, atributos={"vecinos": []})

    # Añadir nodos al grafo
    grafo.aniadir_nodo(nodo1)
    grafo.aniadir_nodo(nodo2)

    # Crear una arista
    arista = Arista(nodo1, nodo2)

    # Añadir la arista al grafo
    grafo.aniadir_arista(arista)

    # Generar un grafo aleatorio
    grafo.grafo_erdos_renyi(10, 15)

    # Guardar el grafo en formato Graphviz
    grafo.guardar_graphviz("grafo_erdos_renyi.dot")
```

## Contenido del Repositorio

* **Código Fuente**: Implementación de la biblioteca de grafos en Python.
* **Archivos GraphViz (.gv)**: Archivos generados con los modelos de grafos para 50, 200 y 500 nodos (3 archivos por modelo).
* **Imágenes de Grafos**: Imágenes generadas a partir de los archivos GraphViz utilizando Gephi (18 imágenes en total).

## Instrucciones de Uso

1.  Clona el repositorio:
    ```bash
    git clone git@github.com:ElvisTech007/proyectos_DAA.git
    ```
2.  Ejecuta los scripts de Python para generar grafos y archivos GraphViz.
3.  Utiliza Gephi para visualizar y generar imágenes de los grafos a partir de los archivos `.gv`.

## Licencia

GPL-3.0 license

## Contacto

Emiliano Aguilar
elvis_teck007@protonmail.com