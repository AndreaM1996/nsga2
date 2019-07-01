from functions import f_values
from sorting_strategy import nd_sort
from evolving import evolve


def nsga2(gen0, max_gen):
    gen = 0
    generation = gen0
    fronts, ranks = nd_sort(generation)

    while gen < max_gen:  # until we exceed max generation number, evolve
        generation = evolve(generation, ranks, fronts, True)
        fronts, ranks = nd_sort(generation)
        gen += 1

    f1 = [f_values(individual)[0] for individual in generation]
    f2 = [f_values(individual)[1] for individual in generation]
    pareto_x = []
    pareto_y = []
    for ind in fronts[0]:
        pareto_x.append(f1[ind])
        pareto_y.append(f2[ind])

    return pareto_x, pareto_y



