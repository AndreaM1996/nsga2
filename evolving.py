from sorting_strategy import crowd_distance
from sorting_strategy import check_front, sort_parents
from evolution_strategy import children
import math


def evolve(generation, ranks, fronts, parm=False):
    cd = [crowd_distance(generation, j, check_front(j, fronts)) for j in range(len(generation))]
    new = 20
    if parm == False:  # for every other generation
        n = int(len(generation)/2)
        Pt1 = sort_parents(fronts, cd, n)
        generationPt1 = []
        ranksPt1 = []
        cdPt1 = []
        for ind in Pt1:
            generationPt1.append(generation[ind])  # individual with index in Pt1
            ranksPt1.append(ranks[ind])  # rank for such individual
            cdPt1.append(cd[ind])  # crowd distance for such individual
    else:  # for first generation
        generationPt1 = generation
        ranksPt1 = ranks
        cdPt1 = cd
        n = len(generationPt1)

    Qt1 = children(generationPt1, ranksPt1, cdPt1, n)

    final_gen = generationPt1 + Qt1

    return final_gen

