import numpy as np
import matplotlib.pyplot as plt

p=np.arange(0,6,0.1) #generate from 0 to 6 in increment of 0.1
q1=np.sin(p)
q2=np.cos(p)

plt.plot(p,q1, label="sin")
plt.plot(p,q2, label="cos", linestyle="--")
plt.xlabel("X")
plt.ylabel("Y")
plt.title('Sin & Cos')
plt.legend()
plt.show()