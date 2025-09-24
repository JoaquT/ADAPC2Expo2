from itertools import permutations

def brute_force_job_scheduling(jobs):
    # jobs = [(id, deadline, profit)]
    max_profit = 0
    best_schedule = []
    for perm in permutations(jobs):
        time = 0
        profit = 0
        schedule = []
        for job in perm:
            if time < job[1]:  # dentro del deadline
                schedule.append(job)
                profit += job[2]
                time += 1
        if profit > max_profit:
            max_profit = profit
            best_schedule = schedule
    return best_schedule, max_profit

# Ejemplo
jobs = [("a",2,100),("b",1,19),("c",2,27),("d",1,25),("e",3,15)]
print(brute_force_job_scheduling(jobs))
