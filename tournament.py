import numpy as np


def binary_tour(population, rank, cd):
    good_individuals = []

    while len(good_individuals) != 2:
        i = np.random.random_integers(0, len(population) - 1)
        j = np.random.random_integers(0, len(population) - 1)
        if (rank[i] < rank[j]) or (rank[i] == rank[j] and cd[i] > cd[j]):
            good_individuals.append(i)
        else:
            good_individuals.append(j)

    return good_individuals
