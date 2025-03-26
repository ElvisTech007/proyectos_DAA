from nodo import Nodo

class Arista:
    def __init__ (self, nodo_1, nodo_2):
        self.nodo_1 = nodo_1
        self.nodo_2 = nodo_2
    
    def __str__(self):
        return f"({self.nodo_1}, {self.nodo_2})"

    def __repr__(self):
        return f"({self.nodo_1}, {self.nodo_2})"

