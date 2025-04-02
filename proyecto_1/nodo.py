class Nodo:
    """
    Representa una arista en un grafo.

    Una arista conecta dos nodos y puede tener un peso asociado.

    Attributes
    ----------
    etiqueta : int
        etiqueta del nodo
    """

    def __init__(self, etiqueta, atributos={}):
        """
        Constructor de la clase Nodo.

        Parámetros
        ----------
        etiqueta : str
            Etiqueta única del nodo.
        atributos : dict, opcional
            Atributos del nodo
        """
        self.etiqueta = etiqueta
        self.atributos = atributos if atributos is not None else {}

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

    def __eq__(self, otro_nodo):
        """
        Compara dos nodos por su etiqueta.

        Parámetros
        ----------
        otro_nodo : Nodo
            El otro nodo con el que se va a comparar.

        Devuelve
        -------
        bool
            True si los nodos tienen la misma etiqueta, False en caso contrario.
        """
        if isinstance(otro_nodo, Nodo):
            return self.etiqueta == otro_nodo.etiqueta
        return False

    def __hash__(self):
        """
        Calcula el valor hash del nodo.

        El valor hash se basa en la etiqueta del nodo, lo que permite que los nodos
        se utilicen como claves en diccionarios y conjuntos.

        Devuelve
        -------
        int
            El valor hash del nodo.
        """
        return hash(self.etiqueta)  # Usamos la etiqueta como valor hash

    def obtener_grado(self):
        
        """Obtiene el grado de un nodo.

        Calcula y devuelve el número de vecinos que tiene el nodo.

        Returns
        -------
        int
            El grado del nodo (número de vecinos).

        Raises
        ------
        ValueError
            Si el nodo no tiene el atributo 'atributos' o si no tiene la clave 'vecinos' en su diccionario de atributos.

        Notes
        -----
        El grado de un nodo se define como el número de aristas que lo conectan a otros nodos.
        Esta función asume que los nodos tienen un atributo 'atributos' que contiene un diccionario.
        Este diccionario debe tener una clave 'vecinos' que es una lista de nodos vecinos.
        """
        # Aquí debe de hacer algo para que haga eso jaja salu2
        if not hasattr(self, "atributos"):
            raise ValueError(f"El nodo no tiene diccionario de atributos")
        else:
            if "vecinos" in self.atributos:
                return len(self.atributos["vecinos"])
            raise ValueError("El nodo no posee el atributo 'vecinos'")