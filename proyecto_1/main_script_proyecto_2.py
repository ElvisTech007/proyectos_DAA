# Script donde se ejecutaran unicamente las funciones ya programadas
# De la generación de grafos aleatorios
from grafo import Grafo

cantidad_nodos = [30, 100, 500]
dimensiones_malla = [(6,6), (10, 10), (23, 23)]
grafo = Grafo("G_1")

# for n,m in dimensiones_malla:

#     grafo.grafo_malla(n,m, dirigido=False)

#     # arbol_BFS, _ = grafo.BFS(1)
#     arbol_DFS_R = grafo.DFS_R(1)
#     #arbol_DFS_I = grafo.DFS_I(1)

#     # arbol_BFS.guardar_graphviz(nombre_archivo="arbol_BFS_malla_" + str(n*m) + "_nodos.dot")
#     arbol_DFS_R.guardar_graphviz(nombre_archivo="arbol_DFS_R_malla_" + str(n*m) + "_nodos.dot")
#     #arbol_DFS_I.guardar_graphviz(nombre_archivo="arbol_DFS_I_malla_" + str(n*m) + "_nodos.dot")


for numero_nodos in cantidad_nodos:

    grafo.grafo_erdos_renyi(numero_nodos, numero_nodos*5, dirigido=False)
    # arbol_BFS, _ = grafo.BFS(1)
    arbol_DFS_R = grafo.DFS_R(1)
    # arbol_DFS_I = grafo.DFS_I(1)

    # arbol_BFS.guardar_graphviz(nombre_archivo="arbol_BFS_erdos_renyi_" + str(numero_nodos) + "_nodos.dot")
    arbol_DFS_R.guardar_graphviz(nombre_archivo="arbol_DFS_R_erdos_renyi_" + str(numero_nodos) + "_nodos.dot")
    # arbol_DFS_I.guardar_graphviz(nombre_archivo="arbol_DFS_I_erdos_renyi_" + str(numero_nodos) + "_nodos.dot")


    grafo.grafo_gilbert(numero_nodos,p=0.25, dirigido=False)
    # arbol_BFS, _ = grafo.BFS(1)
    arbol_DFS_R = grafo.DFS_R(1)
    # arbol_DFS_I = grafo.DFS_I(1)

    # arbol_BFS.guardar_graphviz(nombre_archivo="arbol_BFS_gilbert_" + str(numero_nodos) + "_nodos.dot")
    arbol_DFS_R.guardar_graphviz(nombre_archivo="arbol_DFS_R_gilbert_" + str(numero_nodos) + "_nodos.dot")
    # arbol_DFS_I.guardar_graphviz(nombre_archivo="arbol_DFS_I_gilbert_" + str(numero_nodos) + "_nodos.dot")

    grafo.grafo_geografico(numero_nodos,r=0.2, dirigido=False)
    # arbol_BFS, _ = grafo.BFS(1)
    arbol_DFS_R = grafo.DFS_R(1)
    # arbol_DFS_I = grafo.DFS_I(1)

    # arbol_BFS.guardar_graphviz(nombre_archivo="arbol_BFS_geografico_" + str(numero_nodos) + "_nodos.dot")
    arbol_DFS_R.guardar_graphviz(nombre_archivo="arbol_DFS_R_geografico_" + str(numero_nodos) + "_nodos.dot")
    # arbol_DFS_I.guardar_graphviz(nombre_archivo="arbol_DFS_I_geografico_" + str(numero_nodos) + "_nodos.dot")

    grafo.grafo_barabasi_albert(numero_nodos,d=4, dirigido=False)
    # arbol_BFS, _ = grafo.BFS(1)
    arbol_DFS_R = grafo.DFS_R(1)
    # arbol_DFS_I = grafo.DFS_I(1)

    # arbol_BFS.guardar_graphviz(nombre_archivo="arbol_BFS_barabasi_" + str(numero_nodos) + "_nodos.dot")
    arbol_DFS_R.guardar_graphviz(nombre_archivo="arbol_DFS_R_barabasi_" + str(numero_nodos) + "_nodos.dot")
    # arbol_DFS_I.guardar_graphviz(nombre_archivo="arbol_DFS_I_barabasi_" + str(numero_nodos) + "_nodos.dot")

    grafo.grafo_dorogovtsev_mendes(numero_nodos, dirigido=False)
    # arbol_BFS, _ = grafo.BFS(1)
    arbol_DFS_R = grafo.DFS_R(1)
    # arbol_DFS_I = grafo.DFS_I(1)

    # arbol_BFS.guardar_graphviz(nombre_archivo="arbol_BFS_dogorostov_" + str(numero_nodos) + "_nodos.dot")
    arbol_DFS_R.guardar_graphviz(nombre_archivo="arbol_DFS_R_dogorostov_" + str(numero_nodos) + "_nodos.dot")
    # arbol_DFS_I.guardar_graphviz(nombre_archivo="arbol_DFS_I_dogorostov_" + str(numero_nodos) + "_nodos.dot")