import os
import random


from copy import deepcopy
from collections import OrderedDict, deque
# Lista de prioridades actualizable
from heapdict import heapdict
from math import sqrt, inf
from itertools import combinations
from random import choices, uniform, choice
from arista import Arista
from nodo import Nodo


class Grafo:
    """Un grafo esta definido como una dupla que consta de un conjunto de nodos
    y un conjunto de aristas subconjunto potencia del conjunto de nodos
    

    Parameters
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

    # Metodo especiales de la clase
    def __init__(self, nombre_grafo="G",
        conjunto_nodos=None,
        conjunto_aristas=None,
        dirigido=False
    ):
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
        # Se crea uno nuevo cuando no se le pasa uno
        self.conjunto_nodos = OrderedDict() if conjunto_nodos is None else conjunto_nodos.copy()
        # Diccionario por si se le quiere añadir más cosas en un futuro
        # misma forma que lo anterior
        self.conjunto_aristas = OrderedDict() if conjunto_aristas is None else conjunto_aristas.copy() 
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

    def __deepcopy__(self, memo):
        """
        Crea una copia profunda del grafo.

        Copia recursivamente nodos y aristas, gestionando referencias para evitar bucles.

        Parameters
        ----------
        memo : dict
            Diccionario de objetos ya copiados en la operación actual para evitar recursión infinita.

        Returns
        -------
        nuevo_grafo : Grafo
            Una nueva instancia de Grafo que es una copia profunda del original.
        """
        # Si el objeto actual ya ha sido copiado en esta operación deepcopy,
        # devolver la copia existente para evitar bucles infinitos.
        if id(self) in memo:
            return memo[id(self)]

        nuevo_grafo = Grafo(nombre_grafo=self.nombre_grafo, dirigido=self.dirigido)
        
        memo[id(self)] = nuevo_grafo

        nuevo_grafo.conjunto_nodos = copy.deepcopy(self.conjunto_nodos, memo)
        nuevo_grafo.conjunto_aristas = copy.deepcopy(self.conjunto_aristas, memo)


        return nuevo_grafo

    # Metodo PRIVADOS  para manejar cositas:
    def _echar_volado(self, p=0.5):
        """
        Simula un volado con una probabilidad dada.

        Args:
            probabilidad: La probabilidad de obtener True.

        Returns:
            True o False.
        """
        return random.choices([True, False], [p, 1-p])[0]
    def _iniciar_grafo_con_aristas(self, set_aristas):
        """
        Inicializa un nuevo grafo con un conjunto específico de aristas.

        Construye un nuevo grafo que incluye todos los nodos del grafo original
        y las aristas proporcionadas, creando nuevas instancias de nodos y aristas.

        Parameters
        ----------
        set_aristas : set
            Un conjunto de objetos Arista a añadir al nuevo grafo.

        Returns
        -------
        subgrafo : Grafo
            Un nuevo objeto Grafo que contiene los nodos del grafo original
            y las aristas especificadas, sin copiar referencias directas.

        Notes
        -----
        Este es un método auxiliar privado.
        """
        # Dado un conjunto de aristas 
        # Estoy construyendo un árbol desde 0
        # para no estar copiando referencias
        subgrafo = Grafo()
        num_nodos = len(self.conjunto_nodos.keys())
        for i in range(1,num_nodos+1):
            subgrafo.aniadir_nodo(Nodo(i, atributos={"vecinos":[]}))

        for arista in set_aristas:
            nodo_1 = subgrafo.obtener_nodo(arista.nodo_1.etiqueta)
            nodo_2 = subgrafo.obtener_nodo(arista.nodo_2.etiqueta)
            subgrafo.aniadir_arista(Arista(nodo_1, nodo_2))
        return subgrafo



    def inicializar_pesos_aleatorios(self, rango_inferior=1, rango_superior=100):
        """
        Inicializa los pesos de las aristas y las distancias de los nodos con valores aleatorios.

        Asigna un peso aleatorio a cada arista dentro del rango especificado
        y establece la distancia de todos los nodos a None.

        Parameters
        ----------
        rango_inferior : int, optional
            El valor mínimo posible para el peso de una arista. Por defecto es 1.
        rango_superior : int, optional
            El valor máximo posible para el peso de una arista. Por defecto es 100.

        Returns
        -------
        None
            Esta función no retorna ningún valor; modifica el grafo inplace.
        """
        # También las distnacias de los nodos:
        for nodo in self.conjunto_nodos.values():
            nodo.atributos["distancia"] = None
        # Añadimos los pesos en las aristas:
        for arista in self.conjunto_aristas.values():
            arista.atributos["peso"] = random.randint(rango_inferior,rango_superior)

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
        """Añade una arista al grafo y actualiza los vecinos de los nodos.

        Añade una arista al grafo, conectando dos nodos y actualizando sus listas de vecinos.

        Parameters
        ----------
        arista : Arista
            Objeto Arista que se va a añadir al grafo.

        Raises
        ------
        ValueError
            Si uno o ambos nodos de la arista no existen en el grafo.
            Si uno o ambos nodos no tienen el atributo 'vecinos' en su diccionario de atributos.

        Returns
        -------
        None
            La función modifica el grafo en su lugar (self)."""


        nodo_1 = arista.nodo_1
        nodo_2 = arista.nodo_2

        # Asegurarse de que los nodos existen en el grafo
        if nodo_1.etiqueta not in self.conjunto_nodos.keys() or nodo_2.etiqueta not in self.conjunto_nodos.keys():
            # Por si no existen
            raise ValueError("Uno o ambos nodos de la arista no existen en el grafo.")
        # Comprobamos si tiene el atributo
        if hasattr(nodo_1, "atributos") and hasattr(nodo_2, "atributos"):
            # Si no están, entonces inicializamos el atributo de vecinos
            if "vecinos" not in nodo_1.atributos:
                nodo_1.atributos["vecinos"] = []
            if "vecinos" not in nodo_2.atributos:
                nodo_2.atributos["vecinos"] = []
            # Y cuando ya es seguro que lo tengan agregamos 
            # los vecinos los unos al los otros

            # COndición para que no se agreguen dobles los vecinos
            if nodo_2 not in nodo_1.atributos["vecinos"]:
                nodo_1.atributos["vecinos"].append(nodo_2)
            if nodo_1 not in nodo_2.atributos["vecinos"]:
                nodo_2.atributos["vecinos"].append(nodo_1)
        else:
            raise ValueError("Uno o ambos nodos no tienen atributo de vecinos")
        self.conjunto_aristas[(nodo_1, nodo_2)] = arista

    def obtener_nodo(self,etiqueta):
        """Obtiene un nodo del grafo por su etiqueta.

        Busca un nodo en el grafo utilizando su etiqueta única.

        Parameters
        ----------
        etiqueta : int o str
            Etiqueta del nodo que se desea obtener.

        Returns
        ----------
        Nodo
            El objeto Nodo correspondiente a la etiqueta dada.

        Raises
        ----------
        ValueError
            Si no existe un nodo con la etiqueta especificada.
        """
        # Primero vamos a usar un diccionario para que sea mas facil 
        if etiqueta in self.conjunto_nodos.keys():
            return self.conjunto_nodos[etiqueta]
        else:
            raise ValueError(f"El nodo {etiqueta} no existe")

    def obtener_arista(self, nodo_1, nodo_2):
        """
        Obtiene la arista que conecta dos nodos específicos en el grafo.

        Verifica ambas direcciones si el grafo no es dirigido.

        Parameters
        ----------
        nodo_1 : object
            El primer objeto nodo en la arista.
        nodo_2 : object
            El segundo objeto nodo en la arista.

        Returns
        -------
        arista : Arista
            El objeto arista que conecta 'nodo_1' y 'nodo_2'.

        Raises
        ------
        ValueError
            Si la arista entre los dos nodos no existe en el grafo.
        """
        # Primero verificamos la dirección original de la arista
        if (nodo_1,nodo_2) in self.conjunto_aristas.keys():
            return self.conjunto_aristas[(nodo_1,nodo_2)]
        # Si no esta, debemos revisar la otra dirección solo si
        # el grafo no es dirigido:
        elif not self.dirigido:
            if (nodo_2,nodo_1) in self.conjunto_aristas.keys():
                return self.conjunto_aristas[(nodo_2,nodo_1)]
        else:
            raise ValueError(f"La arista {(nodo_1,nodo_2)} no existe")

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
                # # o que sean de la penultima fila
                # if (not esta_en_orilla ) and (not esta_en_ultima_fila):
                #     arista_propuesta = Arista(self.obtener_nodo(i), self.obtener_nodo(i+(m+1)))
                #     self.aniadir_arista(arista_propuesta)

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
            self.conjunto_nodos = OrderedDict()
            self.conjunto_aristas = OrderedDict()
        
        # Ahora si generamos nuestra lista de n nodos
        # del 1 al n
        [self.aniadir_nodo(Nodo(i+1)) for i in range(n)]
        lista_nodos = list(self.conjunto_nodos.values())
        # Mientras no hayamos completado las conexiones
        while len(self.conjunto_aristas) < m:
            
            # Ahora vamos a hacer choice para elegir
            nodo_1, nodo_2 = choice(lista_nodos), choice(lista_nodos)
            arista_propuesta = Arista(nodo_1,nodo_2)
            if not self.emparejamiento_valido(arista_propuesta, self.dirigido):
                #print(arista_propuesta, self.emparejamiento_valido(arista_propuesta))
                continue
            else:
                self.aniadir_arista(arista_propuesta)


    def grafo_gilbert(self, n, p, dirigido=False):
        """Genera grafo aleatorio con el modelo Gilbert.

        Genera un grafo aleatorio donde cada posible arista se crea con una probabilidad dada.

        Parameters
        ----------
        n : int
            Número total de nodos en el grafo generado.
        p : float
            Probabilidad de crear una arista entre dos nodos cualesquiera.
        dirigido : bool, opcional
            Indica si el grafo es dirigido (True) o no dirigido (False). El valor predeterminado es False.

        Returns
        -------
        None
            La función modifica el grafo en su lugar (self).

        Notes
        -----
        El modelo Gilbert es un modelo de grafo aleatorio donde cada posible arista
        se crea con una probabilidad fija p, independientemente de las demás aristas.
        """

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
            gano_volado = self._echar_volado(p)
            # print(gano_volado)
            arista_propuesta = Arista(nodo_1,nodo_2)
            if gano_volado and self.emparejamiento_valido(arista_propuesta, self.dirigido):
                self.aniadir_arista(arista_propuesta)

    def grafo_geografico(self, n, r, dirigido=False):
        """Genera grafo aleatorio con el modelo geográfico simple.

        Genera un grafo aleatorio donde los nodos se distribuyen uniformemente
        en un espacio bidimensional (cuadrado unitario) y se conectan si la
        distancia euclidiana entre ellos es menor o igual a un radio dado.

        Parameters
        ----------
        n : int
            Número total de nodos en el grafo generado.
        r : float
            Radio de conexión. Dos nodos se conectan si su distancia es menor o igual a r.
        dirigido : bool, opcional
            Indica si el grafo es dirigido (True) o no dirigido (False). El valor predeterminado es False.

        Returns
        -------
        None
            La función modifica el grafo en su lugar (self).

        Notes
        -----
        El modelo geográfico simple genera grafos donde la conectividad depende de la
        distancia espacial entre los nodos. Los nodos se distribuyen uniformemente
        en un cuadrado unitario [0, 1] x [0, 1].
        """
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
        """Genera grafo aleatorio con el modelo Barabási-Albert.

        Variante del modelo Gn,d Barabási-Albert. Coloca n nodos uno por uno,
        asignando a cada uno d aristas a vértices distintos, donde la probabilidad
        de que el vértice nuevo se conecte a un vértice existente v es proporcional
        a la cantidad de aristas que v tiene actualmente.

        Parameters
        ----------
        n : int
            Número total de nodos en el grafo generado.
        d : int
            Número máximo de aristas que se asignan a un nodo
        dirigido : bool, opcional
            Indica si el grafo es dirigido (True) o no dirigido (False). El valor predeterminado es False.

        Returns
        -------
        None
            La función modifica el grafo en su lugar (self).
        """

        # Definimos nuestra función para calcular la probabilidad
        def formula_probabilidad(nodo, d):
            # la formula es 1  - deg(v)/d
            p = 1 - (nodo.obtener_grado()/d)
            return p
            
        # Conforme vamos generando los nodos vamos a tratar de conectar 
        # los nodos anteriores con una función de probabilidad
        # que se calcula como deg(r)/d 
        # para esto deberíamos de mantener el registro de todos los nodos
        # que estan conectados unos a los otros
        # para esto usare al diccionario atributos con el atributo vecinos
        # que será una lista


        # Primero generamos todos los nodos
        # Primero vamos  añadir todos esos m*n nodos:
        # Si el grafo no es vacio lo vaciamos xD
        if not self.es_vacio():
            self.conjunto_aristas = OrderedDict()
            self.conjunto_nodos = OrderedDict()

        etiquetas_nodos = [(i+1) for i in range(n)]
        # Esto es para aleatorizar los nombres de los nodos
        # Para crear la estructura deseada
        random.shuffle(etiquetas_nodos)

        # Creando los nodos:
        for etiqueta  in etiquetas_nodos:
            # Creamos los nodos con un atributo vecinos que es una lista
            nodo_creado = Nodo(etiqueta, {"vecinos":[]})
            self.aniadir_nodo(nodo_creado)
            # Para cada nodo que ya está en 
            for nodo in self.conjunto_nodos.values():
                # Recorremos todos los nodos ya creados previamente

                # Si es el mismo nodo pues ya terminamos de recorrer del inicio hasta 
                # donde ya estabamos con nuestro nodo tons saltamos a la sig
                # iteraciob                
                if nodo == nodo_creado:
                    break
                else:
                    # De otra forma, tratamos de establecer la conexion
                    # con la funcion de probabilidad

                    # Creamos la arista propuesta
                    arista_propuesta = Arista(nodo, nodo_creado)
                    # Calculamos la probabilidad
                    probabilidad = formula_probabilidad(nodo, d)
                    # echamos el volado
                    gano_volado = self._echar_volado(probabilidad)
                    # Ahora si ganamos el volado establecemos la conexion
                    # no sin antes verificarla
                    conexion_valida = (
                        gano_volado
                        and self.emparejamiento_valido(arista_propuesta, self.dirigido)
                        and nodo.obtener_grado() <= d
                    )

                    if conexion_valida:
                        self.aniadir_arista(arista_propuesta)

    def grafo_dorogovtsev_mendes(self, n, dirigido=False):
        """Genera grafo aleatorio con el modelo Dorogovtsev-Mendes.

        El modelo Dorogovtsev-Mendes comienza con un triángulo inicial y, en cada paso, 
        agrega un nuevo nodo conectado a los dos extremos de una arista elegida al azar.

        Parameters
        ----------
        n : int
            Número total de nodos en el grafo generado.
        dirigido : bool, opcional
            Indica si el grafo es dirigido (True) o no dirigido (False). El valor predeterminado es False.

        Returns
        -------
        None

        Notes
        -----
        El modelo Dorogovtsev-Mendes es un modelo de grafo de crecimiento que genera grafos libres de escala.
        El grafo inicial es un triángulo (K3).
        En cada paso, se selecciona una arista aleatoria y se
        agrega un nuevo nodo conectado a los dos nodos de la arista seleccionada.
        """

        if not self.es_vacio():
            self.conjunto_aristas = OrderedDict()
            self.conjunto_nodos = OrderedDict()
        # Generamos un triangulo al inicio
        nodo_1, nodo_2, nodo_3 = Nodo(1), Nodo(2), Nodo(3)
        self.aniadir_nodo(nodo_1)
        self.aniadir_nodo(nodo_2)
        self.aniadir_nodo(nodo_3)
        # Ahora conectamos los 3 nodos:
        self.aniadir_arista(Arista(nodo_1, nodo_2))
        self.aniadir_arista(Arista(nodo_2, nodo_3))
        self.aniadir_arista(Arista(nodo_1, nodo_3))
        
        del nodo_1
        del nodo_2
        del nodo_3

        # Ahora ya tenemos el triangulo simplemente hacemos lo siguiente:
        # Generamos n nodos:
        for i in range(4, n+1):
            # Creamos el nodo y lo agregamos:
            nodo_creado = Nodo(i)
            self.aniadir_nodo(nodo_creado)
            # Primero seleccionamos un arista al azar
            arista_elegida = choice(list(self.conjunto_aristas.values()))
            # y conectamos nuestro nodo a esa arista:
            arista_1 = Arista(nodo_creado, arista_elegida.nodo_1)
            arista_2 = Arista(nodo_creado, arista_elegida.nodo_2)
            # Validamos las conexiones y posteriormente agregamos:
            if self.emparejamiento_valido(arista_1, self.dirigido):
                self.aniadir_arista(arista_1)
            if self.emparejamiento_valido(arista_2, self.dirigido):
                self.aniadir_arista(arista_2)

    
    def guardar_graphviz(self,  nombre_archivo="graph.dot", mostrar_pesos = False, directorio="proyecto_1/archivos_graphviz"):
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

        Notes
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
                if not mostrar_pesos:
                    archivo_dot.write(f"    {nodo};\n")
                else:
                    peso = self.conjunto_nodos[nodo].atributos["distancia"]
                    if peso == 0:
                        archivo_dot.write(f"    \"{nodo}\" [label=\"Raiz {nodo}\"];\n")
                    elif peso is None:
                        archivo_dot.write(f"    {nodo};\n")
                    else:
                        archivo_dot.write(f"    \"{nodo}\" [label=\"Nodo {nodo} ({peso})\"];\n")

            for arista in self.conjunto_aristas.values():
                if not mostrar_pesos:
                    archivo_dot.write(f"    {arista.nodo_1}{apuntador}{arista.nodo_2};\n")
                else:
                    peso = arista.atributos["peso"]
                    archivo_dot.write(f"    {arista.nodo_1}{apuntador}{arista.nodo_2} [label=\"{peso}\"];\n")
            archivo_dot.write("}")
        print(f"Grafo guardado en: {ruta_completa}")

    # --- PARTE DEL PROYECTO 2 ---

    # Utilizando la biblioteca de grafos desarrollada en el proyecto 1, 
    # implementar los algoritmos BFS y DFS (recursivo e iterativo) de tal forma que dado un nodo fuente (s)
    # calculen el árbol inducido por los algoritmos mencionados
    # es decir, desarrollar los métodos en la clase Grafo:

    def BFS(self, s):
        """
        Realiza una Búsqueda en Amplitud (BFS) desde un nodo inicial.

        Construye un árbol BFS y organiza los nodos por capas/profundidad.
        Los nodos visitados se marcan con el atributo "visitado".

        Parameters
        ----------
        s : int
            La etiqeutaa del nodo de inicio para el BFS.

        Returns
        -------
        arbol_BFS : Grafo
            Un nuevo objeto Grafo que representa el árbol de la BFS.
        lista_capas : dict
            Un diccionario donde las claves son los números de capa (profundidad)
            y los valores son listas de nodos en esa capa.
        """
        # Obtenemos bien el nodo
        s = self.obtener_nodo(s)
        s.atributos["visitado"] = True
        # Inicializamos el árbol que está vacio
        arbol_BFS = Grafo("arbol_BFS_" + self.nombre_grafo)
        # Añadimos el nodo
        arbol_BFS.aniadir_nodo(s)

        contador_capa = 0

        # Nuestro diccionario de capas
        lista_capas = {0:[s]}

        # Mientras la lista no esté vacía
        while lista_capas[contador_capa]:
            # Añadimos la siguiente capa siendo vacia
            lista_capas[contador_capa + 1] = []
            for nodo in lista_capas[contador_capa]:
                for nodo_vecino in nodo.atributos["vecinos"]:
                    if "visitado" not in nodo_vecino.atributos:
                        # Marcamos como visitado
                        nodo_vecino.atributos["visitado"] = True
                        # Añadimos esta conexión al arbol:
                        conexion = Arista(nodo, nodo_vecino)
                        arbol_BFS.aniadir_nodo(nodo_vecino)
                        arbol_BFS.aniadir_arista(conexion)
                        lista_capas[contador_capa + 1].append(nodo_vecino)
            contador_capa +=1
        return arbol_BFS, lista_capas

    def DFS_R(self, s, nodo_padre = None, arbol_DFS = None):
        """
        Realiza una Búsqueda en Profundidad (DFS) de forma recursiva.

        Construye un árbol DFS explorando el grafo recursivamente desde un nodo de inicio.

        Parameters
        ----------
        s : int
            La etiqueta del nodo actual que se está visitando en la recursión.
        nodo_padre : object, optional
            El objeto del nodo padre en el árbol DFS. Es None en la llamada inicial.
        arbol_DFS : Grafo, optional
            El objeto Grafo que representa el árbol DFS en construcción.
            Se inicializa internamente en la primera llamada recursiva.

        Returns
        -------
        arbol_DFS : Grafo
            Un nuevo objeto Grafo que representa el árbol de la DFS construida.
        """
        # Si no hemos incializado el arbol es
        # La primera iteración
        if arbol_DFS == None:
            # Incializamos el arbol
            arbol_DFS = Grafo("arbol_DFS_R_" + self.nombre_grafo)
            # añadimos el nodo de inicio al arbol
            nodo_raiz = self.obtener_nodo(s)
            arbol_DFS.aniadir_nodo(nodo_raiz)
        # Obtenemos el nodo
        s = self.obtener_nodo(s)
        # Lo añadimos al arbol
        # arbol_DFS.aniadir_nodo(s)
        # Marcamos como visitado
        s.atributos["visitado"] = True

        # Si no es el nodo raíz, añadimos la conexión al padre
        if nodo_padre is not None:
            # Creamos la conexión entre el nodo padre y el nodo actual (s)
            conexion = self.obtener_arista(nodo_padre, s)
            arbol_DFS.aniadir_nodo(s)
            arbol_DFS.aniadir_arista(conexion)
        elif len(arbol_DFS.conjunto_nodos) == 0: # Aseguramos que la raíz se añada si el bloque anterior no se ejecutó
            arbol_DFS.aniadir_nodo(s)

        # Para cada vecino que tenga
        for nodo_vecino in s.atributos["vecinos"]:
            # Si no está visitado entonces
            if "visitado" not in nodo_vecino.atributos:
                # Si ya hay un nodo padre entonces
                if nodo_padre is not None:
                    # Creamos la conexión entre
                    # el nodo padre y el nodo que estamos descubriendo que es s
                    conexion = self.obtener_arista(nodo_padre, s)
                        #arbol_BFS.aniadir_nodo(nodo_vecino)
                    arbol_DFS.aniadir_arista(conexion)
                # Llamada recurisva para descubrir el siguiente nodo
                self.DFS_R(nodo_vecino.etiqueta, s, arbol_DFS)
        return arbol_DFS

    def DFS_I(self, s):
        """
        Realiza una Búsqueda en Profundidad (DFS) de forma iterativa.

        Construye un árbol DFS utilizando una pila para explorar el grafo.

        Parameters
        ----------
        s : int
            La etiqueta del nodo de inicio para DFS. Se usa para obtener el objeto nodo.

        Returns
        -------
        arbol_DFS : Grafo
            Un nuevo objeto Grafo que representa el árbol del DFS.
        """
        # Primero vamos a inicializar el árbol:
        arbol_DFS = Grafo("arbol_DFS_I_" + self.nombre_grafo)
        # Obtenemos el nodo raíz
        s = self.obtener_nodo(s)

        # Va a ser una pila de tuplas
        # donde cuando se llama al nodo
        # entonces también se adjunta la referncia a su padre
        pila = deque([(s,None)])
        # Conjunto vacío
        nodos_visitados = set()

        # Mientras la pila no esté vacía
        while pila:
            nodo_visitado, nodo_padre = pila.pop()
            if nodo_visitado in nodos_visitados: continue
            # Marcamos como nodo visitado
            nodos_visitados.add(nodo_visitado)
            arbol_DFS.aniadir_nodo(nodo_visitado)
            # Si no es el nodo raíz entonces generamos
            # la conexión con el padre
            if nodo_padre is not None:
                conexion = Arista(nodo_padre, nodo_visitado)
                arbol_DFS.aniadir_arista(conexion)
            # Ahora tomamos cada vecino de ese nodo
            for nodo_vecino in nodo_visitado.atributos["vecinos"]:
                if nodo_vecino not in nodos_visitados:
                    pila.append((nodo_vecino, nodo_visitado))
        return arbol_DFS

    # Entregables, en el repositorio:
    # Código fuente
    # Archivos de grafos generados. Tres por cada generador (con 30, 100 y 500 nodos).
    # Archivos de grafos calculados. Tres por cada grafo generado (un BFS y dos DFS).
    # Imágenes de la visualización de cada grafo (generados y calculados).

    # Utilizando la biblioteca de grafos desarrollada en el proyecto 1, implementar el algoritmo de Dijkstra de tal forma que dado un nodo fuente (s), calcule el árbol de caminos más cortos; es decir, desarrollar el método en la clase Grafo:
    # def Dijkstra(self, s):

    # Entregables en el repositorio:
    # Código fuente
    # Archivos de grafos generados. Dos por cada generador aleatorio (uno con "pocos" y otro con "muchos" nodos).
    # Archivos de grafos calculados. Se debe poder visualizar la distancia que se calculó al nodo origen. Si el nodo original se llama "nodo_2", en el nodo resultante debe llamarse "nodo_2 (22.45)" (dónde 22.45 es la distancia del "nodo_2" al nodo de origen.
    # Imágenes de la visualización de cada grafo (generados y calculados)
    def Dijkstra(self, s):
        """
        Calcula las rutas más cortas desde un nodo de origen usando el algoritmo de Dijkstra.

        Construye un árbol de caminos más cortos y determina la distancia mínima
        a cada nodo alcanzable desde el origen.

        Parameters
        ----------
        s : int
            La etiqueta del nodo donde va a iniciar el algoritmo.

        Returns
        -------
        arbol_dijkstra : Grafo
            Un nuevo objeto Grafo que representa el árbol de caminos más cortos.

        Notes
        -----
        Este algoritmo asume que los pesos de las aristas son no negativos.

        """
        # Primero vamos a inicializar el árbol:
        arbol_dijkstra = Grafo("arbol_dijkstra_" + self.nombre_grafo)
        # inicializamos los predecesores de los nodos
        # Obtenemos el nodo raíz
        s = self.obtener_nodo(s)
        # Algoritmo de dijsktra
        cola_prioridad = heapdict()
        visitados = set()
        for nodo in [n for n in self.conjunto_nodos.values() if n != s]:
            # Asignamos infinito a delmin a todos los nodos menos s
            cola_prioridad[nodo] = inf
            nodo.atributos["padre"] = None
        # Al nodo raíz asignamos 0
        cola_prioridad[s] = 0

        # Mientras la cola no esté vacía
        while cola_prioridad:
            u, dist_u = cola_prioridad.popitem()
            u.atributos["distancia"] = dist_u
            visitados.add(u)
            
            # Aquí agregamos al nodo por que ya lo estamos visitando:
            arbol_dijkstra.aniadir_nodo(u)
            if "vecinos" not in u.atributos: continue
            for nodo_vecino in u.atributos["vecinos"]:
                arista = self.obtener_arista(u, nodo_vecino)
                # Obtener peso:
                peso_arista = arista.atributos["peso"]
                # Si no hemos encontrado el camino minimo hacia el nodo
                if nodo_vecino not in visitados:
                    # Si encontramos un camino más corto
                    if cola_prioridad[nodo_vecino] > dist_u + peso_arista:
                        cola_prioridad[nodo_vecino] = dist_u + peso_arista
                        # Y actualizamos cual es el padre para luego armar el árbol:
                        nodo_vecino.atributos["padre"] = u
        
        # Ahora armamos el arbol:
        for nodo in self.conjunto_nodos.values():
            if nodo == s:
                continue
            padre = nodo.atributos["padre"]
            # Agregamos esa arista entre el nodo y el padre:
            arista = self.obtener_arista(nodo, padre)
            # añadimos esa misma arista
            arbol_dijkstra.aniadir_arista(arista)
        
        return arbol_dijkstra

    # Proyecto 4 - Algoritmos Kruskal y Prim
    # Fecha límite: 3 jun
    # Utilizando la biblioteca de grafos desarrollada en el proyecto 1,
    # implementar los algoritmos de Kruskal (directo e inverso) y 
    # Prim de tal forma que calculen el árbol de expansión mínima; es decir,
    # desarrollar los métodos en la clase Grafo:

    def KruskalD(self):
        """
        Calcula un Árbol de Expansión Mínima (MST) usando un algoritmo tipo Kruskal.

        Ordena las aristas por peso y las añade al MST si no forman un ciclo.
        La detección de ciclos se realiza mediante una Búsqueda en Amplitud (BFS).

        Parameters
        ----------
        None

        Returns
        -------
        minimum_spanning_tree : Grafo
            Un nuevo objeto Grafo que representa el Árbol de Expansión Mínima.
        """
        # Incializamos el conjunto de aristas:
        aristas_MST = set()
        num_aristas_en_MST = 0
        # Primero obtenemos una lista de aristas por su costo
        # Esto lo hare con una heapdict
        pila_aristas = heapdict()
        for arista in self.conjunto_aristas.values():
            # Las ordenamos automaticamente por peso
            # Esto cuesta O(log(k)) que siendo n
            # es O(n log(n))
            pila_aristas[arista] = arista.atributos["peso"]
        # Ya que tenemos la lista de aristas por peso
        # Emepzamos a recorrer los nodos
        while pila_aristas:
            arista,_ = pila_aristas.popitem()
            if num_aristas_en_MST == len(self.conjunto_nodos.keys()) - 1:
                break
            # Creamos un grafo temporal
            grafo_temporal = self._iniciar_grafo_con_aristas(aristas_MST)
            u = arista.nodo_1
            v = arista.nodo_2

            # Como mi grafo temporal es solo una referencia
            # a cosas de mi grafo original, entonces lo que hago es
            arbol_BFS, _ = grafo_temporal.BFS(u.etiqueta)
            # Ahora revisamos si v se puede alcanzar desde u
            # es decir, v debe ser parte del conjunto de nodos
            # del arbol BFS

            # si es alcanzable entonces creariamos un ciclo
            # por lo no la agregamos 
            if v in arbol_BFS.conjunto_nodos.values():
                continue
            else:
                aristas_MST.add(arista)
                num_aristas_en_MST += 1
        # Finalmente creamos el MST:
        minimum_spanning_tree = Grafo(self.nombre_grafo + "_MST")
        for arista in aristas_MST:
            if arista.nodo_1 not in minimum_spanning_tree.conjunto_nodos.values():
                arista.nodo_1.atributos["distancia"] = None
                minimum_spanning_tree.aniadir_nodo(arista.nodo_1)
            if arista.nodo_2 not in minimum_spanning_tree.conjunto_nodos.values():
                arista.nodo_2.atributos["distancia"] = None
                minimum_spanning_tree.aniadir_nodo(arista.nodo_2)
            minimum_spanning_tree.aniadir_arista(arista)
        
        return minimum_spanning_tree

    
    def KruskalI(self):
        """
        Calcula un Árbol de Expansión Mínima (MST) usando el algoritmo Kruskal inverso (Reverse-Delete).

        Comienza con todas las aristas y elimina progresivamente las más pesadas
        si no desconectan el grafo. La conectividad se verifica con BFS.

        Parameters
        ----------
        None

        Returns
        -------
        minimum_spanning_tree : Grafo
            Un nuevo objeto Grafo que representa el Árbol de Expansión Mínima resultante.
        """
        # variable para ver si se desconecta o no
        num_nodos = len(self.conjunto_nodos.values())
        # Incializamos el conjunto de aristas:
        aristas_MST = set()
        # Primero obtenemos una lista de aristas por su costo
        # Esto lo hare con una heapdict
        pila_aristas = heapdict()
        for arista in self.conjunto_aristas.values():
            # guardamos en el orden inverso
            pila_aristas[arista] = -arista.atributos["peso"]
            # Guardamos todas las aristas
            aristas_MST.add(arista)
        # Ya que tenemos la lista de aristas por peso
        # Emepzamos a recorrer los aristas en orden inverso
        # Practicamente agregamos todas:
        while pila_aristas:
            arista,_ = pila_aristas.popitem()
            if len(aristas_MST) == len(self.conjunto_nodos.keys()) - 1:
                break
            # Quitamos la arista:
            aristas_MST.discard(arista)
            # Creamos un grafo temporal menos la arista
            grafo_temporal = self._iniciar_grafo_con_aristas(aristas_MST)

            u = arista.nodo_1
            # Como mi grafo temporal es solo una referencia
            # a cosas de mi grafo original, entonces lo que hago es
            arbol_BFS, _ = grafo_temporal.BFS(u.etiqueta)

            # si desde u se pueden llegar a todos los nodos
            # quiere decir que mi grafo sigue conectado
            if len(arbol_BFS.conjunto_nodos.values()) == num_nodos:
                continue
            else:
                # Si al quitarla se desconecta simplemente la ponemos en su lugar XD
                aristas_MST.add(arista)
                # Finalmente creamos el MST:
        minimum_spanning_tree = Grafo(self.nombre_grafo + "_MST")
        for arista in aristas_MST:
            if arista.nodo_1 not in minimum_spanning_tree.conjunto_nodos.values():
                arista.nodo_1.atributos["distancia"] = None
                minimum_spanning_tree.aniadir_nodo(arista.nodo_1)
            if arista.nodo_2 not in minimum_spanning_tree.conjunto_nodos.values():
                arista.nodo_2.atributos["distancia"] = None
                minimum_spanning_tree.aniadir_nodo(arista.nodo_2)
            minimum_spanning_tree.aniadir_arista(arista)
        return minimum_spanning_tree
        
    def Prim(self):
        """
        Calcula un Árbol de Expansión Mínima (MST) usando el algoritmo de Prim.

        Construye el MST creciendo desde un nodo inicial, añadiendo iterativamente
        la arista de menor peso que conecta un nodo en el árbol con uno fuera de él.

        Parameters
        ----------
        None

        Returns
        -------
        minimum_spanning_tree : Grafo
            Un nuevo objeto Grafo que representa el Árbol de Expansión Mínima.

        Notes
        -----
        El algoritmo inicia desde el nodo cuya etiqueta es '1'. Se asume que el grafo es conexo.
        """
        # Asigmanos un conjunto S y una cola de prioridad
        nodos_MST = set()
        # Creamos el conjunto de aristas de nuestro arbol
        aristas_MST = set()
        # Creamos el diccionario de aristas potenciales:
        arista_temporal = {}
        cola_prioridad = heapdict()
        # Primero debemos inicializar
        # Todos los vertices con distancia infinita
        for nodo in self.conjunto_nodos.values():
            # Ponemos la distancia como infinita
            if nodo.etiqueta == 1:
                nodo.atributos["distancia"] = 0
            else:
                nodo.atributos["distancia"] = inf
            cola_prioridad[nodo] = nodo.atributos["distancia"]

        # Ahora vamos sacando las cosas de la cola de prioridad:
        while cola_prioridad:
            u,_ = cola_prioridad.popitem()
            if u in nodos_MST: continue
            # Lo insertamos en S
            nodos_MST.add(u)
            # Agregamos la arista al MST:
            if u in arista_temporal:
                aristas_MST.add(arista_temporal[u])
            # Ahora para cada arista que sale de u:
            for nodo_vecino in u.atributos["vecinos"]:
                # Obtenemos la arista:
                arista = self.obtener_arista(u, nodo_vecino)
                if (nodo_vecino not in nodos_MST) and (arista.atributos["peso"] < nodo_vecino.atributos["distancia"]):
                    # Establecemos la distancia del nodo como el peso de la arista
                    nodo_vecino.atributos["distancia"] = arista.atributos["peso"]
                    # Actualizamos la cola de prioridades
                    cola_prioridad[nodo_vecino] = nodo_vecino.atributos["distancia"]
                    # Actualizamos el diccionario de posibles aristas chipocludas:
                    arista_temporal[nodo_vecino] = arista
        # Finalmente creamos el MST:
        minimum_spanning_tree = Grafo(self.nombre_grafo + "_MST")
        for arista in aristas_MST:
            if arista.nodo_1 not in minimum_spanning_tree.conjunto_nodos.values():
                arista.nodo_1.atributos["distancia"] = None
                minimum_spanning_tree.aniadir_nodo(arista.nodo_1)
            if arista.nodo_2 not in minimum_spanning_tree.conjunto_nodos.values():
                arista.nodo_2.atributos["distancia"] = None
                minimum_spanning_tree.aniadir_nodo(arista.nodo_2)
            minimum_spanning_tree.aniadir_arista(arista)
        # y así creamos el MST
        return minimum_spanning_tree

    # Entregables en el repositorio

    #     Código fuente
    #     Archivos de grafos generados. Dos por cada generador (uno con "pocos" y otro con "muchos" nodos).
    #     Archivos de grafos calculados.
    #     Imágenes de la visualización de cada grafo (generados y calculados)
    #     Capturas de pantalla donde se muestre el valor del MST