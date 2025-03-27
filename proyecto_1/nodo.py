class Nodo:
    """
    Representa una arista en un grafo.

    Una arista conecta dos nodos y puede tener un peso asociado.

    Attributes
    ----------
    etiqueta : int
        etiqueta del nodo
    """

    def __init__(self, etiqueta):
        """
        Constructor de la clase Nodo.

        Parámetros
        ----------
        etiqueta : str
            Etiqueta única del nodo.
        """
        self.etiqueta = etiqueta

    def __str__(self):
        """
        Devuelve una representación en cadena del nodo.

        Devuelve
        -------
        str
            Representación en cadena del nodo, que es su etiqueta.
        """
        return f"{self.etiqueta}"

    def __repr__(self):
        """
        Devuelve una representación en cadena del nodo para depuración.

        Devuelve
        -------
        str
            Representación en cadena del nodo, que es su etiqueta.
        """
        return f"{self.etiqueta}"