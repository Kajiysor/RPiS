import math
import numpy as np
import matplotlib.pyplot as plt

def rot_func(y_ax):
    x_ax = []
    for i in y_ax:
        if 0<i<=1/6:
            x_ax.append(math.sqrt(6*i)-1)
        elif 1/6<i<=5/6:
            x_ax.append(3*i-1/2)
        elif 5/6<i<=1:
            x_ax.append(3-math.sqrt(6-6*i))
    return x_ax


size1 = 10**3
size2 = 10**5
x = np.array([-1, 0.1, 2.1, 3])
y = np.array([0, 1/3, 1/3, 0])
y1 = np.random.uniform(0, 1, size1)
print (f"{y1 = }")
x1 = rot_func(y1)
print(f"{x1 = }")

plt.title(f"Porównanie funkcji dla {size1} losowanych liczb")
plt.plot(x, y, label="Funkcja Teoretyczna", color = "lime", marker="h")
plt.hist(x1, density=True, bins=60, label='Funkcja "Eksperymentalna"', color="gray", ec = "black")
plt.ylim(0, 0.6)
plt.legend(loc = "best")
plt.savefig("histogram1.pdf", bbox_inches='tight')

plt.clf()

y2 = np.random.uniform(0, 1, size2)
x2 = rot_func(y2)

plt.title(f"Porównanie funkcji dla {size2} losowanych liczb")
plt.plot(x, y, label="Funkcja Teoretyczna", color = "lime", marker="h")
plt.hist(x2, density=True, bins=60, label='Funkcja "Eksperymentalna"', color="gray", ec = "black")
plt.ylim(0, 0.45)
plt.legend(loc = "best")
plt.savefig("histogram2.pdf", bbox_inches='tight')

