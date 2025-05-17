# Archivos de grafos generados. Dos por cada generador aleatorio (uno con "pocos" y otro con "muchos" nodos).
# Archivos de grafos calculados. 
# Se debe poder visualizar la distancia que se calculó al nodo origen. 
# Si el nodo original se llama "nodo_2", en el nodo resultante debe llamarse "nodo_2 (22.45)"
# (dónde 22.45 es la distancia del "nodo_2" al nodo de origen.
# Imágenes de la visualización de cada grafo (generados y calculados)
# Script donde se ejecutaran unicamente las funciones ya programadas
# De la generación de grafos aleatorios
from grafo import Grafo





cantidad_nodos = [500]#[50, 500]
#dimensiones_malla = [(8, 8), (23, 23)]
grafo = Grafo("G_1")

# for n,m in dimensiones_malla:

#     grafo.grafo_malla(n,m, dirigido=False)
#     arbol_dijsktra = grafo.Dijkstra(1)
#     arbol_dijsktra.guardar_graphviz(nombre_archivo="grafo_malla_" + str(n*m) + "_nodos.dot")
for numero_nodos in cantidad_nodos:

    # Grafo Erdon Renyi
    grafo.grafo_erdos_renyi(numero_nodos, numero_nodos*5, dirigido=False)
    grafo.inicializar_pesos_aleatorios()
    arbol_dijsktra = grafo.Dijkstra(1)
    #arbol_Dijkstra_erdos_renyi_PRUEBA.dot
    arbol_dijsktra.guardar_graphviz(nombre_archivo="AAAPRUEBAAAAA_" + str(numero_nodos) + ".dot", mostrar_pesos=True)
    # print(arbol_dijsktra)
    #arbol_dijsktra.guardar_graphviz(nombre_archivo="grafo_erdos_renyi_" + str(numero_nodos) + "_nodos.dot")


    # grafo.grafo_gilbert(numero_nodos,p=0.25, dirigido=False)
    # arbol_dijsktra = grafo.Dijkstra(1)
    # arbol_dijsktra.guardar_graphviz(nombre_archivo="grafo_gilbert_" + str(numero_nodos) + "_nodos.dot")

    # grafo.grafo_geografico(numero_nodos,r=0.2, dirigido=False)
    # arbol_dijsktra = grafo.Dijkstra(1)
    # arbol_dijsktra.guardar_graphviz(nombre_archivo="grafo_geografico_" + str(numero_nodos) + "_nodos.dot")

    # grafo.grafo_barabasi_albert(numero_nodos,d=4, dirigido=False)
    # arbol_dijsktra = grafo.Dijkstra(1)
    # arbol_dijsktra.guardar_graphviz(nombre_archivo="grafo_barabasi_" + str(numero_nodos) + "_nodos.dot")

    # grafo.grafo_dorogovtsev_mendes(numero_nodos, dirigido=False)
    # arbol_dijsktra = grafo.Dijkstra(1)
    # arbol_dijsktra.guardar_graphviz(nombre_archivo="grafo_dogorostov_" + str(numero_nodos) + "_nodos.dot")