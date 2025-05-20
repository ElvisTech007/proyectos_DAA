# Archivos de grafos generados. Dos por cada generador aleatorio (uno con "pocos" y otro con "muchos" nodos).
# Archivos de grafos calculados. 
# Se debe poder visualizar la distancia que se calculó al nodo origen. 
# Si el nodo original se llama "nodo_2", en el nodo resultante debe llamarse "nodo_2 (22.45)"
# (dónde 22.45 es la distancia del "nodo_2" al nodo de origen.
# Imágenes de la visualización de cada grafo (generados y calculados)
# Script donde se ejecutaran unicamente las funciones ya programadas
# De la generación de grafos aleatorios
from grafo import Grafo




# Puse esta cantidad de nodos por que si no, no se ve nada.
cantidad_nodos = [10, 50]#[50, 500]
dimensiones_malla = [(4, 4), (8, 8)]
grafo = Grafo("G_1")

# for n,m in dimensiones_malla:

#     grafo.grafo_malla(n,m, dirigido=False)
#     grafo.inicializar_pesos_aleatorios()
#     arbol_dijsktra = grafo.Dijkstra(1)
#     arbol_dijsktra.guardar_graphviz(nombre_archivo="arbol_Dijkstra_malla_" + str(n*m) + "_nodos.dot", mostrar_pesos=True)
for numero_nodos in cantidad_nodos:

    # # Grafo Erdon Renyi
    # grafo.grafo_erdos_renyi(numero_nodos, numero_nodos*4, dirigido=False)
    # grafo.inicializar_pesos_aleatorios()
    # arbol_dijsktra = grafo.Dijkstra(1)
    # arbol_dijsktra.guardar_graphviz(nombre_archivo="arbol_Dijkstra_erdos_renyi_" + str(numero_nodos) + ".dot", mostrar_pesos=True)


    # grafo.grafo_gilbert(numero_nodos,p=0.25, dirigido=False)
    # grafo.inicializar_pesos_aleatorios()
    # arbol_dijsktra = grafo.Dijkstra(1)
    # arbol_dijsktra.guardar_graphviz(nombre_archivo="arbol_Dijkstra_gilbert_" + str(numero_nodos) + "_nodos.dot", mostrar_pesos=True)

    # grafo.grafo_geografico(numero_nodos,r=0.4, dirigido=False)
    # grafo.inicializar_pesos_aleatorios()
    # arbol_dijsktra = grafo.Dijkstra(1)
    # arbol_dijsktra.guardar_graphviz(nombre_archivo="arbol_Dijkstra_geografico_" + str(numero_nodos) + "_nodos.dot", mostrar_pesos=True)

    # grafo.grafo_barabasi_albert(numero_nodos,d=4, dirigido=False)
    # grafo.inicializar_pesos_aleatorios()
    # arbol_dijsktra = grafo.Dijkstra(1)
    # arbol_dijsktra.guardar_graphviz(nombre_archivo="arbol_Dijkstra_barabasi_" + str(numero_nodos) + "_nodos.dot", mostrar_pesos=True)

    grafo.grafo_dorogovtsev_mendes(numero_nodos, dirigido=False)
    grafo.inicializar_pesos_aleatorios()
    arbol_dijsktra = grafo.Dijkstra(1)
    arbol_dijsktra.guardar_graphviz(nombre_archivo="arbol_Dijkstra_dogorostov_" + str(numero_nodos) + "_nodos.dot", mostrar_pesos=True)