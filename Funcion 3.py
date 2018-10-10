import matplotlib.pyplot as plt
from numpy import arange, exp

x = arange(0,2, 0.01)
y = (x - 1.5)*exp(-4*(x - 1.5)**2)
plt.plot(x,y)
plt.grid(True)
plt.ylabel('Y')
plt.xlabel('X')
plt.show()