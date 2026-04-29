from util import valid_path, cost
from functools import partial
from two_opt import two_opt
import random

def ga_tsp(initial_population, distances, generations):
    # making a copy
    pop = initial_population
    # number of paths that will be compared in each tourney
    n = 2

    # refine initial population via two-opt
    for i in range(0, len(initial_population)):
        path = initial_population[i]
        path = two_opt(path, distances)
        initial_population[i] = path

    # iterate generations
    for gen in range(generations):
        newgen = []

        # tournament selection
        for i in range(len(pop)):
            # get winner A and B
            winner_A = tourney(pop, n, distances)
            winner_B = tourney(pop, n, distances)

            # crossover of A and B
            newgen.append(crossover(A, B))

        pop = newgen

    # sort population
    pop_sorted = sorted(pop, key=partial(cost, distances=distances))
        
    return pop_sorted[0]

# compares n paths from pop using distances and returns fittest path.
def tourney(pop, n, distances):
    competitors = []

    while len(competitors) < n:
        competitor = pop[random.randint(0, len(pop))]
        if competitor not in competitors:
            competitors.append(competitor)

    fittest = None
    lowest =  float('inf')

    for c in competitors:
        fitness = cost(c, distances)
        if fitness < lowest:
            fittest = c
            lowest = fitness
    
    return fittest
