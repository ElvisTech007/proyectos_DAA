from arista import Arista
from nodo import Nodo

class Grafo:
    """Un grafo esta definido como una dupla que consta de un conjunto de nodos
    y un conjunto de aristas subconjunto potencia del conjunto de nodos"""
    def __init__(self, nombre_grafo, nodos, aristas):
        self.nombre_grafo = nombre_grafo
        self.nodos = nodos
        self.aristas = aristas

    def __str__(self):
        nodos_str = ", ".join(str(nodo) for nodo in self.nodos)
        aristas_str = ", ".join(str(arista) for arista in self.aristas)
        return f"{self.nombre_grafo}={{[{nodos_str}], [{aristas_str}]}}"

    def __repr__(self):
        return f"Grafo(Nodos=[{nodos_str}], Aristas=[{aristas_str}])"

    def to_graphviz(self, path="./"):
        """Metodo para parsear el grafo generado 
        y guardarlo en un archivo .viz"""
        pass