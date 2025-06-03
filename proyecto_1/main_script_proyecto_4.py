# Aquí van las pruebas para el minimum spanning tree
# Script donde se ejecutaran unicamente las funciones ya programadas
# De la generación de grafos aleatorios
from grafo import Grafo
cantidad_nodos = [10, 50]
# dimensiones_malla = [(4, 4), (8, 8)] # [(8, 8), (15, 15), (23, 23)]
grafo = Grafo("G_1")

# for n,m in dimensiones_malla:


#     # Grafo Erdon Renyi
#     grafo.grafo_malla(n,m, dirigido=False)
#     # Inicializamos el grafo:
#     grafo.inicializar_pesos_aleatorios()
#     grafo.guardar_graphviz(
#         "grafo_malla_" + str(n*m) + "_nodos.dot",
#         mostrar_pesos=True,
#         directorio="proyecto_1/archivos_graphviz/minimum_spanning_tree")
#     # Ya que hicimos eso solo deberíamos aplciar Kruskal o algo así:
#     MST_grafo = grafo.Prim()
#     MST_grafo.guardar_graphviz(
#         "MST_grafo_malla_" + str(n*m) + "_nodos.dot",
#         mostrar_pesos=True,
#         directorio="proyecto_1/archivos_graphviz/minimum_spanning_tree"
#         )



for numero_nodos in cantidad_nodos:
    pass
    # # Grafo Erdon Renyi
    # grafo.grafo_erdos_renyi(numero_nodos, numero_nodos*4, dirigido=False)
    # # Inicializamos el grafo:
    # grafo.inicializar_pesos_aleatorios()
    # grafo.guardar_graphviz(
    #     "grafo_erods_renyi_" + str(numero_nodos) + "_nodos.dot",
    #     mostrar_pesos=True,
    #     directorio="proyecto_1/archivos_graphviz/minimum_spanning_tree")
    # # Ya que hicimos eso solo deberíamos aplciar Kruskal o algo así:
    # MST_grafo = grafo.Prim()
    # MST_grafo.guardar_graphviz(
    #     "MST_grafo_erods_renyi_" + str(numero_nodos) + "_nodos.dot",
    #     mostrar_pesos=True,
    #     directorio="proyecto_1/archivos_graphviz/minimum_spanning_tree"
    #     )

    # Grafo Gilbert:
    # grafo.grafo_gilbert(numero_nodos,p=0.7, dirigido=False)
    # # Inicializamos el grafo:
    # grafo.inicializar_pesos_aleatorios()
    # grafo.guardar_graphviz(
    #     "grafo_gilbert_" + str(numero_nodos) + "_nodos.dot",
    #     mostrar_pesos=True,
    #     directorio="proyecto_1/archivos_graphviz/minimum_spanning_tree")
    # # Ya que hicimos eso solo deberíamos aplciar Kruskal o algo así:
    # MST_grafo = grafo.Prim()
    # MST_grafo.guardar_graphviz(
    #     "MST_grafo_gilbert_" + str(numero_nodos) + "_nodos.dot",
    #     mostrar_pesos=True,
    #     directorio="proyecto_1/archivos_graphviz/minimum_spanning_tree"
    #     )
        
    # Grafo geografico
    # grafo.grafo_geografico(numero_nodos,r=0.45, dirigido=False)
    # # Inicializamos el grafo:
    # grafo.inicializar_pesos_aleatorios()
    # grafo.guardar_graphviz(
    #     "grafo_geografico_" + str(numero_nodos) + "_nodos.dot",
    #     mostrar_pesos=True,
    #     directorio="proyecto_1/archivos_graphviz/minimum_spanning_tree")
    # # Ya que hicimos eso solo deberíamos aplciar Kruskal o algo así:
    # MST_grafo = grafo.Prim()
    # MST_grafo.guardar_graphviz(
    #     "MST_grafo_geografico_" + str(numero_nodos) + "_nodos.dot",
    #     mostrar_pesos=True,
    #     directorio="proyecto_1/archivos_graphviz/minimum_spanning_tree"
    #     )
    # grafo.grafo_geografico(numero_nodos,r=0.2, dirigido=False)
    # grafo.guardar_graphviz(nombre_archivo="grafo_geografico_" + str(numero_nodos) + "_nodos.dot")


    # Grafo Barabasi
    # grafo.grafo_barabasi_albert(numero_nodos,d=4, dirigido=False)
    # # Inicializamos el grafo:
    # grafo.inicializar_pesos_aleatorios()
    # grafo.guardar_graphviz(
    #     "grafo_barabasi_" + str(numero_nodos) + "_nodos.dot",
    #     mostrar_pesos=True,
    #     directorio="proyecto_1/archivos_graphviz/minimum_spanning_tree")
    # # Ya que hicimos eso solo deberíamos aplciar Kruskal o algo así:
    # MST_grafo = grafo.Prim()
    # MST_grafo.guardar_graphviz(
    #     "MST_grafo_barabasi_" + str(numero_nodos) + "_nodos.dot",
    #     mostrar_pesos=True,
    #     directorio="proyecto_1/archivos_graphviz/minimum_spanning_tree"
    #     )
    # grafo.grafo_barabasi_albert(numero_nodos,d=4, dirigido=False)
    # grafo.guardar_graphviz(nombre_archivo="grafo_barabasi_" + str(numero_nodos) + "_nodos.dot")


    # Grafo Dorogostev:
    grafo.grafo_dorogovtsev_mendes(numero_nodos, dirigido=False)
    # Inicializamos el grafo:
    grafo.inicializar_pesos_aleatorios()
    grafo.guardar_graphviz(
        "grafo_dogorostov_" + str(numero_nodos) + "_nodos.dot",
        mostrar_pesos=True,
        directorio="proyecto_1/archivos_graphviz/minimum_spanning_tree")
    # Ya que hicimos eso solo deberíamos aplciar Kruskal o algo así:
    MST_grafo = grafo.Prim()
    MST_grafo.guardar_graphviz(
        "MST_grafo_dogorostov_" + str(numero_nodos) + "_nodos.dot",
        mostrar_pesos=True,
        directorio="proyecto_1/archivos_graphviz/minimum_spanning_tree"
        )
    # grafo.grafo_dorogovtsev_mendes(numero_nodos, dirigido=False)
    # grafo.guardar_graphviz(nombre_archivo="grafo_dogorostov_" + str(numero_nodos) + "_nodos.dot")