from typing import List, Tuple

class Job:
    def __init__(self, id: str, deadline: int, profit: int):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs: List[Job]) -> Tuple[List[str], int]:
    # Ordenar por ganancia descendente
    jobs.sort(key=lambda job: job.profit, reverse=True)
    
    # Encontrar el deadline máximo para definir el número de slots
    max_deadline = max(job.deadline for job in jobs)
    
    # Inicializar slots como vacíos (-1 = libre)
    slots = [-1] * (max_deadline + 1)
    
    total_profit = 0
    scheduled_jobs = []
    
    # Intentar asignar cada trabajo en el slot más tarde posible
    for job in jobs:
        for t in range(job.deadline, 0, -1):  # de deadline hacia atrás
            if slots[t] == -1:
                slots[t] = job.id
                total_profit += job.profit
                scheduled_jobs.append(job.id)
                break
    
    return scheduled_jobs, total_profit


# Ejemplo de uso
jobs = [
    Job("A", 2, 100),
    Job("B", 1, 19),
    Job("C", 2, 27),
    Job("D", 1, 25),
    Job("E", 3, 15)
]

schedule, profit = job_scheduling(jobs)
print("Trabajos seleccionados:", schedule)
print("Ganancia total:", profit)
