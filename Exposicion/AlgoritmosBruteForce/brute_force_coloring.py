def is_valid(graph, colors):
    for u in range(len(graph)):
        for v in graph[u]:
            if colors[u] == colors[v]:
                return False
    return True

def brute_force_coloring(graph, k):
    from itertools import product
    n = len(graph)
    for assignment in product(range(1, k+1), repeat=n):
        if is_valid(graph, assignment):
            return assignment
    return None


if __name__ == "__main__":
    # Grafo con 6 vértices
    graph = [
        [1, 5, 2],   # conexiones de nodo 0
        [0, 2],      # nodo 1
        [1, 3, 0, 5],# nodo 2
        [2, 4],      # nodo 3
        [3, 5],      # nodo 4
        [0, 4, 2]    # nodo 5
    ]
    
    k = 3  # intentar colorear con 3 colores
    result = brute_force_coloring(graph, k)
    
    if result:
        print(f"Coloreo válido con {k} colores: {result}")
    else:
        print(f"No es posible colorear con {k} colores")
