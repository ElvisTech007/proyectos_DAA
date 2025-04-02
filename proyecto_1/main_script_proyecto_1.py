# Script donde se ejecutaran unicamente las funciones ya programadas
# De la generación de grafos aleatorios
from grafo import Grafo

cantidad_nodos = [50, 200, 500]
grafo = Grafo("G_1")
for numero_nodos in cantidad_nodos:

    # Grafo Erdon Renyi
    grafo.grafo_erdos_renyi(numero_nodos, numero_nodos*3, dirigido=False)
    grafo.guardar_graphviz(nombre_archivo="grafo_erdos_renyi_" + str(numero_nodos) + "_nodos.dot")

    grafo.grafo_malla(int(numero_nodos/2),int(numero_nodos/2), dirigido=False)
    grafo.guardar_graphviz(nombre_archivo="grafo_malla_" + str(numero_nodos) + "_nodos.dot")

    grafo.grafo_gilbert(numero_nodos,p=0.2, dirigido=False)
    grafo.guardar_graphviz(nombre_archivo="grafo_gilbert_" + str(numero_nodos) + "_nodos.dot")

    grafo.grafo_geografico(numero_nodos,r=0.1, dirigido=False)
    grafo.guardar_graphviz(nombre_archivo="grafo_geografico_" + str(numero_nodos) + "_nodos.dot")

    grafo.grafo_barabasi_albert(numero_nodos,d=3, dirigido=False)
    grafo.guardar_graphviz(nombre_archivo="grafo_barabasi_" + str(numero_nodos) + "_nodos.dot")

    grafo.grafo_dorogovtsev_mendes(numero_nodos, dirigido=False)
    grafo.guardar_graphviz(nombre_archivo="grafo_dogorostov_" + str(numero_nodos) + "_nodos.dot")