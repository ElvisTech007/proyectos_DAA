from nodo import Nodo
from arista import Arista
from grafo import Grafo

from grafo import Grafo

grafo = Grafo("G_1")

grafo.grafo_erdos_renyi(10, 15, dirigido=False)

arbol,_ = grafo.BFS(1)
print(grafo)
print(_)
#arbol.guardar_graphviz("PRUEBA_BFS.dot")
#grafo.guardar_graphviz("pruebaXDDD.dot", "./")
#for _,nodo in grafo.conjunto_nodos.items():
#    print(_, nodo.atributos)
# arbol_BFS = grafo.BFS(1)
# print(arbol_BFS)
#grafo.DFS_R(1)
#grafo.DFS_I(1)
# print(grafo)
#grafo.guardar_graphviz(nombre_archivo="PRUEBA" + str(numero_nodos) + ".dot")