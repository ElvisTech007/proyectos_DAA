# Script donde se ejecutaran unicamente las funciones ya programadas
# De la generación de grafos aleatorios
from grafo import Grafo

cantidad_nodos = [50, 200, 500]
# dimensiones_malla = [(8, 8), (15, 15), (23, 23)]
grafo = Grafo("G_1")

for n,m in dimensiones_malla:

    grafo.grafo_malla(n,m, dirigido=False)
    grafo.guardar_graphviz(nombre_archivo="grafo_malla_" + str(n*m) + "_nodos.dot")



for numero_nodos in cantidad_nodos:

    # Grafo Erdon Renyi
    grafo.grafo_erdos_renyi(numero_nodos, numero_nodos*5, dirigido=False)
    grafo.guardar_graphviz(nombre_archivo="grafo_erdos_renyi_" + str(numero_nodos) + "_nodos.dot")


    grafo.grafo_gilbert(numero_nodos,p=0.25, dirigido=False)
    grafo.guardar_graphviz(nombre_archivo="grafo_gilbert_" + str(numero_nodos) + "_nodos.dot")

    grafo.grafo_geografico(numero_nodos,r=0.2, dirigido=False)
    grafo.guardar_graphviz(nombre_archivo="grafo_geografico_" + str(numero_nodos) + "_nodos.dot")

    grafo.grafo_barabasi_albert(numero_nodos,d=4, dirigido=False)
    grafo.guardar_graphviz(nombre_archivo="grafo_barabasi_" + str(numero_nodos) + "_nodos.dot")

    grafo.grafo_dorogovtsev_mendes(numero_nodos, dirigido=False)
    grafo.guardar_graphviz(nombre_archivo="grafo_dogorostov_" + str(numero_nodos) + "_nodos.dot")