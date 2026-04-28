from util import valid_path, cost
from functools import partial
from two_opt import two_opt
import random

def ga_tsp(initial_population, distances, generations):
    # refine initial population via two-opt
    for i in range(0, len(initial_population)):
        path = initial_population[i]
        path = two_opt(path, distances)
        initial_population[i] = path
    
    # sort population
    pop_sorted = sorted(initial_population, key=partial(cost, distances=distances))

    pop = select_fittest(pop_sorted, distances)
    return pop[0]

# replaces the paths with the highest costs with None
# population must be sorted beforehand
def select_fittest(population, distances):
    rm_amt = len(population)//4
    
    # still doesn't remove exactly half
    for i in range(0, rm_amt):
        population[len(population)-1-i] = None
        population[rm_amt:rm_amt*3:2] = [None for _ in range(rm_amt)]
    
    return population