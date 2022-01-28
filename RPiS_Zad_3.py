from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt

rozklad = poisson.rvs(mu=4, size=10000)
plt.hist(rozklad, density=True, edgecolor='black')
plt.savefig('poisson_scipy.pdf')

plt.clf()

rozklad2 = np.random.poisson(4, 10000)
plt.hist(rozklad2, density=True, edgecolor='black')
plt.savefig('poisson_numpy.pdf')

plt.clf()


k = np.arange(0, 17)
pmf = poisson.pmf(k, mu=4)
pmf = np.round(pmf, 5)
plt.plot(k, pmf)
plt.savefig('poisson_pmf.pdf')
