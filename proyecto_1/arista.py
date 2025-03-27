from nodo import Nodo


class Arista:
    """
    Representa una arista en un grafo.

    Una arista conecta dos nodos y puede tener un peso asociado.

    Attributes
    ----------
    nodo_1 : Nodo
        Nodo de origen de la arista.
    nodo_2 : Nodo
        Nodo de destino de la arista.
    peso : int, opcional
        Peso asociado a la arista. El valor predeterminado es 1.
    """

    def __init__(self, nodo_1, nodo_2, peso=1):
        """
        Constructor de la clase Arista.

        Parameters
        ----------
        nodo_1 : Nodo
            Nodo de origen de la arista.
        nodo_2 : Nodo
            Nodo de destino de la arista.
        peso : int, opcional
            Peso asociado a la arista. El valor predeterminado es 1.
        """
        self.nodo_1 = nodo_1
        self.nodo_2 = nodo_2
        self.peso = peso

    def __str__(self):
        """
        Devuelve una representación en cadena de la arista.

        Returns
        -------
        str
            Representación en cadena de la arista en el formato "(nodo_1, nodo_2)".
        """
        return f"({self.nodo_1}, {self.nodo_2})"

    def __repr__(self):
        """
        Devuelve una representación en cadena de la arista para depuración.

        Returns
        -------
        str
            Representación en cadena de la arista en el formato "(nodo_1, nodo_2)".
        """
        return f"({self.nodo_1}, {self.nodo_2})"