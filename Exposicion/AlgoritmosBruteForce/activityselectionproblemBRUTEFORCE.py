from itertools import combinations

def is_valid(schedule):
    # verificar que no haya solapamientos
    for i in range(len(schedule)):
        for j in range(i + 1, len(schedule)):
            if not (schedule[i][1] <= schedule[j][0] or schedule[j][1] <= schedule[i][0]):
                return False
    return True

def brute_force_activity_selection(activities):
    n = len(activities)
    best = []
    # probar todos los subconjuntos
    for r in range(1, n + 1):
        for subset in combinations(activities, r):
            if is_valid(subset) and len(subset) > len(best):
                best = list(subset)
    return best
#Complejidad: O(2^n * n²)
# Ejemplo
activities = [(1, 3), (2, 5), (4, 6)]
best_schedule = brute_force_activity_selection(activities)
print("Mejor solución (fuerza bruta):", best_schedule)
