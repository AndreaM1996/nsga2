from matplotlib import pyplot as plt
from nsga2 import nsga2
import random

pop_size = 100


gen0 = [[random.uniform(0, 1) for j in range(0, 5)] for i in range(pop_size)]

m, pa = nsga2(gen0, 100)
sortm = sorted(m)
sortpa = sorted(pa)
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111)
ax.scatter(sortm, sortpa)
ax.set_xlabel(u'f\u2081')
ax.set_ylabel(u'f\u2082')

ax.plot(sortm, sortpa, 'r')
plt.show()
