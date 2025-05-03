from nodo import Nodo
from arista import Arista
from grafo import Grafo

from grafo import Grafo

grafo = Grafo("G_1")

grafo.grafo_malla(10, 10, dirigido=False)
#grafo.guardar_graphviz("pruebaXDDD.dot", "./")
#for _,nodo in grafo.conjunto_nodos.items():
#    print(_, nodo.atributos)
# arbol_BFS = grafo.BFS(1)
# print(arbol_BFS)
#grafo.DFS_R(1)
grafo.DFS_I(1)
#grafo.guardar_graphviz(nombre_archivo="PRUEBA" + str(numero_nodos) + ".dot")