from nodo import Nodo
import copy

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

    def __init__(self, nodo_1, nodo_2, peso=1, atributos={}):
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
        atributos : dict, opcional
            Atributos asociados a la arista
        """
        self.nodo_1 = nodo_1
        self.nodo_2 = nodo_2
        self.peso = peso
        self.atributos = atributos

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

    def __eq__(self, otra_arista):
        """
        Compara dos aristas para determinar si son iguales.

        Esta función verifica si los nodos de las dos aristas son los mismos

        Parámetros:
            otra_arista (Arista): La otra arista con la que se compara.

        Retorna:
            bool: True si las aristas son iguales, False de lo contrario.
        """
        # Para grafos no dirigidos, el orden de los nodos no importa
        # Para grafos dirigidos, el orden de los nodos importa.
        return (self.nodo_1 == otra_arista.nodo_1 and self.nodo_2 == otra_arista.nodo_2)

    def __hash__(self):
        """
        Calcula el valor hash de la arista.

        Esta función calcula un valor hash único para la arista, basado en los
        valores hash de sus nodos. Esto permite usar objetos Arista como claves
        en diccionarios y elementos en conjuntos.

        Retorna:
            int: El valor hash de la arista.
        """
        # Usamos una tupla inmutable de los nodos para calcular el hash.
        # El orden de los nodos es importante para grafos dirigidos.
        return hash((self.nodo_1, self.nodo_2))
    
    def __deepcopy__(self, memo):
        # vemos si ya estaba copiado
        if id(self) in memo:
            return memo[id(self)]
        # Hacmoes una copia de los atributos de una instancia arista
        # los cuales sean mutables, es decir los nodos
        # y le pasamos el diccionario de copias
        nodo_1_copia = copy.deepcopy(self.nodo_1, memo)
        nodo_2_copia = copy.deepcopy(self.nodo_2, memo)
        # El peso es inmutable por que es un entero on un float
        # Ahora los atributos
        copia_atributos = copy.deepcopy(self.atributos, memo)
        # Ahora creamos una nueva arista:
        nueva_arista = Arista(nodo_1_copia, nodo_2_copia, self.peso, copia_atributos)
        # Le pasamos al diccionario de copias el id
        memo[id(self)] = nueva_arista

        return nueva_arista