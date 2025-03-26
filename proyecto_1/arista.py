from nodo import Nodo


class Arista:
    def __init__(self, nodo_1, nodo_2, peso=1):
        # Va del nodo 1 al nodo 2 en caso de ser dirigido
        # Si no, solamente la interpretación cambia
        self.nodo_1 = nodo_1
        self.nodo_2 = nodo_2
        self.peso = peso

    def __str__(self):
        return f"({self.nodo_1}, {self.nodo_2})"

    def __repr__(self):
        return f"({self.nodo_1}, {self.nodo_2})"
