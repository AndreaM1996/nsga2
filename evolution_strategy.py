import random
import numpy as np
from tournament import binary_tour


def crossover(parents):
    ind1, ind2 = parents[0], parents[1]
    size = min(len(ind1), len(ind2))
    cut_point = random.randint(1, size-1)
    ind1[cut_point:], ind2[cut_point:] = ind2[cut_point:], ind1[cut_point:]
    return ind1, ind2


def mutation(parent):
    mutation_rates = np.random.rand(len(parent))
    mutated = np.random.rand(len(parent))
    return np.where(mutation_rates < 0.05, mutated, parent)


def children(generationPt1, ranksPt1, cdPt1, n):
    children_list = []  # children
    while len(children_list) != n:  # create n children
        parents_ind = binary_tour(generationPt1, ranksPt1, cdPt1)  # pick two indices for parents
        parents = [generationPt1[parents_ind[0]], generationPt1[parents_ind[1]]]  # individual for indices above
        child1, child2 = crossover(parents)
        child1 = mutation(child1)
        child2 = mutation(child2)
        children_list.append(child1)
        children_list.append(child2)

    return children_list
