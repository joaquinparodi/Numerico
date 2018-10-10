import matplotlib.pyplot as plt
from numpy import arange

x = arange(0,2, 0.01)
y = x**5 - 6.6*x**4 + 5.12*x**3 + 21.312*x**2 - 38.016*x + 17.28
plt.plot(x,y)
plt.grid(True)
plt.ylabel('Y')
plt.xlabel('X')
plt.show()