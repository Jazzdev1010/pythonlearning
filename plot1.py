import numpy as np
import matplotlib.pyplot as plt

p=np.arange(0,6,0.1) #generate from 0 to 6 in increment of 0.1
q=np.sin(p)
plt.plot(p,q)
plt.show()