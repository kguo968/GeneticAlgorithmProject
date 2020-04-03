import numpy as np
import matplotlib.pyplot as plt

base = np.genfromtxt("baseline_results.txt")
compare = np.genfromtxt("compare_results.txt")

plt.plot(base, 'ro')
plt.plot(compare, 'bo')

plt.show()

