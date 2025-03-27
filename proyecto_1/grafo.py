import os
import random

from arista import Arista
from nodo import Nodo


class Grafo:
    """Un grafo esta definido como una dupla que consta de un conjunto de nodos
    y un conjunto de aristas subconjunto potencia del conjunto de nodos"""

    # Metodo especiales de la clase
    def __init__(self, nombre_grafo, lista_nodos, lista_aristas, dirigido):
        """
        Constructor de la clase Grafo.

        Parámetros
        ----------
        nombre_grafo : str
            El nombre del grafo.
        lista_nodos : list
            Lista de objetos Nodo que representan los nodos del grafo.
        lista_aristas : list
            Lista de objetos Arista que representan las aristas del grafo.
        dirigido : bool
            Indica si el grafo es dirigido (True) o no dirigido (False).
        """
        self.nombre_grafo = nombre_grafo
        self.lista_nodos = lista_nodos  # Debería ser una lista de nodos
        # Diccionario por si se le quiere añadir más cosas en un futuro
        self.lista_aristas = lista_aristas  # lista de aristas suponiendo que todo chido xd
        self.dirigido = dirigido  # booleano para ver si es dirigido

    def __str__(self):
        """
        Método str para mostrar el grafo.

        Devuelve
        -------
        str
            Representación en cadena del grafo, incluyendo el nombre, los nodos y las aristas.
        """
        nodos_str = ", ".join(str(nodo) for nodo in self.lista_nodos)
        aristas_str = ", ".join(str(arista) for arista in self.lista_aristas)
        return f"{self.nombre_grafo}={{[{nodos_str}], [{aristas_str}]}}"

    def __repr__(self):
        """
        Método str para mostrar el grafo.

        Devuelve
        -------
        str
            Representación en cadena del grafo, incluyendo el nombre, los nodos y las aristas.
        """
        return f"Grafo(Nodos=[{nodos_str}], Aristas=[{aristas_str}])"

    # Metodos EXTRA del Grafo para poder manipular su información:

    def aniadir_nodo(self, nodo):   
        """
        Añade un nodo al grafo.

        Parámetros
        ----------
        nodo : Nodo
            Objeto Nodo que se va a añadir al grafo.
        """  
        self.lista_nodos.append(nodo)

    def aniadir_arista(self, arista):
        """
        Añade una arista al grafo.

        Parámetros
        ----------
        arista : Arista
            Objeto Arista que se va a añadir al grafo.
        """
        self.lista_aristas.append(arista)

    def obtener_grado(self, nodo):
        """Método para obtener el grado de un nodo"""
        # Aquí debe de hacer algo para que haga eso jaja salu2
        pass
    
    def es_vacio(self):
        """
        Verifica si el grafo está vacío.

        Returns
        -------
        bool
            True si el grafo está vacío (no tiene nodos ni aristas), False en caso contrario.
        """
        # Esto para ver que se le pase un grafo vacio
        return not self.lista_nodos and not self.lista_aristas

    def emparejamiento_valido(self, arista, dirigido):
        """
        Verifica si una arista propuesta cumple las condiciones de emparejamiento.

        Atributos
        ----------
        arista : Arista
            Objeto Arista que representa la arista a verificar.
        dirigido : bool
            Indica si el grafo es dirigido (True) o no dirigido (False).

        Returns
        -------
        bool
            True si la arista cumple las condiciones de emparejamiento, False en caso contrario.

        Notas
        -----
        En grafos no dirigidos, verifica que la arista inversa (nodo_2, nodo_1)
        no exista, ya que representa la misma conexión que (nodo_1, nodo_2).
        """
        if arista.nodo_1 == arista.nodo_2:
            return False
        if arista in self.lista_aristas:
            return False
        # Si no es dirigido deberíamos verificar si 
        # la pareja nodo_2 -> nodo_1 está
        # por que al no ser dirigido, esta pareja es
        # la misma que nodo_1, nodo_2
        if not dirigido:
            if Arista(arista.nodo_2, arista.nodo_1) in self.lista_aristas:
                return False
        return True

    # ALGORITMOS DE GENERACIÓN DE GRAFOS ALEATORIOS

    def grafo_malla(self, m, n, dirigido=False):
        """Genera grafo de malla"""
        pass

    def grafo_erdos_renyi(self, n, m, dirigido=False):
        """
        Genera un grafo aleatorio utilizando el modelo Erdős-Rényi.

        Parámetros
        ----------
        n : int
            Número de nodos en el grafo (debe ser mayor que 0).
        m : int
            Número de aristas en el grafo (debe ser mayor o igual a n-1).
        dirigido : bool, opcional
            Indica si el grafo es dirigido (True) o no dirigido (False). El valor predeterminado es False.

        Returns
        -------
        None
            Este método modifica el grafo actual (self) añadiendo nodos y aristas.

        Raises
        ------
        ValueError
            Si el número de nodos (n) es menor o igual a 0.
            Si el número de aristas (m) es menor que n-1.
        """
        if n <= 0:
            # Por si ponen más nodos
            raise ValueError("El número de nodos (n) debe ser mayor que 0.")
        if m < n - 1:
            # Por si ponen más aristas
            raise ValueError("El número de aristas (m) debe ser mayor o igual a n-1.")
        # Primero comenzamos con un grafo vacio de aristas
        # Solo puros nodos del 1 a n

        # Si el nodo no es vacio lo vaciamos xD
        if not self.es_vacio():
            self.lista_nodos = []
            self.lista_aristas = []
        
        # Ahora si generamos nuestra lista de n nodos
        # del 1 al n
        [self.aniadir_nodo(i+1) for i in range(n)]
        # Mientras no hayamos completado las conexiones
        while len(self.lista_aristas) < m:
            
            # Ahora vamos a hacer random choice para elegir
            nodo_1, nodo_2 = random.choice(self.lista_nodos), random.choice(self.lista_nodos)
            arista_propuesta = Arista(nodo_1,nodo_2)
            if not self.emparejamiento_valido(arista_propuesta, self.dirigido):
                #print(arista_propuesta, self.emparejamiento_valido(arista_propuesta))
                continue
            else:
                self.aniadir_arista(arista_propuesta)


    def grafo_gilbert(self, n, p, dirigido=False):
        """Genera grafo aleatorio con el modelo Gilbert."""
        pass

    def grafo_geografico(self, n, r, dirigido=False):
        """Genera grafo aleatorio con el modelo geográfico simple."""
        pass

    def grafo_barabasi_albert(self, n, d, dirigido=False):
        """Genera grafo aleatorio con el modelo Barabasi-Albert."""
        pass

    def grafo_dorogovtsev_mendes(self, n, dirigido=False):
        """Genera grafo aleatorio con el modelo Dorogovtsev-Mendes."""
        pass

    
    def guardar_graphviz(self,  nombre_archivo="graph.dot",directorio="proyecto_1/archivos_graphviz"):
        """
        Guarda el grafo en un archivo con formato Graphviz.

        Parameters
        ----------
        nombre_archivo : str, opcional
            Nombre del archivo en el que se guardará el grafo. El valor predeterminado es "graph.dot".
        directorio : str, opcional
            Directorio donde se guardará el archivo del grafo. El valor predeterminado es "proyecto_1/archivos_graphviz".

        Returns
        -------
        None
            Este método guarda el grafo en un archivo y no devuelve ningún valor.

        Notas
        -----
        El grafo se guarda en formato Graphviz, que puede ser visualizado con herramientas como Graphviz.
        """
        # Primero creamos un archivo con terminación
        # dot para escribirlo en un directorio y le asignamos el nombre
        # que tiene el archivo
        ruta_completa = os.path.join(directorio, nombre_archivo)
        
        with open(ruta_completa, "w") as archivo_dot:
            if not self.dirigido:
                apuntador = " -- "
                archivo_dot.write(f"graph {self.nombre_grafo} {{\n")
            else:
                apuntador = " -> "
                archivo_dot.write(f"digraph {self.nombre_grafo} {{\n")
            for nodo in self.lista_nodos:
                archivo_dot.write(f"    {nodo};\n")
            for arista in self.lista_aristas:
                archivo_dot.write(f"    {arista.nodo_1}{apuntador}{arista.nodo_2};\n")
            archivo_dot.write("}")
        print(f"Grafo guardado en: {ruta_completa}")
        