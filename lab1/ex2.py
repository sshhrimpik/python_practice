import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10.01, 0.01)

plt.plot(x, x * x - x -6)
plt.xlabel(r'$x$')
plt.ylabel(r'$y(x)$')
plt.title(r'$ex2$')
plt.grid(True)
plt.show()