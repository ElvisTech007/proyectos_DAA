from nodo import Nodo
from arista import Arista
from grafo import Grafo

# # EJEMPLO DE DOCSTRING SCIPY/NUMPY
#     # """
#     # Descripción concisa de la función.

#     # Descripción detallada de la función (opcional). Puedes incluir más detalles
#     # sobre el propósito de la función, el algoritmo que utiliza, etc.

#     # Parámetros
#     # ----------
#     # parametro1 : tipo_de_dato
#     #     Descripción del parámetro 1.
#     # parametro2 : tipo_de_dato
#     #     Descripción del parámetro 2.
#     # parametro_opcional : tipo_de_dato, opcional
#     #     Descripción del parámetro opcional (si se proporciona). El valor predeterminado es None.

#     # Devuelve
#     # -------
#     # tipo_de_dato
#     #     Descripción del valor de retorno.

#     # Otros parámetros
#     # ----------------
#     # otros_parametros : tipo_de_dato, opcional
#     #     Descripción de otros parámetros opcionales (si los hay).

#     # """
# Crear 10 nodos
# Crear nodos
# nodos = [Nodo(i) for i in range(10)]

# # Crear aristas
# aristas = [
#     Arista(nodos[0], nodos[1]),
#     Arista(nodos[1], nodos[2]),
#     Arista(nodos[2], nodos[3]),
#     Arista(nodos[3], nodos[0]),
#     Arista(nodos[4], nodos[5]),
#     Arista(nodos[5], nodos[6]),
#     Arista(nodos[6], nodos[7]),
#     Arista(nodos[7], nodos[4]),
#     Arista(nodos[0], nodos[5]),
#     Arista(nodos[2], nodos[7]),
#     Arista(nodos[1], nodos[4]),
#     Arista(nodos[3], nodos[6]),
#     Arista(nodos[8], nodos[9]),
# ]

# # Crear un grafo y añadir nodos y aristas
# mi_grafo = Grafo()
# for nodo in nodos:
#     mi_grafo.aniadir_nodo(nodo)

# for arista in aristas:
#     mi_grafo.aniadir_arista(arista)

# # Imprimir el grafo
# print(mi_grafo)

# Crear el grafo
grafo = Grafo("G_1",dirigido=False)

# #Ahora voy a probar al algoritmo grafo_erdos_renyi
grafo.grafo_erdos_renyi(500, 1000, dirigido=False)
#print(grafo)
grafo.guardar_graphviz(nombre_archivo="grafo_erdos_renyi.dot")

# Ahora voy a probar al algoritmo grafo_malla
grafo.grafo_malla(24,24)
#print(grafo)
grafo.guardar_graphviz(nombre_archivo="grafo_malla.dot")









# from collections import OrderedDict
# from grafo import Grafo
# from nodo import Nodo
# from arista import Arista
# import random
# from random import choice

# Crear una instancia de Grafo
# mi_grafo = Grafo(nombre_grafo="MiGrafo", dirigido=False)

# lista_nodos = [Nodo(i) for i in range(10)]
# [mi_grafo.aniadir_nodo(nodo) for nodo in lista_nodos]
# for i in range(20):
#     arista = Arista(choice(lista_nodos), choice(lista_nodos))
#     mi_grafo.aniadir_arista(arista)
# mi_grafo.aniadir_arista(arista)# Imprimir el grafo
# print(mi_grafo)