import numpy as np
import matplotlib.pyplot as plt

colors = ['r','g','b','m','k','y','c']

x = np.linspace(0,2*np.pi,1000)
for i in range(1,6):
    plt.plot(x,np.sin(i*x)/x,colors[i],label="n=" + str(i))

plt.legend()
plt.show(block=True)
