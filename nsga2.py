from functions import f_values
from sorting_strategy import nd_sort
from evolving import evolve


def nsga2(gen0, max_gen):
    gen = 0
    generation = gen0

    # below we evaluate objective functions for the first generation, sort in fronts and evolve first generation
    f1 = []
    f2 = []
    for individual in generation:
        values = f_values(individual)
        f1.append(values[0])
        f2.append(values[1])

    fronts, ranks = nd_sort(generation, f1, f2)
    generation = evolve(generation, ranks, fronts, f1, f2, parm=True)

    while gen < max_gen:  # until we exceed max generation number, evolve
        generation = evolve(generation, ranks, fronts, f1, f2)

        f1 = []
        f2 = []
        for individual in generation:
            values = f_values(individual)
            f1.append(values[0])
            f2.append(values[1])

        fronts, ranks = nd_sort(generation, f1, f2)

        gen += 1

    pareto_x = []
    pareto_y = []
    for ind in fronts[0]:
        pareto_x.append(f1[ind])
        pareto_y.append(f2[ind])

    return pareto_x, pareto_y



