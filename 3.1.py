import numpy as np
import matplotlib.pyplot as plt

c = ['r', 'g', 'b', 'm', 'k', 'y', 'c']
for i in range(0, 3):
    filename = 'csk' + str(i + 1) + '.dat'
    f = open(filename)
    d = f.read()
    f.close()

    data = d.replace('\t', '\n').split('\n')[:-1:]
    l = np.array([float(j) for j in data[0::2]])
    x = np.array(l/11606)
    y = np.array([float(j) for j in data[1::2]])

    new_filename = 'csev' + str(i + 1) + '.dat'
    np.savetxt(new_filename, np.column_stack((x, y)), delimiter='\t', header='x\ty', comments='')

    plt.plot(x, y, c[i], label=filename)
    plt.yscale('log')
    plt.xlim(0, 86.2)

plt.legend()
plt.show(block=True)
