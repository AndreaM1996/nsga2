from matplotlib import pyplot as plt
from nsga2 import nsga2

max_gen = 10
gen0 = [[0.22, 0.33, 0.75, 0.04, 0.15, 0.33], [0.62, 0.34, 0.04, 0.94, 0.55, 0.36],
        [0.01, 0.29, 0.66, 0.05, 0.55, 0.47], [0.88, 0.15, 0.38, 0.78, 0.07, 0.7],
        [0.24, 0.99, 0.99, 0.005, 0.77, 0.77]]

m, pa = nsga2(gen0, max_gen)
sortm = sorted(m)
sortpa = sorted(pa)
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111)
ax.scatter(sortpa, sortm)
plt.show()


