import os
import random

from collections import OrderedDict
from math import sqrt
from itertools import combinations
from random import choices, uniform
from arista import Arista
from nodo import Nodo


class Grafo:
    """Un grafo esta definido como una dupla que consta de un conjunto de nodos
    y un conjunto de aristas subconjunto potencia del conjunto de nodos"""

    # Metodo especiales de la clase
    def __init__(self, nombre_grafo="G", conjunto_nodos=OrderedDict(), conjunto_aristas=OrderedDict(), dirigido=False):
        """
        Constructor de la clase Grafo.

        Parámetros
        ----------
        nombre_grafo : str, opcional
            El nombre del grafo.
        conjunto_nodos : OrderedDict, opcional
            Lista de objetos Nodo que representan los nodos del grafo.
        conjunto_aristas : OrderedDict
            Lista de objetos Arista que representan las aristas del grafo.
        dirigido : bool
            Indica si el grafo es dirigido (True) o no dirigido (False).
        """
        self.nombre_grafo = nombre_grafo
        self.conjunto_nodos = conjunto_nodos  # Debería ser una lista de nodos
        # Diccionario por si se le quiere añadir más cosas en un futuro
        self.conjunto_aristas = conjunto_aristas  # lista de aristas suponiendo que todo chido xd
        self.dirigido = dirigido  # booleano para ver si es dirigido

    def __str__(self):
        """
        Método str para mostrar el grafo.

        Devuelve
        -------
        str
            Representación en cadena del grafo, incluyendo el nombre, los nodos y las aristas.
        """
        nodos_str = ", ".join(str(nodo) for nodo in self.conjunto_nodos.values())
        # Modificación para iterar sobre las listas de aristas
        aristas_str = ", ".join(str(arista) for arista in self.conjunto_aristas.values())
        return f"{self.nombre_grafo}={{[{nodos_str}], [{aristas_str}]}}"

    def __repr__(self):
        """
        Método repr para mostrar el grafo.

        Devuelve
        -------
        str
            Representación en cadena del grafo, incluyendo el nombre, los nodos y las aristas.
        """
        nodos_str = ", ".join(str(nodo) for nodo in self.conjunto_nodos.values())
        # Modificación para iterar sobre las listas de aristas
        aristas_str = ", ".join(str(arista) for arista_list in self.conjunto_aristas.values() for arista in arista_list)
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
        # Añadimos el nodo al diccionario de nodos
        # con Etiqueta que apunta al objeto Nodo
        self.conjunto_nodos[nodo.etiqueta] = nodo

    def aniadir_arista(self, arista):
        """
        Añade una arista al grafo.

        Parámetros
        ----------
        arista : Arista
            Objeto Arista que se va a añadir al grafo.

        """
        nodo_1 = arista.nodo_1
        nodo_2 = arista.nodo_2

        # Asegurarse de que los nodos existen en el grafo
        if nodo_1.etiqueta not in self.conjunto_nodos.keys() or nodo_2.etiqueta not in self.conjunto_nodos.keys():
            # Por si no existen
            raise ValueError("Uno o ambos nodos de la arista no existen en el grafo.")

        self.conjunto_aristas[(nodo_1, nodo_2)] = arista

    def obtener_nodo(self,etiqueta):
        """Metodo para acceder a un nodo mediante su etiqueta"""
        # Primero vamos a usar un diccionario para que sea mas facil 
        if etiqueta in self.conjunto_nodos.keys():
            return self.conjunto_nodos[etiqueta]
        else:
            raise ValueError(f"El nodo {etiqueta} no existe") # O lanza una excepción personalizada

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
        return not self.conjunto_aristas and not self.conjunto_nodos

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
        if arista in self.conjunto_aristas.values():
            return False
        # Si no es dirigido deberíamos verificar si 
        # la pareja nodo_2 -> nodo_1 está
        # por que al no ser dirigido, esta pareja es
        # la misma que nodo_1, nodo_2
        if not dirigido:
            if Arista(arista.nodo_2, arista.nodo_1) in self.conjunto_aristas.values():
                return False
        return True

    # ALGORITMOS DE GENERACIÓN DE GRAFOS ALEATORIOS

    def grafo_malla(self, m, n, dirigido=False):
        """
        Genera un grafo de malla.

        Construye un grafo de malla con 'm' columnas y 'n' filas.

        Parameters
        ----------
        m : int
            Número de columnas en la malla.
        n : int
            Número de filas en la malla.
        dirigido : bool, opcional
            Indica si el grafo es dirigido (True) o no dirigido (False). El valor predeterminado es False.

        Returns
        -------
        None
            Este método modifica el grafo actual (self) añadiendo nodos y aristas para formar la malla.

        Notes
        -----
        El grafo generado tendrá 'm * n' nodos y aristas que conectan los nodos adyacentes en la malla.
        """
        # Primero vamos  añadir todos esos m*n nodos:
        # Si el grafo no es vacio lo vaciamos xD
        if not self.es_vacio():
            self.conjunto_aristas = OrderedDict()
            self.conjunto_nodos = OrderedDict()
        [self.aniadir_nodo(Nodo(i+1)) for i in range((n*m))]
        # AHora debemos agregar las aristas tal que se forme una malla:
        for i in range(1,(m*n)+1):
                # Primero proponemos la arista de la derecha
                # Como avanzamos uno siempre existe
                # pero determinamos la conexion sabiendo si esta a la orilla
                # es decir, su mod m es igual a 0

                # SI no es igual no esta en la orilla
                esta_en_orilla = (i)%m == 0
                esta_en_ultima_fila = i > m*(n-1)
                if not esta_en_orilla:
                    arista_propuesta = Arista(self.obtener_nodo(i), self.obtener_nodo(i+1))
                    self.aniadir_arista(arista_propuesta)
                
                # Ahora para la arista que apunta hacia abajo tenemos que 
                # mientras m*(n-1) que indica justamente la penultima fila
                # que es la ultima que tiene conexiones hacia abajo
                if not esta_en_ultima_fila:
                    arista_propuesta = Arista(self.obtener_nodo(i), self.obtener_nodo(i+m))
                    self.aniadir_arista(arista_propuesta)
                # Nada mas por diversión le voy a agregar las diagonales a mi codigo
                # que serían todos aquellas todas menos las que son multiplos de m
                # o que sean de la penultima fila
                if (not esta_en_orilla ) and (not esta_en_ultima_fila):
                    arista_propuesta = Arista(self.obtener_nodo(i), self.obtener_nodo(i+(m+1)))
                    self.aniadir_arista(arista_propuesta)

        # Eso debería ser todo

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
            self.lista_nodos = OrderedDict()
            self.lista_aristas = OrderedDict()
        
        # Ahora si generamos nuestra lista de n nodos
        # del 1 al n
        [self.aniadir_nodo(Nodo(i+1)) for i in range(n)]
        lista_nodos = list(self.conjunto_nodos.values())
        # Mientras no hayamos completado las conexiones
        while len(self.conjunto_aristas) < m:
            
            # Ahora vamos a hacer random choice para elegir
            nodo_1, nodo_2 = random.choice(lista_nodos), random.choice(lista_nodos)
            arista_propuesta = Arista(nodo_1,nodo_2)
            if not self.emparejamiento_valido(arista_propuesta, self.dirigido):
                #print(arista_propuesta, self.emparejamiento_valido(arista_propuesta))
                continue
            else:
                self.aniadir_arista(arista_propuesta)


    def grafo_gilbert(self, n, p, dirigido=False):
        """Genera grafo aleatorio con el modelo Gilbert."""
        # Primero generamos todos los nodos
        # Primero vamos  añadir todos esos m*n nodos:
        # Si el grafo no es vacio lo vaciamos xD
        if not self.es_vacio():
            self.conjunto_aristas = OrderedDict()
            self.conjunto_nodos = OrderedDict()
        [self.aniadir_nodo(Nodo(i+1)) for i in range(n)]
        # Despues de eso para cada pareja de nodos
        parejas_nodos = combinations(list(self.conjunto_nodos.values()), 2)
        # Intentamos crear una arista con una probabilidad p
        # Para cada nodo de la lista y así lo vamos a hacer sucesivamente
        for nodo_1, nodo_2 in parejas_nodos:
            # Resultado del volado, la función regresa la lista [False]
            gano_volado = random.choices([True, False], [p, 1-p])[0]
            # print(gano_volado)
            arista_propuesta = Arista(nodo_1,nodo_2)
            if gano_volado and self.emparejamiento_valido(arista_propuesta, self.dirigido):
                self.aniadir_arista(arista_propuesta)

    def grafo_geografico(self, n, r, dirigido=False):
        """Genera grafo aleatorio con el modelo geográfico simple."""
        # Primero generamos todos los nodos
        # Primero vamos  añadir todos esos m*n nodos:
        # Si el grafo no es vacio lo vaciamos xD
        def distancia_euclideana(punto_1, punto_2):
            """función auxiliar para calcular la distancia euclidiana"""
            return sqrt((punto_1[0] - punto_2[0])**2 +  (punto_1[1] - punto_2[1])**2)

        if not self.es_vacio():
            self.conjunto_aristas = OrderedDict()
            self.conjunto_nodos = OrderedDict()

        # Ahora cuando los creamos debemos añadirles una posición 
        # que se genere uniformemente entre 0 y 1 para x,y
        for i in range(n):
            # Posicion aleatoria con x,y entre 0 y 1
            x,y = random.uniform(0,1), random.uniform(0,1)
            nodo = Nodo(i+1, {"posicion": (x,y)})
            self.aniadir_nodo(nodo)
        # Ya que creamos los nodos entonces tenemos que
        # Medir la distancia de ese nodo a todos los demás nodos
        parejas_nodos = combinations(list(self.conjunto_nodos.values()), 2)
        # y solo conectar aquellos que están a distancia a lo más r
        for nodo_1, nodo_2 in parejas_nodos:
            pos_nodo_1 = nodo_1.atributos["posicion"]
            pos_nodo_2 = nodo_2.atributos["posicion"]
            distancia_entre_nodos = distancia_euclideana(pos_nodo_1, pos_nodo_2)
            if distancia_entre_nodos <= r:
                arista_propuesta = Arista(nodo_1, nodo_2)
                self.aniadir_arista(arista_propuesta)


    def grafo_barabasi_albert(self, n, d, dirigido=False):
        """Genera grafo aleatorio con el modelo Barabasi-Albert.
        Variante del modelo Gn,d Barabási-Albert. 
        Colocar n nodos uno por uno, asignando a cada uno d aristas a vértices
        distintos de tal manera que la probabilidad de que el vértice nuevo se conecte a un vértice existente 
        v es proporcional a la cantidad de aristas que v tiene actualmente"""
        # Conforme vamos generando los nodos vamos a tratar de conectar 
        # los nodos anteriores con una función de probabilidad
        # que se calcula como deg(r)/d 
        # para esto deberíamos de mantener el registro de todos los nodos
        # que estan conectados unos a los otros
        # para esto usare al diccionario atributos con el atributo vecinos
        # que será una lista

        # También es importante recordar que 
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

            for nodo in self.conjunto_nodos.keys():
                archivo_dot.write(f"    {nodo};\n")
            for arista in self.conjunto_aristas.values():
                archivo_dot.write(f"    {arista.nodo_1}{apuntador}{arista.nodo_2};\n")
            archivo_dot.write("}")
        print(f"Grafo guardado en: {ruta_completa}")
        