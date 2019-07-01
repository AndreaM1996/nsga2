import math
from functions import f_values


def check_front(j, fronts):
    for front in fronts:
        if j in front:
            return front


def sort_by_values(list1, list2):  # create list of values from list1 with indices from list2 and sort the new list
    values = [list1[ind] for ind in list2]
    return sorted(values)


def nd_sort(population):
    f1 = [f_values(individual)[0] for individual in population]
    f2 = [f_values(individual)[1] for individual in population]

    Sp = [[] for i in range(len(population))]
    np = [0 for i in range(len(population))]
    front = [[]]
    rank = [0 for i in range(len(population))]

    for i in range(len(f1)):
        Sp[i] = []
        np[i] = 0
        for j in range(len(f1)):
            if f1[i] <= f1[j] and f2[i] <= f2[j]:
                if j not in Sp[i]:
                    Sp[i].append(j)
            elif f1[j] <= f1[i] and f2[j] <= f2[i]:
                np[i] += 1

        if np[i] == 0:
            rank[i] = 0
            if i not in front[0]:
                front[0].append(i)

    k = 0
    while front[k]:
        Sp2 = []
        for i in front[k]:
            for j in Sp[i]:
                np[j] -= 1
                if np[j] == 0:
                    rank[j] = k + 1
                    if j not in Sp2:
                        Sp2.append(j)
        k += 1
        front.append(Sp2)
    front.pop()
    return front, rank


def crowd_distance(population, j, front):
    f1 = [f_values(individual)[0] for individual in population]
    f2 = [f_values(individual)[1] for individual in population]
    sorted_front1 = sort_by_values(f1, front)
    sorted_front2 = sort_by_values(f2, front)

    if f1[j] == min(sorted_front1) or f1[j] == max(sorted_front1) or f2[j] == min(sorted_front2) or f2[j] == max(sorted_front2):
        return math.inf
    else:
        index1 = sorted_front1.index(f1[j])
        index2 = sorted_front2.index(f2[j])
        return (sorted_front1[index1 + 1] - sorted_front1[index1 - 1]) / \
                      ( max(f1) - min(f1)) + (sorted_front2[index2 + 1] - sorted_front2[index2 - 1]) / \
                      (max(f2) - min(f2))


def sort_ind_by_cd(cd, front):  # sort values of crowd distance of indices in front by descending order
    d = {}
    for ind in front:
        d[ind] = cd[ind]
    items = [(v, k) for k, v in d.items()]
    items = sorted(items, reverse=True)
    return [k for v, k in items]


def sort_parents(fronts, cd, n):
    Pt1 = []
    for front in fronts:
        if len(Pt1) + len(front) <= n:
            Pt1 += front  # we copy first few fronts
        else:
            ind_cd_sort = sort_ind_by_cd(cd, front)  # indices of such sorted list
            k = n - len(Pt1) + 1
            Pt1 += ind_cd_sort[:k]  # take only first n-len(Pt1) of them (which have the largest crowd distance)

    return Pt1

