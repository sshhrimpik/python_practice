import numpy as np
import matplotlib.pyplot as plt

def weierstrass(x, a=3, b=0.5, n_terms=50):

    result = np.zeros_like(x, dtype=float)
    for n in range(n_terms):
        result += (b ** n) * np.cos((a ** n) * np.pi * x)
    return result


x = np.linspace(-2, 2, 8000)
y = weierstrass(x, a=3, b=0.5, n_terms=50)

plt.figure()
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Weierstrass function")
plt.grid(True)
plt.show()
