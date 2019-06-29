import math


def check_front(j, fronts):
    for front in fronts:
        if j in front:
            return front


def sort_by_values(list1, list2):  # create list of values from list1 with indices from list2 and sort the new list
    values = [list1[ind] for ind in list2]
    return sorted(values)


def nd_sort(population, f1, f2):
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


def crowd_distance(f1, f2, j, front):
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


def sort_parents(fronts, cd, n):
    Pt1 = []
    front = fronts[0]
    i = 0
    while len(Pt1) + len(front) <= n:
        Pt1 += front  # we copy first few fronts
        i += 1
        front = fronts[i]

    cd_Pt_sorted = sort_by_values(cd, front)  # sort values of crowd distance of indices in front by ascending order
    cd_Pt_sorted.reverse()  # reverse, by descending order
    ind_cd_sort = [cd.index(cdp) for cdp in cd_Pt_sorted]  # indices of such sorted list
    Pt1.append(ind_cd_sort[:n - len(Pt1) + 1])  # take only first n-len(Pt1) of them (which have the largest crowd distance)

    return Pt1

