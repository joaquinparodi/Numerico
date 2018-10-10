import matplotlib.pyplot as plt
from numpy import arange

x = arange(0,2, 0.01)
y = x**2 - 2
plt.plot(x,y)
plt.grid(True)
plt.ylabel('Y')
plt.xlabel('X')
plt.show()