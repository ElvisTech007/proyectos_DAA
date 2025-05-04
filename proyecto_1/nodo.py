import copy

class Nodo:
    """
    Representa una arista en un grafo.

    Una arista conecta dos nodos y puede tener un peso asociado.

    Attributes
    ----------
    etiqueta : int
        etiqueta del nodo
    """

    def __init__(self, etiqueta, atributos=None):
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

        if atributos is None:
            self.atributos =  {}
        else:
            self.atributos = atributos.copy()
        
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

    # Metodo para copiar 
    def __deepcopy__(self,memo):
        """
        Crea y devuelve una copia profunda de la instancia del Nodo.

        Parámetros
        ----------
        memo : dict
            Diccionario utilizado por copy.deepcopy() para recordar los objetos ya copiados.

        Devuelve
        -------
        Nodo
            Una nueva instancia de Nodo que es una copia profunda de la original.
        """
        # Verificar si ya se ha copiado este objeto Nodo
        if id(self) in memo:
            return memo[id(self)]
        # Creamos un nuevo nodo
        nuevo_nodo = Nodo(self.etiqueta)
        # copiamos los atributos
        nuevo_nodo.atributos = copy.deepcopy(self.atributos, memo)
        memo[id(self)] = nuevo_nodo
        return nuevo_nodo

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