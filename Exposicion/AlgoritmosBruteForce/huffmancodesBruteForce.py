import itertools

# Generar todos los árboles binarios completos con n hojas
def generate_trees(n):
    if n == 1:
        return ["x"]  # hoja
    trees = []
    for left_size in range(1, n):
        right_size = n - left_size
        for left in generate_trees(left_size):
            for right in generate_trees(right_size):
                trees.append((left, right))
    return trees

# Calcular longitudes de códigos desde un árbol
def code_lengths(tree, depth=0):
    if tree == "x":  # hoja
        return [depth]
    left, right = tree
    return code_lengths(left, depth+1) + code_lengths(right, depth+1)

# Fuerza bruta Huffman
def huffman_bruteforce(symbols, freqs):
    n = len(symbols)
    best_cost = float("inf")
    best_assignment = None
    for tree in generate_trees(n):
        lengths = code_lengths(tree)
        for perm in itertools.permutations(range(n)):
            cost = sum(freqs[perm[i]] * lengths[i] for i in range(n))
            if cost < best_cost:
                best_cost = cost
                best_assignment = {symbols[perm[i]]: lengths[i] for i in range(n)}
    return best_cost, best_assignment

# Ejemplo
symbols = ["A","B","C","D"]
freqs = [5,2,1,1]
cost, assignment = huffman_bruteforce(symbols, freqs)
print("Mejor costo:", cost)
print("Asignación (longitudes de códigos):", assignment)
