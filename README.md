# proyectos_DAA
Repositorio del proyecto para diseño y análisis de algoritmos

Proyecto 1
# Biblioteca de Grafos en Python

Este repositorio contiene una biblioteca orientada a objetos en Python 3 para describir y utilizar grafos. Incluye clases para representar grafos, nodos y aristas, así como funciones para generar grafos utilizando varios modelos comunes.

## Clases

* **Grafo**: Representa un grafo con nodos y aristas.
* **Nodo**: Representa un nodo en el grafo.
* **Arista**: Representa una arista que conecta dos nodos.

## Modelos de Generación de Grafos

Se implementan los siguientes modelos de generación de grafos:

* **Grafo de Malla (Gm,n)**: Crea una malla de nodos con conexiones adyacentes.
    ```python
    grafoMalla(m, n, dirigido=False)
    ```
* **Erdös-Rényi (Gn,m)**: Genera un grafo aleatorio con un número fijo de aristas.
    ```python
    grafoErdosRenyi(n, m, dirigido=False)
    ```
* **Gilbert (Gn,p)**: Genera un grafo aleatorio con probabilidad de conexión entre nodos.
    ```python
    grafoGilbert(n, p, dirigido=False)
    ```
* **Geográfico Simple (Gn,r)**: Genera un grafo basado en la distancia entre nodos en un espacio geográfico.
    ```python
    grafoGeografico(n, r, dirigido=False)
    ```
* **Barabási-Albert (Gn,d)**: Genera un grafo con crecimiento preferencial.
    ```python
    grafoBarabasiAlbert(n, d, dirigido=False)
    ```
* **Dorogovtsev-Mendes (Gn)**: Genera un grafo con crecimiento triangular.
    ```python
    grafoDorogovtsevMendes(n, dirigido=False)
    ```

## Funcionalidades Adicionales

* **Guardar Grafo en Formato GraphViz**: La clase `Grafo` incluye un método para guardar el grafo en un archivo `.gv` compatible con GraphViz.

## Contenido del Repositorio

* **Código Fuente**: Implementación de la biblioteca de grafos en Python.
* **Archivos GraphViz (.gv)**: Archivos generados con los modelos de grafos para 50, 200 y 500 nodos (3 archivos por modelo).
* **Imágenes de Grafos**: Imágenes generadas a partir de los archivos GraphViz utilizando Gephi (18 imágenes en total).

## Instrucciones de Uso

1.  Clona el repositorio:
    ```bash
    git clone [https://github.com/ElvisTech007/proyectos_DAA.git](https://github.com/ElvisTech007/proyectos_DAA.git)
    ```
2.  Ejecuta los scripts de Python para generar grafos y archivos GraphViz.
3.  Utiliza Gephi para visualizar y generar imágenes de los grafos a partir de los archivos `.gv`.

## Dependencias

Pendiente para el requirements



## Licencia

GPL-3.0 license

## Contacto

Emiliano Aguilar
elvis_teck007@protonmail.com